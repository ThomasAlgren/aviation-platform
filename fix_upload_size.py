with open('app.py', 'r') as f:
    content = f.read()

old = 'app.config[\'SQLALCHEMY_TRACK_MODIFICATIONS\'] = False'
new = '''app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB'''

if old in content:
    content = content.replace(old, new)
    print("Upload størrelse øget til 16MB!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
