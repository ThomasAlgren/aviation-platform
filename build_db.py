import pandas as pd
import sqlite3
import os
os.makedirs("instance", exist_ok=True)

print("Opretter database...")
conn = sqlite3.connect('instance/panpanparts.db')

print("Loader FAA data...")
faa = pd.read_csv('faa_small.csv', low_memory=False)
ref = pd.read_csv('faa_ref_small.csv', low_memory=False)
ref2 = ref[ref.columns[:3]].copy()
ref2.columns = ['code', 'manufacturer', 'model']
ref2['code'] = ref2['code'].astype(str).str.strip()
faa['MFR MDL CODE'] = faa['MFR MDL CODE'].astype(str).str.strip()
merged = faa.merge(ref2, left_on='MFR MDL CODE', right_on='code', how='left')

aircraft = []
for _, r in merged.iterrows():
    aircraft.append({
        'registration': 'N' + str(r[merged.columns[0]]).strip(),
        'manufacturer': str(r.get('manufacturer', '')).strip(),
        'model': str(r.get('model', '')).strip(),
        'year': str(r.get('YEAR MFR', '')).strip(),
        'serial': str(r.get('SERIAL NUMBER', '')).strip(),
        'country': 'US',
        'source': 'FAA',
        'owner': str(r.get('NAME', '')).strip(),
        'city': str(r.get('CITY', '')).strip(),
        'state': str(r.get('STATE', '')).strip(),
    })
print(f"FAA: {len(aircraft)} fly")

print("Loader dansk data...")
dk = pd.read_csv('denmark.csv')
for _, r in dk.iterrows():
    aircraft.append({
        'registration': str(r.get('registration', '')).strip(),
        'manufacturer': str(r.get('manufacturer', '')).strip(),
        'model': str(r.get('type', '')).strip(),
        'year': str(r.get('year_built', '')).strip(),
        'serial': str(r.get('serial', '')).strip(),
        'country': 'DK',
        'source': 'DCAA',
        'owner': '',
        'city': '',
        'state': 'Denmark',
    })
print(f"Efter DK: {len(aircraft)} fly")

print("Loader norsk data...")
ln = pd.read_csv('ln_register.csv')
for _, r in ln.iterrows():
    aircraft.append({
        'registration': str(r.get('registration', '')).strip(),
        'manufacturer': str(r.get('manufacturer', '')).strip(),
        'model': str(r.get('type', '')).strip(),
        'year': str(r.get('year_built', '')).strip(),
        'serial': str(r.get('serial', '')).strip(),
        'country': 'NO',
        'source': 'CAA-NO',
        'owner': '',
        'city': '',
        'state': 'Norway',
    })
print(f"Efter NO: {len(aircraft)} fly")

print("Loader schweizisk data...")
hb = pd.read_csv('hb_register.csv', sep=';', encoding='utf-16', skipinitialspace=True, low_memory=False)
for _, r in hb.iterrows():
    aircraft.append({
        'registration': str(r.get(' Registration', '')).strip(),
        'manufacturer': str(r.get(' Manufacturer', '')).strip(),
        'model': str(r.get(' Aicraft Model', '')).strip(),
        'year': str(r.get(' Year of Manufacture', '')).strip(),
        'serial': str(r.get(' Serial Number', '')).strip(),
        'country': 'CH',
        'source': 'BAZL',
        'owner': '',
        'city': '',
        'state': 'Switzerland',
    })
print(f"Efter CH: {len(aircraft)} fly")

print("Loader australsk data...")
vh = pd.read_csv('vh_register.csv')
for _, r in vh.iterrows():
    aircraft.append({
        'registration': 'VH-' + str(r.get('Mark', '')).strip(),
        'manufacturer': str(r.get('Manu', '')).strip(),
        'model': str(r.get('Model', '')).strip(),
        'year': str(r.get('Yearmanu', '')).strip(),
        'serial': str(r.get('Serial', '')).strip(),
        'country': 'AU',
        'source': 'CASA',
        'owner': str(r.get('regholdname', '')).strip(),
        'city': str(r.get('regholdSuburb', '')).strip(),
        'state': 'Australia',
    })
print(f"Efter AU: {len(aircraft)} fly")

print("Gemmer til database...")
print('Loader canadisk data...')
import csv
canada_aircraft = []
with open('carscurr.txt', 'r', encoding='latin-1') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 7:
            continue
        mark = row[0].strip()
        if not mark:
            continue
        canada_aircraft.append({
            'registration': 'C-' + mark,
            'manufacturer': row[3].strip() if len(row) > 3 else '',
            'model': row[4].strip() if len(row) > 4 else '',
            'year': '',
            'serial': row[5].strip() if len(row) > 5 else '',
            'country': 'CA',
        'source': 'TC',
            'owner': '',
            'city': '',
            'state': 'Canada',
        })
aircraft.extend(canada_aircraft)
print(f'Efter CA: {len(aircraft)} fly')

print('Loader østrigsk data...')
import csv
austria_aircraft = []
with open('ACG_LFZ_24032026.csv', 'r', encoding='latin-1') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        reg = row.get('Registration ', '').strip()
        if not reg:
            continue
        austria_aircraft.append({
            'registration': 'OE-' + reg,
            'manufacturer': row.get('Manufacturer', '').strip(),
            'model': row.get('Manufacturer ', '').strip(),
            'year': '',
            'serial': row.get('Serial number', '').strip(),
            'country': 'AT',
        'source': 'Austrocontrol',
            'owner': row.get('Operator', '').strip()[:100],
            'city': '',
            'state': 'Austria',
        })
aircraft.extend(austria_aircraft)
print(f'Efter AT: {len(aircraft)} fly')


print('Loader OpenSky data (nye lande)...')
import pandas as pd
osky = pd.read_csv('opensky.csv', low_memory=False, on_bad_lines='skip')
osky.columns = osky.columns.str.replace(chr(39), '')
exclude = ['United States', 'Canada', 'Australia', 'Denmark', 'Norway', 'Switzerland', 'Austria']
osky_new = osky[~osky['country'].isin(exclude)]
opensky_aircraft = []
for _, r in osky_new.iterrows():
    reg = str(r.get('registration', '')).replace(chr(39), '').strip()
    if not reg or reg == 'nan':
        continue
    opensky_aircraft.append({
        'registration': reg,
        'manufacturer': str(r.get('manufacturerName', '')).replace(chr(39), '').strip(),
        'model': str(r.get('model', '')).replace(chr(39), '').strip(),
        'year': str(r.get('built', '')).replace(chr(39), '').strip()[:4],
        'serial': str(r.get('serialNumber', '')).replace(chr(39), '').strip(),
        'country': str(r.get('country', '')).replace(chr(39), '').strip()[:2],
        'owner': str(r.get('owner', '')).replace(chr(39), '').strip()[:100],
        'source': 'OpenSky',
        'city': '',
        'state': str(r.get('country', '')).replace(chr(39), '').strip(),
    })
aircraft.extend(opensky_aircraft)
print(f'Efter OpenSky: {len(aircraft)} fly')

df = pd.DataFrame(aircraft)
df.to_sql('aircraft', conn, if_exists='replace', index=False)
conn.execute('CREATE INDEX IF NOT EXISTS idx_registration ON aircraft(registration)')
conn.commit()
conn.close()
print(f"FAERDIG! {len(df)} fly i databasen!")

