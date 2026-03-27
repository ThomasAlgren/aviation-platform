with open('app.py', 'r') as f:
    content = f.read()

old = '                        <input type="file" id="cert-photo" accept="image/*" onchange="loadCertPhoto(this)" style="margin-bottom:10px">'
new = '                        <input type="file" id="cert-photo" accept="image/*" capture="environment" onchange="loadCertPhoto(this)" style="margin-bottom:10px">'

if old in content:
    content = content.replace(old, new)
    print("Kamera tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
