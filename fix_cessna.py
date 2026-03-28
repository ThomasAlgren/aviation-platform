with open('app.py', 'r') as f:
    content = f.read()

old = '    aircraft = {"tail": tail, "model": s(r["model"]) if r else "", "manufacturer": s(r["manufacturer"]) if r else ""}'
new = '''    manufacturer = s(r["manufacturer"]) if r else ""
    model = s(r["model"]) if r else ""
    if model.lower().startswith(manufacturer.lower()):
        model = model[len(manufacturer):].strip()
    aircraft = {"tail": tail, "model": model, "manufacturer": manufacturer}'''

if old in content:
    content = content.replace(old, new)
    print("Fix tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
