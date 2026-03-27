with open('app.py', 'r') as f:
    content = f.read()

old = '''        <div class="card">
            <h3>Own this aircraft?</h3>
            <p style="color:#666; font-size:14px; margin-bottom:16px">Claim your aircraft profile to add photos, flight hours, avionics and maintenance history.</p>
            <a href="/claim/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;margin-bottom:10px">Claim {{ aircraft.tail }} — it\'s free</a>
            <a href="/upload-arc/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2d7a3a;margin-bottom:10px">✓ Upload ARC — verify airworthiness</a>
            <a href="/upload-aircraft?tail={{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2a2a3e">List {{ aircraft.tail }} for sale</a>
        </div>'''

new = '''        <div class="card">
            <h3>Own this aircraft?</h3>
            <p style="color:#666; font-size:14px; margin-bottom:16px">Claim your aircraft profile to add photos, flight hours, avionics and maintenance history.</p>
            <a href="/claim/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;margin-bottom:10px">Claim {{ aircraft.tail }} — it\'s free</a>
            <a href="/upload-arc/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2d7a3a;margin-bottom:10px">✓ Upload ARC — verify airworthiness</a>
            <a href="/upload-aircraft?tail={{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2a2a3e">List {{ aircraft.tail }} for sale</a>
            {% if arc_info and arc_info.disputed %}
            <div style="background:rgba(255,193,7,0.15);border:1px solid rgba(255,193,7,0.3);border-radius:8px;padding:12px;margin-top:10px;color:#ffc107;font-size:13px">
                ⚠ This claim is disputed and under review
            </div>
            {% endif %}
            <a href="/protest-claim/{{ aircraft.tail }}" style="display:block;text-align:center;text-decoration:none;color:#666;font-size:13px;margin-top:12px">
                Report incorrect claim
            </a>
        </div>'''

if old in content:
    content = content.replace(old, new)
    print("Protest knap tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
