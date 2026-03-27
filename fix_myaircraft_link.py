with open('app.py', 'r') as f:
    content = f.read()

old = '            <a class="aircraft-card" href="/aircraft/{{ a.tail }}">'
new = '            <a class="aircraft-card" href="/my-aircraft/{{ a.tail }}">'

if old in content:
    content = content.replace(old, new)
    print("Link rettet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
