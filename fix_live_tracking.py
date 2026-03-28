with open('app.py', 'r') as f:
    content = f.read()

old = '''            <div class="field"><span class="field-label">Registered</span><span class="field-value">{{ aircraft.reg_date }}</span></div>
        </div>

        {% if aircraft.previous %}'''

new = '''            <div class="field"><span class="field-label">Registered</span><span class="field-value">{{ aircraft.reg_date }}</span></div>
        </div>

        <!-- Live tracking -->
        <div class="card" id="live-card">
            <h3>Live status</h3>
            <div id="live-status" style="color:#666;font-size:14px">Checking live position...</div>
        </div>

        <script>
        fetch('/api/live/{{ aircraft.tail }}')
            .then(r => r.json())
            .then(data => {
                var card = document.getElementById('live-card');
                var status = document.getElementById('live-status');
                if (data.airborne) {
                    card.style.borderColor = '#4caf50';
                    status.innerHTML = 
                        '<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px">' +
                        '<span style="width:10px;height:10px;background:#4caf50;border-radius:50%;display:inline-block;animation:pulse 1s infinite"></span>' +
                        '<span style="color:#4caf50;font-weight:600">AIRBORNE — ' + data.callsign + '</span></div>' +
                        '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">' +
                        '<div><div style="font-size:24px;font-weight:700;color:#ff6b35">' + data.altitude + 'm</div><div style="font-size:11px;color:#666">ALTITUDE</div></div>' +
                        '<div><div style="font-size:24px;font-weight:700;color:#ff6b35">' + data.speed + 'km/h</div><div style="font-size:11px;color:#666">SPEED</div></div>' +
                        '<div><div style="font-size:24px;font-weight:700;color:#ff6b35">' + data.heading + '°</div><div style="font-size:11px;color:#666">HEADING</div></div>' +
                        '</div>' +
                        '<a href="https://www.flightradar24.com/' + data.callsign + '" target="_blank" style="display:block;margin-top:12px;color:#4a9eff;font-size:13px">View on FlightRadar24 →</a>';
                } else {
                    status.innerHTML = '<span style="color:#444">⬤</span> Currently on ground';
                }
            })
            .catch(() => {
                document.getElementById('live-status').textContent = 'Live data unavailable';
            });
        </script>
        <style>
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
        </style>

        {% if aircraft.previous %}'''

if old in content:
    content = content.replace(old, new)
    print("Live tracking tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
