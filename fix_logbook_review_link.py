with open('app.py', 'r') as f:
    content = f.read()

old = '            <button class="scan-btn" id="scan-btn" onclick="scanPages()" disabled>Scan with AI</button>'
new = '            <button class="scan-btn" id="scan-btn" onclick="scanPages()" disabled>Scan with AI</button>\n            <a href="/logbook-review" style="display:block;text-align:center;margin-top:10px;color:#ff6b35;font-size:14px">Or use step-by-step review →</a>'

if old in content:
    content = content.replace(old, new)
    print("Link tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
