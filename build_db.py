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
vh = pd.read_csv('vh_register.csv')
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