
with open('app.py', 'r') as f:
    content = f.read()

old = '        <a href="/my-profile" class="back">← My profile</a>\n        <h1 style="font-size:32px;margin-bottom:24px">My <span style="color:#ff6b35">Logbook</span></h1>'
new = '''        <a href="/my-profile" class="back">← My profile</a>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px">
            <h1 style="font-size:32px">My <span style="color:#ff6b35">Logbook</span></h1>
            <div style="text-align:right">
                <div style="font-size:36px;font-weight:700;color:#ff6b35;font-family:monospace">{{ total_time }}</div>
                <div style="font-size:12px;color:#666">Total flight hours</div>
                <div style="font-size:12px;color:#444">{{ total_flights }} flights</div>
            </div>
        </div>'''

if old in content:
    content = content.replace(old, new)
    print("Header opdateret!")
else:
    print("Header IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
