with open('app.py', 'r') as f:
    content = f.read()

# Tilføj hjælpefunktion til at normalisere datoer
old = 'app.config[\'SECRET_KEY\'] = os.environ.get(\'SECRET_KEY\', \'dev-secret-key-change-in-production\')'
new = '''app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

def normalize_date(value):
    """Konverter alle datoformater til YYYY-MM-DD"""
    if not value:
        return None
    value = str(value).strip()
    from datetime import datetime
    for fmt in ['%Y-%m-%d', '%Y%m%d', '%d/%m/%Y', '%d/%m/%y', '%m/%d/%Y']:
        try:
            d = datetime.strptime(value, fmt)
            return d.strftime('%Y-%m-%d')
        except:
            pass
    return value'''

if old in content:
    content = content.replace(old, new)
    print("normalize_date tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
