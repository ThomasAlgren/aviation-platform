with open('app.py', 'r') as f:
    content = f.read()

# Tilføj en dato-format funktion til Jinja2
old = 'app.config[\'SECRET_KEY\'] = os.environ.get(\'SECRET_KEY\', \'dev-secret-key-change-in-production\')'
new = '''app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.template_filter('format_date')
def format_date(value):
    if not value:
        return 'Not registered'
    try:
        from datetime import datetime
        for fmt in ['%Y-%m-%d', '%Y%m%d', '%d/%m/%Y']:
            try:
                d = datetime.strptime(str(value), fmt)
                return d.strftime('%d %b %Y')
            except:
                pass
    except:
        pass
    return value'''

if old in content:
    content = content.replace(old, new)
    print("Format filter tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
