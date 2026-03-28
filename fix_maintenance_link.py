with open('app.py', 'r') as f:
    content = f.read()

old = '            <a href="/upload-arc/{{ aircraft.tail }}" class="action-btn">Upload & verify ARC with AI <span>→</span></a>\n            <a href="/parts?q={{ aircraft.manufacturer }}" class="action-btn">Find parts for {{ aircraft.manufacturer }} {{ aircraft.model }} <span>→</span></a>\n            <a href="/sell-aircraft/{{ aircraft.tail }}" class="action-btn">List this aircraft for sale <span>→</span></a>'

new = '            <a href="/upload-arc/{{ aircraft.tail }}" class="action-btn">Upload & verify ARC with AI <span>→</span></a>\n            <a href="/my-aircraft/{{ aircraft.tail }}/maintenance" class="action-btn">✦ Maintenance log <span>→</span></a>\n            <a href="/parts?q={{ aircraft.manufacturer }}" class="action-btn">Find parts for {{ aircraft.manufacturer }} {{ aircraft.model }} <span>→</span></a>\n            <a href="/sell-aircraft/{{ aircraft.tail }}" class="action-btn">List this aircraft for sale <span>→</span></a>'

if old in content:
    content = content.replace(old, new)
    print("Maintenance link tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
