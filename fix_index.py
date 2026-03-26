with open('app.py', 'r') as f:
    content = f.read()

old = '''@app.route("/")
def index():
    import os
    if not os.path.exists('instance/panpanparts.db'):
        return "<html><body style='font-family:sans-serif;text-align:center;padding:100px'><h1>PanPanParts</h1><p>Loading aircraft database... please refresh in 30 seconds.</p></body></html>"'''

new = '''@app.route("/")
def index():'''

content = content.replace(old, new)

if new in content:
    print("FUNDET OG ERSTATTET!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
