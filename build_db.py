import pandas as pd
import sqlite3
import os
os.makedirs("instance", exist_ok=True)

print("Opretter database...")
conn = sqlite3.connect('instance/panpanparts.db')

print("Downloader FAA data fra FAA.gov...")
import urllib.request
import zipfile
urllib.request.urlretrieve(
    'https://registry.faa.gov/database/ReleasableAircraft.zip',
    'faa_data.zip'
)
with zipfile.ZipFile('faa_data.zip', 'r') as z:
    z.extractall('faa_data')
faa = pd.read_csv('faa_data/MASTER.txt', low_memory=False)
ref = pd.read_csv('faa_data/ACFTREF.txt', low_memory=False)
ref2 = ref[ref.columns[:3]].copy()
ref2.columns = ['code', 'manufacturer', 'model']
ref2['code'] = ref2['code'].astype(str).str.strip()
faa[faa.columns[4]] = faa[faa.columns[4]].astype(str).str.strip()
merged = faa.merge(ref2, left_on=faa.columns[4], right_on='code', how='left')

aircraft = []
for _, r in merged.iterrows():
    aircraft.append({
        'registration': 'N' + str(r[merged.columns[0]]).strip(),
        'manufacturer': str(r.get('manufacturer', '')).strip(),
        'model': str(r.get('model', '')).strip(),
        'year': str(r.get('YEAR MFR', '')).strip(),
        'serial': str(r.get('SERIAL NUMBER', '')).strip(),
        'country': 'US',
        'owner': str(r.get('NAME', '')).strip(),
        'city': str(r.get('CITY', '')).strip(),
        'state': str(r.get('STATE', '')).strip(),
    })
print(f"FAA: {len(aircraft)} fly")

print("Loader dansk data...")
dk = pd.read_pickle('denmark.pkl')
for _, r in dk.iterrows():
    aircraft.append({
        'registration': str(r.get('registration', '')).strip(),
        'manufacturer': str(r.get('manufacturer', '')).strip(),
        'model': str(r.get('type', '')).strip(),
        'year': str(r.get('year_built', '')).strip(),
        'serial': str(r.get('serial', '')).strip(),
        'country': 'DK',
        'owner': '',
        'city': '',
        'state': 'Denmark',
    })
print(f"Efter DK: {len(aircraft)} fly")

print("Loader norsk data...")
ln = pd.read_pickle('ln_register.pkl')
for _, r in ln.iterrows():
    aircraft.append({
        'registration': str(r.get('registration', '')).strip(),
        'manufacturer': str(r.get('manufacturer', '')).strip(),
        'model': str(r.get('type', '')).strip(),
        'year': str(r.get('year_built', '')).strip(),
        'serial': str(r.get('serial', '')).strip(),
        'country': 'NO',
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
        'owner': '',
        'city': '',
        'state': 'Switzerland',
    })
print(f"Efter CH: {len(aircraft)} fly")

print("Loader australsk data...")
vh = pd.read_pickle('vh_register.pkl')
for _, r in vh.iterrows():
    aircraft.append({
        'registration': 'VH-' + str(r.get('Mark', '')).strip(),
        'manufacturer': str(r.get('Manu', '')).strip(),
        'model': str(r.get('Model', '')).strip(),
        'year': str(r.get('Yearmanu', '')).strip(),
        'serial': str(r.get('Serial', '')).strip(),
        'country': 'AU',
        'owner': str(r.get('regholdname', '')).strip(),
        'city': str(r.get('regholdSuburb', '')).strip(),
        'state': 'Australia',
    })
print(f"Efter AU: {len(aircraft)} fly")

print("Gemmer til database...")
df = pd.DataFrame(aircraft)
df.to_sql('aircraft', conn, if_exists='replace', index=False)
conn.execute('CREATE INDEX IF NOT EXISTS idx_registration ON aircraft(registration)')
conn.commit()
conn.close()
print(f"FAERDIG! {len(df)} fly i databasen!")