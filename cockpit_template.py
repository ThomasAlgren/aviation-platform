AIRCRAFT_COCKPIT_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>{{ aircraft.tail }} Cockpit - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 900px; margin: 40px auto; padding: 0 20px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }
        .back:hover { color: white; }

        /* Hero */
        .hero { background: linear-gradient(135deg, #1a1a2e, #16213e); border-radius: 16px; padding: 32px; margin-bottom: 24px; border: 1px solid #2a2a3e; display: flex; justify-content: space-between; align-items: center; }
        .hero-tail { font-size: 52px; font-weight: 800; color: #ff6b35; font-family: monospace; letter-spacing: 2px; }
        .hero-model { font-size: 20px; color: #ccc; margin-top: 6px; }
        .hero-meta { color: #666; font-size: 14px; margin-top: 4px; }
        .status-badge { padding: 8px 20px; border-radius: 20px; font-size: 14px; font-weight: 600; }
        .status-ok { background: rgba(76,175,80,0.2); color: #4caf50; border: 1px solid rgba(76,175,80,0.3); }
        .status-warn { background: rgba(255,193,7,0.2); color: #ffc107; border: 1px solid rgba(255,193,7,0.3); }
        .status-alert { background: rgba(255,107,53,0.2); color: #ff6b35; border: 1px solid rgba(255,107,53,0.3); }

        /* Grid */
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
        .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 16px; }

        /* Cards */
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .card-full { grid-column: 1 / -1; }

        /* Date items */
        .date-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #2a2a3e; }
        .date-item:last-child { border-bottom: none; }
        .date-label { color: #aaa; font-size: 14px; }
        .date-value { font-size: 14px; font-weight: 600; }
        .date-ok { color: #4caf50; }
        .date-warn { color: #ffc107; }
        .date-alert { color: #ff6b35; }
        .date-missing { color: #444; font-style: italic; font-weight: 400; }

        /* Documents */
        .doc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .doc-item { background: #0d0d1a; border-radius: 8px; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center; border: 1px solid #2a2a3e; cursor: pointer; }
        .doc-item:hover { border-color: #ff6b35; }
        .doc-name { font-size: 13px; color: #ccc; }
        .doc-status { font-size: 18px; }

        /* Hours */
        .hours-value { font-size: 36px; font-weight: 700; color: #ff6b35; }
        .hours-label { font-size: 12px; color: #666; margin-top: 4px; }

        /* Edit form */
        .edit-btn { background: transparent; border: 1px solid #333; color: #aaa; padding: 6px 14px; border-radius: 6px; font-size: 12px; cursor: pointer; float: right; margin-top: -4px; }
        .edit-btn:hover { border-color: #ff6b35; color: #ff6b35; }
        input[type=text], input[type=date], input[type=number], textarea, select { width: 100%; padding: 10px 12px; border: 1px solid #333; border-radius: 8px; font-size: 14px; margin-bottom: 10px; background: #0d0d1a; color: white; }
        .save-btn { background: #ff6b35; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 14px; cursor: pointer; font-weight: 600; width: 100%; margin-top: 4px; }
        .hidden { display: none; }

        /* Actions */
        .action-btn { display: block; background: #1a1a2e; border: 1px solid #2a2a3e; color: #aaa; padding: 14px 20px; border-radius: 10px; text-decoration: none; font-size: 14px; margin-bottom: 8px; }
        .action-btn:hover { border-color: #ff6b35; color: white; }
        .action-btn span { float: right; }

        .user-menu { position: relative; margin-left: 8px; }
        .user-btn { background: #1a1a2e; color: #aaa; border: 1px solid #333; padding: 8px 16px; border-radius: 8px; font-size: 14px; cursor: pointer; }
        .dropdown { display: none; position: absolute; right: 0; top: 44px; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 8px; min-width: 140px; z-index: 100; }
        .dropdown a { display: block; padding: 12px 16px; color: #aaa; text-decoration: none; font-size: 14px; }
        .dropdown a:hover { color: white; background: #2a2a3e; }
        .dropdown.open { display: block; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/parts">Parts</a>
            <div class="user-menu">
                <button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} ▾</button>
                <div class="dropdown">
                    <a href="/my-aircraft">My aircraft</a>
                    <a href="/my-profile">My profile</a>
                    <a href="/my-listings">My listings</a>
                    <a href="/logout">Log out</a>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <a href="/my-aircraft" class="back">← My aircraft</a>

        <!-- Hero -->
        <div class="hero">
            <div>
                <div class="hero-tail">{{ aircraft.tail }}</div>
                <div class="hero-model">{{ aircraft.manufacturer }} {{ aircraft.model }}</div>
                <div class="hero-meta">{{ aircraft.year }}{% if aircraft.country %} · {{ aircraft.country }}{% endif %}</div>
            </div>
            <div>
                {% if arc_days is not none %}
                    {% if arc_days < 0 %}
                        <span class="status-badge status-alert">⚠ ARC Expired</span>
                    {% elif arc_days < 30 %}
                        <span class="status-badge status-warn">⚠ ARC expires soon</span>
                    {% else %}
                        <span class="status-badge status-ok">✓ Airworthy</span>
                    {% endif %}
                {% else %}
                    <span class="status-badge status-warn">? ARC unknown</span>
                {% endif %}
            </div>
        </div>

        <!-- Kritiske datoer -->
        <div class="grid">
            <div class="card">
                <h3>Critical dates
                    <button class="edit-btn" onclick="document.getElementById('dates-form').classList.toggle('hidden')">Edit</button>
                </h3>
                <div class="date-item">
                    <span class="date-label">ARC valid until</span>
                    <span class="date-value {% if arc_days is not none %}{% if arc_days < 0 %}date-alert{% elif arc_days < 60 %}date-warn{% else %}date-ok{% endif %}{% else %}date-missing{% endif %}">
                        {{ claimed.arc_valid_until or 'Not registered' }}
                    </span>
                </div>
                <div class="date-item">
                    <span class="date-label">CoA valid until</span>
                    <span class="date-value {% if claimed.coa_valid_until %}date-ok{% else %}date-missing{% endif %}">
                        {{ claimed.coa_valid_until or 'Not registered' }}
                    </span>
                </div>
                <div class="date-item">
                    <span class="date-label">Insurance valid until</span>
                    <span class="date-value {% if claimed.insurance_valid_until %}date-ok{% else %}date-missing{% endif %}">
                        {{ claimed.insurance_valid_until or 'Not registered' }}
                    </span>
                </div>
                <div class="date-item">
                    <span class="date-label">Last service</span>
                    <span class="date-value {% if claimed.last_service_date %}date-ok{% else %}date-missing{% endif %}">
                        {{ claimed.last_service_date or 'Not registered' }}
                    </span>
                </div>
                <div class="date-item">
                    <span class="date-label">Next service</span>
                    <span class="date-value {% if claimed.next_service_date %}date-warn{% else %}date-missing{% endif %}">
                        {{ claimed.next_service_date or 'Not registered' }}
                    </span>
                </div>

                <!-- Edit form -->
                <div id="dates-form" class="hidden" style="margin-top:16px">
                    <form method="POST" action="/my-aircraft/{{ aircraft.tail }}/update">
                        <input type="text" name="arc_valid_until" placeholder="ARC valid until (e.g. 2026-12-01)" value="{{ claimed.arc_valid_until or '' }}">
                        <input type="text" name="coa_valid_until" placeholder="CoA valid until" value="{{ claimed.coa_valid_until or '' }}">
                        <input type="text" name="insurance_valid_until" placeholder="Insurance valid until" value="{{ claimed.insurance_valid_until or '' }}">
                        <input type="text" name="last_service_date" placeholder="Last service date" value="{{ claimed.last_service_date or '' }}">
                        <input type="text" name="next_service_date" placeholder="Next service date" value="{{ claimed.next_service_date or '' }}">
                        <button type="submit" class="save-btn">Save dates</button>
                    </form>
                </div>
            </div>

            <!-- Timer -->
            <div class="card">
                <h3>Flight hours
                    <button class="edit-btn" onclick="document.getElementById('hours-form').classList.toggle('hidden')">Edit</button>
                </h3>
                <div style="display:flex;gap:24px;margin-bottom:16px">
                    <div>
                        <div class="hours-value">{{ claimed.total_hours or '—' }}</div>
                        <div class="hours-label">Total hours</div>
                    </div>
                    <div>
                        <div class="hours-value">{{ claimed.engine_hours or '—' }}</div>
                        <div class="hours-label">Engine hours</div>
                    </div>
                </div>
                {% if claimed.notes %}
                <p style="color:#666;font-size:13px">{{ claimed.notes }}</p>
                {% endif %}

                <div id="hours-form" class="hidden" style="margin-top:16px">
                    <form method="POST" action="/my-aircraft/{{ aircraft.tail }}/update">
                        <input type="number" name="total_hours" placeholder="Total airframe hours" value="{{ claimed.total_hours or '' }}" step="0.1">
                        <input type="number" name="engine_hours" placeholder="Engine hours since overhaul" value="{{ claimed.engine_hours or '' }}" step="0.1">
                        <textarea name="notes" placeholder="Notes about the aircraft...">{{ claimed.notes or '' }}</textarea>
                        <button type="submit" class="save-btn">Save hours</button>
                    </form>
                </div>
            </div>
        </div>

        <!-- Dokumenter -->
        <div class="card" style="margin-bottom:16px">
            <h3>Documents</h3>
            <div class="doc-grid">
                <div class="doc-item" onclick="uploadDoc('arc')">
                    <span class="doc-name">Airworthiness Review Certificate (ARC)</span>
                    <span class="doc-status">{{ '✅' if claimed.arc_document else '📄' }}</span>
                </div>
                <div class="doc-item" onclick="uploadDoc('coa')">
                    <span class="doc-name">Certificate of Airworthiness (CoA)</span>
                    <span class="doc-status">{{ '✅' if claimed.coa_document else '📄' }}</span>
                </div>
                <div class="doc-item" onclick="uploadDoc('registration')">
                    <span class="doc-name">Registration Certificate</span>
                    <span class="doc-status">{{ '✅' if claimed.registration_document else '📄' }}</span>
                </div>
                <div class="doc-item" onclick="uploadDoc('noise')">
                    <span class="doc-name">Noise Certificate</span>
                    <span class="doc-status">{{ '✅' if claimed.noise_document else '📄' }}</span>
                </div>
                <div class="doc-item" onclick="uploadDoc('radio')">
                    <span class="doc-name">Radio License</span>
                    <span class="doc-status">{{ '✅' if claimed.radio_document else '📄' }}</span>
                </div>
                <div class="doc-item" onclick="uploadDoc('insurance')">
                    <span class="doc-name">Insurance Policy</span>
                    <span class="doc-status">{{ '✅' if claimed.insurance_document else '📄' }}</span>
                </div>
            </div>
            <input type="file" id="doc-upload" accept="image/*,.pdf" style="display:none" onchange="handleDocUpload(this)">
            <p style="color:#444;font-size:12px;margin-top:12px">Click a document to upload a photo or PDF</p>
        </div>

        <!-- Actions -->
        <div class="card">
            <h3>Actions</h3>
            <a href="/upload-arc/{{ aircraft.tail }}" class="action-btn">Upload & verify ARC with AI <span>→</span></a>
            <a href="/parts?q={{ aircraft.manufacturer }}" class="action-btn">Find parts for {{ aircraft.manufacturer }} {{ aircraft.model }} <span>→</span></a>
            <a href="/sell-aircraft/{{ aircraft.tail }}" class="action-btn">List this aircraft for sale <span>→</span></a>
        </div>
    </div>

    <script>
        var currentDocType = null;

        function uploadDoc(type) {
            currentDocType = type;
            document.getElementById('doc-upload').click();
        }

        function handleDocUpload(input) {
            if (!input.files[0]) return;
            var file = input.files[0];
            var reader = new FileReader();
            reader.onload = function(e) {
                var data = e.target.result.split(',')[1];
                fetch('/my-aircraft/{{ aircraft.tail }}/upload-doc', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({doc_type: currentDocType, data: data})
                }).then(r => r.json()).then(result => {
                    if (result.ok) location.reload();
                    else alert('Upload failed');
                });
            };
            reader.readAsDataURL(file);
        }
    </script>
</body>
</html>"""
