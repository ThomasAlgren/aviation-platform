"""
update_registries.py — Månedlig opdatering af alle flyregistre
Køres automatisk den 1. hver måned via APScheduler i app.py
Kan også køres manuelt: python update_registries.py

DATAKILDER:
-----------
Land        | Kilde                                                          | Metode
----------- | -------------------------------------------------------------- | ---------
USA (N-)    | https://registry.faa.gov/database/ReleasableAircraft.zip       | Auto
Sverige(SE-)| https://raw.githubusercontent.com/civictechsweden/...          | Auto
Norge (LN-) | https://data.caa.no/nlr/norgesluftfartoyregister.json          | Auto
Australien  | https://www.casa.gov.au/files/acrftregcsv                      | Auto
Canada (C-) | https://wwwapps.tc.gc.ca/Saf-Sec-Sur/2/CCARCS-RIACC/DDZip.aspx| Auto
Danmark(OY-)| https://www.danishaircraft.dk/list (scrape)                    | Auto scrape
Schweiz(HB-)| https://app02.bazl.admin.ch — manuel download                 | Manuel fil-drop
Østrig (OE-)| https://www.austrocontrol.at — manuel download                 | Manuel fil-drop
OpenSky     | https://opensky-network.org/datasets/metadata/                 | Auto

MANUEL FIL-DROP PROCEDURE:
--------------------------
For Schweiz og Østrig: download filen fra kilden og læg den i samme mappe som dette script.
Scriptet finder automatisk den nyeste fil med det rigtige navn:
  - Schweiz:  hb_register.csv  (semikolon-separeret, UTF-16)
  - Østrig:   ACG_LFZ_*.csv    (semikolon-separeret, latin-1)

Nye lande tilføjes ved at:
1. Tilføje kilden i kommentaren øverst
2. Skrive en fetch_XXX() funktion
3. Kalde den i run_all_updates()
"""

import os
import csv
import json
import zipfile
import requests
import psycopg2
import psycopg2.extras
import pandas as pd
import time
import glob
from io import StringIO, BytesIO
from datetime import datetime

# Mappe hvor manuelle filer lægges (samme som scriptet)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_conn():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def upsert_aircraft(conn, data, country_code, batch_size=10000):
    """Slet alle fly for landet og indsæt nye i batches"""
    cur = conn.cursor()
    cur.execute("DELETE FROM aircraft WHERE country = %s", (country_code,))
    conn.commit()
    total = 0
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        psycopg2.extras.execute_batch(cur, '''
            INSERT INTO aircraft (registration, manufacturer, model, year, serial, country, source, owner, city, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', batch)
        conn.commit()
        total += len(batch)
        if country_code == 'US':
            print(f"  US: {total}/{len(data)} indsat...")
    cur.close()
    print(f"  {country_code}: {len(data)} fly opdateret")

# ─────────────────────────────────────────────
# AUTO: Sverige
# ─────────────────────────────────────────────
def fetch_sweden():
    print("Sverige (SE)...")
    url = 'https://raw.githubusercontent.com/civictechsweden/oppna-luftfartygsregistret/master/register.csv'
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.text), dtype=str)
    active = df[df['Avregistrerad'].isna()].copy()
    data = []
    for _, row in active.iterrows():
        data.append((
            str(row.get('code', '') or '')[:20],
            '',
            str(row.get('Luftfartygstyp', '') or '')[:200],
            str(row.get('Tillverkningsår', '') or '')[:10],
            str(row.get('Tillverkningsnummer', '') or '')[:100],
            'SE',
            'Transportstyrelsen',
            str(row.get('owner.name', '') or '')[:200],
            '',
            'Sweden'
        ))
    return data

# ─────────────────────────────────────────────
# AUTO: Norge
# ─────────────────────────────────────────────
def fetch_norway():
    print("Norge (NO)...")
    url = 'https://data.caa.no/nlr/norgesluftfartoyregister.json'
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    payload = r.json()
    records = payload.get('data', [])
    data = []
    for row in records:
        reg = str(row.get('Registreringsmerke', '') or '').strip()
        if not reg:
            continue
        data.append((
            reg,
            str(row.get('Produsent', '') or '')[:200],
            str(row.get('Type', '') or '')[:200],
            '',
            '',
            'NO',
            'CAA-NO',
            str(row.get('Eier/Kontakt', '') or '')[:200],
            '',
            'Norway'
        ))
    return data

# ─────────────────────────────────────────────
# AUTO: Australien
# ─────────────────────────────────────────────
def fetch_australia():
    print("Australien (AU)...")
    url = 'https://www.casa.gov.au/files/acrftregcsv'
    r = requests.get(url, timeout=120, headers=HEADERS)
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.text), low_memory=False)
    data = []
    for _, row in df.iterrows():
        mark = str(row.get('Mark', '') or '').strip()
        if not mark:
            continue
        data.append((
            'VH-' + mark,
            str(row.get('Manu', '') or '')[:200],
            str(row.get('Model', '') or '')[:200],
            str(row.get('Yearmanu', '') or '')[:10],
            str(row.get('Serial', '') or '')[:100],
            'AU',
            'CASA',
            str(row.get('regholdname', '') or '')[:200],
            str(row.get('regholdSuburb', '') or '')[:100],
            'Australia'
        ))
    return data

# ─────────────────────────────────────────────
# AUTO: Canada
# ─────────────────────────────────────────────
def fetch_canada():
    print("Canada (CA)...")
    # Transport Canada CCARCS direkte ZIP download
    url = 'https://wwwapps.tc.gc.ca/Saf-Sec-Sur/2/CCARCS-RIACC/download/carsall.zip'
    r = requests.get(url, timeout=60, headers=HEADERS)
    if r.status_code != 200:
        # Fallback: brug lokal fil hvis den findes
        local = os.path.join(SCRIPT_DIR, 'carscurr.txt')
        if os.path.exists(local):
            print("  Bruger lokal carscurr.txt")
            with open(local, 'r', encoding='latin-1') as f:
                content = f.read()
        else:
            raise Exception(f"Canada download fejlede ({r.status_code}) og ingen lokal fil fundet")
        reader = csv.reader(StringIO(content))
        data = []
        for row in reader:
            if len(row) < 5:
                continue
            mark = row[0].strip()
            if not mark:
                continue
            def clean(s):
                return s.encode('ascii', 'ignore').decode('ascii').strip()[:200]
            data.append((
                'C-' + clean(mark),
                clean(row[3]) if len(row) > 3 else '',
                clean(row[4]) if len(row) > 4 else '',
                '',
                clean(row[5]) if len(row) > 5 else '',
                'CA', 'TC', '', '', 'Canada'
            ))
        return data
    z = zipfile.ZipFile(BytesIO(r.content))
    # Find carscurr.txt (case-insensitive)
    target = None
    for name in z.namelist():
        if 'carscurr' in name.lower():
            target = name
            break
    if not target:
        raise Exception("carscurr.txt ikke fundet i ZIP")
    content = z.read(target).decode('latin-1')
    data = []
    reader = csv.reader(StringIO(content))
    for row in reader:
        if len(row) < 5:
            continue
        mark = row[0].strip()
        if not mark:
            continue
        data.append((
            'C-' + mark,
            row[3].strip() if len(row) > 3 else '',
            row[4].strip() if len(row) > 4 else '',
            '',
            row[5].strip() if len(row) > 5 else '',
            'CA',
            'TC',
            '',
            '',
            'Canada'
        ))
    return data

# ─────────────────────────────────────────────
# AUTO: USA (FAA)
# ─────────────────────────────────────────────
def fetch_usa():
    print("USA (US)...")
    url = 'https://registry.faa.gov/database/ReleasableAircraft.zip'
    r = requests.get(url, timeout=120, headers=HEADERS)
    if r.status_code != 200:
        # Fallback: brug lokale filer hvis de findes
        master_path = os.path.join(SCRIPT_DIR, 'faa_small.csv')
        ref_path = os.path.join(SCRIPT_DIR, 'faa_ref_small.csv')
        if os.path.exists(master_path) and os.path.exists(ref_path):
            print("  Bruger lokale faa_small.csv filer")
            master = pd.read_csv(master_path, dtype=str, low_memory=False)
            ref = pd.read_csv(ref_path, dtype=str, low_memory=False)
            ref2 = ref[ref.columns[:3]].copy()
            ref2.columns = ['code', 'MFR', 'MODEL']
            ref2['code'] = ref2['code'].str.strip()
            master['MFR MDL CODE'] = master['MFR MDL CODE'].astype(str).str.strip()
            merged = master.merge(ref2, left_on='MFR MDL CODE', right_on='code', how='left')
            data = []
            for _, row in merged.iterrows():
                n_num = str(row.get(merged.columns[0], '') or '').strip()
                if not n_num:
                    continue
                data.append(('N' + n_num, str(row.get('MFR',''))[:200], str(row.get('MODEL',''))[:200],
                    str(row.get('YEAR MFR',''))[:10], str(row.get('SERIAL NUMBER',''))[:100],
                    'US', 'FAA', str(row.get('NAME',''))[:200], str(row.get('CITY',''))[:100], str(row.get('STATE',''))[:100]))
            return data
        raise Exception(f"FAA download fejlede ({r.status_code}) og ingen lokale filer fundet")
    z = zipfile.ZipFile(BytesIO(r.content))
    
    # MASTER.txt = registreringer, ACFTREF.txt = type reference
    master = pd.read_csv(z.open('MASTER.txt'), dtype=str, low_memory=False)
    ref = pd.read_csv(z.open('ACFTREF.txt'), dtype=str, low_memory=False)
    
    ref.columns = ref.columns.str.strip()
    master.columns = master.columns.str.strip()
    
    ref2 = ref[['CODE', 'MFR', 'MODEL']].copy()
    ref2['CODE'] = ref2['CODE'].str.strip()
    master['MFR MDL CODE'] = master['MFR MDL CODE'].str.strip()
    merged = master.merge(ref2, left_on='MFR MDL CODE', right_on='CODE', how='left')
    
    data = []
    for _, row in merged.iterrows():
        n_num = str(row.get('N-NUMBER', '') or '').strip()
        if not n_num:
            continue
        data.append((
            'N' + n_num,
            str(row.get('MFR', '') or '')[:200],
            str(row.get('MODEL', '') or '')[:200],
            str(row.get('YEAR MFR', '') or '')[:10],
            str(row.get('SERIAL NUMBER', '') or '')[:100],
            'US',
            'FAA',
            str(row.get('NAME', '') or '')[:200],
            str(row.get('CITY', '') or '')[:100],
            str(row.get('STATE', '') or '')[:100]
        ))
    return data

# ─────────────────────────────────────────────
# AUTO: Danmark (scrape danishaircraft.dk)
# ─────────────────────────────────────────────
def fetch_denmark():
    print("Danmark (DK) — scraper danishaircraft.dk...")
    import re
    base_url = 'https://www.danishaircraft.dk/list'
    records = []
    page = 0

    while True:
        url = base_url if page == 0 else f'{base_url}/{page}'
        try:
            r = requests.get(url, timeout=15, headers=HEADERS)
            r.raise_for_status()
        except Exception as e:
            print(f"  Stop ved side {page}: {e}")
            break

        # Find alle tabelrækker — HTML er på én linje med enkelt-quotes
        # Kolonner: href, reg, type, serial, reg_date, cancelled
        rows = re.findall(
            r"<tr><td><a href='/show/([^']+)'>([^<]+)</a></td><td>([^<]*)</td><td>([^<]*)</td><td>([^<]*)</td><td>([^<]*)</td>",
            r.text
        )

        if not rows:
            break

        new_rows = 0
        for row in rows:
            reg = row[1].strip()
            aircraft_type = row[2].strip()
            serial = row[3].strip()
            cancelled = row[5].strip()

            # Spring aflyste fly over
            if cancelled and cancelled not in ('', 'NTU'):
                continue

            records.append((
                reg, '', aircraft_type, '', serial,
                'DK', 'DCAA', '', '', 'Denmark'
            ))
            new_rows += 1

        if new_rows == 0:
            break

        page += 1
        time.sleep(0.5)

        if page % 50 == 0:
            print(f"  ...side {page}, {len(records)} fly indtil videre")

    return records

# ─────────────────────────────────────────────
# MANUEL: Schweiz (fil-drop)
# ─────────────────────────────────────────────
def fetch_switzerland():
    print("Schweiz (CH) — leder efter hb_register.csv...")
    filepath = os.path.join(SCRIPT_DIR, 'hb_register.csv')
    if not os.path.exists(filepath):
        print("  SPRING OVER: hb_register.csv ikke fundet — download fra bazl.admin.ch og læg i projektmappen")
        return None
    
    hb = pd.read_csv(filepath, sep=';', encoding='utf-16', skipinitialspace=True, low_memory=False)
    data = []
    for _, row in hb.iterrows():
        reg = str(row.get(' Registration', '') or '').strip()
        if not reg:
            continue
        data.append((
            reg,
            str(row.get(' Manufacturer', '') or '')[:200],
            str(row.get(' Aicraft Model', '') or '')[:200],
            str(row.get(' Year of Manufacture', '') or '')[:10],
            str(row.get(' Serial Number', '') or '')[:100],
            'CH',
            'BAZL',
            '',
            '',
            'Switzerland'
        ))
    return data

# ─────────────────────────────────────────────
# MANUEL: Østrig (fil-drop)
# ─────────────────────────────────────────────
def fetch_austria():
    print("Østrig (AT) — leder efter ACG_LFZ_*.csv...")
    files = sorted(glob.glob(os.path.join(SCRIPT_DIR, 'ACG_LFZ_*.csv')))
    if not files:
        print("  SPRING OVER: ACG_LFZ_*.csv ikke fundet — download fra austrocontrol.at og læg i projektmappen")
        return None
    
    filepath = files[-1]  # Nyeste fil
    print(f"  Bruger: {os.path.basename(filepath)}")
    data = []
    with open(filepath, 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            reg = row.get('Registration ', '').strip()
            if not reg:
                continue
            data.append((
                'OE-' + reg,
                row.get('Manufacturer', '').strip()[:200],
                row.get('Manufacturer ', '').strip()[:200],
                '',
                row.get('Serial number', '').strip()[:100],
                'AT',
                'Austrocontrol',
                row.get('Operator', '').strip()[:200],
                '',
                'Austria'
            ))
    return data

# ─────────────────────────────────────────────
# HOVED-FUNKTION
# ─────────────────────────────────────────────
def run_all_updates():
    print(f"\n{'='*50}")
    print(f"Starter månedlig opdatering: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*50}")
    
    conn = get_conn()
    results = {}
    
    fetchers = [
        ('SE', fetch_sweden),
        ('NO', fetch_norway),
        ('AU', fetch_australia),
        ('CA', fetch_canada),
        ('DK', fetch_denmark),
        ('CH', fetch_switzerland),
        ('AT', fetch_austria),
        ('US', fetch_usa),  # Sidst — stor fil, må ikke crashe resten
    ]
    
    for country_code, fetcher in fetchers:
        try:
            data = fetcher()
            if data is not None:
                upsert_aircraft(conn, data, country_code)
                results[country_code] = len(data)
            else:
                results[country_code] = 'SPRING OVER'
        except Exception as e:
            print(f"  FEJL {country_code}: {e}")
            results[country_code] = f'FEJL: {e}'
    
    conn.close()
    
    print(f"\n{'='*50}")
    print("RESULTAT:")
    for country, result in results.items():
        print(f"  {country}: {result}")
    print(f"{'='*50}\n")
    
    return results

if __name__ == '__main__':
    run_all_updates()
