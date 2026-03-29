"""
fix_aircraft_gauges.py
1. Tilføj nye felter til AircraftListing model
2. Tilføj felter til sell-aircraft formularen
3. Byg gauge-panel ind i listing-siden
"""

with open('app.py', 'r') as f:
    content = f.read()

# ─────────────────────────────────────────────
# 1. OPDATER MODEL
# ─────────────────────────────────────────────
old_model_end = '''    ai_highlights = db.Column(db.Text)
    ai_specs = db.Column(db.Text)
    ai_description = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)'''

new_model_end = '''    ai_highlights = db.Column(db.Text)
    ai_specs = db.Column(db.Text)
    ai_description = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    hours_engine_tbo = db.Column(db.Float)
    hours_prop = db.Column(db.Float)
    hours_prop_tbo = db.Column(db.Float)
    has_autopilot = db.Column(db.Boolean, default=False)
    has_adsb = db.Column(db.Boolean, default=False)
    is_hangared = db.Column(db.Boolean, default=False)
    engine_overhauls = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)'''

if old_model_end in content:
    content = content.replace(old_model_end, new_model_end)
    print("Model OK!")
else:
    print("Model IKKE FUNDET")

# ─────────────────────────────────────────────
# 2. TILFØJ FELTER TIL LISTING SAVE
# ─────────────────────────────────────────────
old_listing_save = '''        listing = AircraftListing(
            user_id=current_user.id,
            tail=tail.upper(),
            manufacturer=request.form.get("manufacturer") or aircraft["manufacturer"],
            model=request.form.get("model") or aircraft["model"],
            year=request.form.get("year") or aircraft["year"],
            price=float(price_str),
            hours_total=float(request.form.get("hours_total") or 0) or None,
            hours_engine=float(request.form.get("hours_engine") or 0) or None,
            description=request.form.get("description", ""),
            location=request.form.get("location", ""),
            contact_name=request.form.get("contact_name") or current_user.name,
            contact_email=request.form.get("contact_email") or current_user.email,
            contact_phone=request.form.get("contact_phone", ""),
            seller_type=request.form.get("seller_type", "owner"),
            condition=request.form.get("condition", "pre-owned"),
            images=_json.dumps(images_list),
            hero_image=hero,
            ai_highlights=ai_highlights,
            ai_specs=ai_specs,
            ai_description=ai_description,
        )'''

new_listing_save = '''        def _f(name):
            try: return float(request.form.get(name) or 0) or None
            except: return None
        def _b(name): return request.form.get(name) == 'on'
        def _i(name):
            try: return int(request.form.get(name) or 0)
            except: return 0

        listing = AircraftListing(
            user_id=current_user.id,
            tail=tail.upper(),
            manufacturer=request.form.get("manufacturer") or aircraft["manufacturer"],
            model=request.form.get("model") or aircraft["model"],
            year=request.form.get("year") or aircraft["year"],
            price=float(price_str),
            hours_total=_f("hours_total"),
            hours_engine=_f("hours_engine"),
            hours_engine_tbo=_f("hours_engine_tbo"),
            hours_prop=_f("hours_prop"),
            hours_prop_tbo=_f("hours_prop_tbo"),
            engine_overhauls=_i("engine_overhauls"),
            has_autopilot=_b("has_autopilot"),
            has_adsb=_b("has_adsb"),
            is_hangared=_b("is_hangared"),
            description=request.form.get("description", ""),
            location=request.form.get("location", ""),
            contact_name=request.form.get("contact_name") or current_user.name,
            contact_email=request.form.get("contact_email") or current_user.email,
            contact_phone=request.form.get("contact_phone", ""),
            seller_type=request.form.get("seller_type", "owner"),
            condition=request.form.get("condition", "pre-owned"),
            images=_json.dumps(images_list),
            hero_image=hero,
            ai_highlights=ai_highlights,
            ai_specs=ai_specs,
            ai_description=ai_description,
        )'''

if old_listing_save in content:
    content = content.replace(old_listing_save, new_listing_save)
    print("Save OK!")
else:
    print("Save IKKE FUNDET")

# ─────────────────────────────────────────────
# 3. TILFØJ FELTER TIL FORMULAREN
# ─────────────────────────────────────────────
old_hours_card = '''            <div class="card">
                <h3>Hours</h3>
                <div class="row2">
                    <div>
                        <label>Total airframe hours</label>
                        <input type="number" name="hours_total" placeholder="e.g. 3200" min="0">
                    </div>
                    <div>
                        <label>Engine hours SMOH</label>
                        <input type="number" name="hours_engine" placeholder="e.g. 450" min="0">
                    </div>
                </div>
            </div>'''

new_hours_card = '''            <div class="card">
                <h3>Hours & technical</h3>
                <div class="row2">
                    <div>
                        <label>Total airframe hours (TT)</label>
                        <input type="number" name="hours_total" placeholder="e.g. 3200" min="0">
                    </div>
                    <div>
                        <label>Engine hours since OH (SMOH)</label>
                        <input type="number" name="hours_engine" placeholder="e.g. 450" min="0">
                    </div>
                </div>
                <div class="row2">
                    <div>
                        <label>Engine TBO (hours)</label>
                        <input type="number" name="hours_engine_tbo" placeholder="e.g. 2000" min="0">
                    </div>
                    <div>
                        <label>Engine overhauls (count)</label>
                        <input type="number" name="engine_overhauls" placeholder="e.g. 1" min="0">
                    </div>
                </div>
                <div class="row2">
                    <div>
                        <label>Propeller hours</label>
                        <input type="number" name="hours_prop" placeholder="e.g. 450" min="0">
                    </div>
                    <div>
                        <label>Propeller OH interval (hours)</label>
                        <input type="number" name="hours_prop_tbo" placeholder="e.g. 1300" min="0">
                    </div>
                </div>
                <label style="margin-top:16px;font-size:13px;color:#aaa">Equipment</label>
                <div style="display:flex;gap:20px;margin-top:8px;flex-wrap:wrap">
                    <label style="display:flex;align-items:center;gap:8px;cursor:pointer;font-size:14px;color:white;margin-top:0">
                        <input type="checkbox" name="has_autopilot" style="width:16px;height:16px;margin-bottom:0"> Autopilot
                    </label>
                    <label style="display:flex;align-items:center;gap:8px;cursor:pointer;font-size:14px;color:white;margin-top:0">
                        <input type="checkbox" name="has_adsb" style="width:16px;height:16px;margin-bottom:0"> ADS-B Out
                    </label>
                    <label style="display:flex;align-items:center;gap:8px;cursor:pointer;font-size:14px;color:white;margin-top:0">
                        <input type="checkbox" name="is_hangared" style="width:16px;height:16px;margin-bottom:0"> Hangared
                    </label>
                </div>
            </div>'''

if old_hours_card in content:
    content = content.replace(old_hours_card, new_hours_card)
    print("Form OK!")
else:
    print("Form IKKE FUNDET")

# ─────────────────────────────────────────────
# 4. BYGG GAUGE PANEL IND I LISTING-SIDEN
# ─────────────────────────────────────────────
old_listing_header = '''                {% if listing.ai_description %}
                <div class="ai-desc">{{ listing.ai_description }}</div>
                {% endif %}

                {% if highlights %}'''

new_listing_header = '''                {% if listing.ai_description %}
                <div class="ai-desc">{{ listing.ai_description }}</div>
                {% endif %}

                <!-- GAUGE PANEL -->
                {% set has_gauges = listing.hours_engine or listing.hours_total or listing.hours_prop or listing.has_autopilot or listing.has_adsb or listing.is_hangared %}
                {% if has_gauges %}
                <div class="health-panel">

                    <!-- YES/NO badges -->
                    <div class="health-badges">
                        {% if listing.has_autopilot %}<span class="hbadge yes">▲ AUTOPILOT</span>{% endif %}
                        {% if listing.has_adsb %}<span class="hbadge yes">▲ ADS-B OUT</span>{% endif %}
                        {% if listing.arc_verified %}<span class="hbadge yes">▲ ARC VERIFIED</span>{% endif %}
                        {% if listing.is_hangared %}<span class="hbadge yes">▲ HANGARED</span>{% else %}<span class="hbadge no">▼ NOT HANGARED</span>{% endif %}
                    </div>

                    <!-- GAUGES -->
                    <div class="health-gauges">
                        {% if listing.hours_engine and listing.hours_engine_tbo %}
                        {% set eng_pct = (listing.hours_engine / listing.hours_engine_tbo * 100)|int %}
                        {% set eng_color = '#4caf50' if eng_pct < 50 else ('#ffc107' if eng_pct < 75 else '#f44336') %}
                        {% set eng_x2 = (65 + 52 * [(eng_pct / 100 * 3.14159 - 3.14159)|cos])|int %}
                        {% set eng_y2 = (76 - 52 * [(eng_pct / 100 * 3.14159 - 3.14159)|sin])|int %}
                        <div class="gauge-card">
                            <div class="gauge-lbl">ENG · SMOH/TBO</div>
                            <svg width="130" height="82" viewBox="0 0 130 82">
                                <defs>
                                    <linearGradient id="eg" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" stop-color="#4caf50"/>
                                        <stop offset="55%" stop-color="#ffc107"/>
                                        <stop offset="100%" stop-color="#f44336"/>
                                    </linearGradient>
                                </defs>
                                <g stroke="#2a3a2a" stroke-width="1">
                                    <line x1="14" y1="76" x2="19" y2="71"/>
                                    <line x1="29" y1="43" x2="35" y2="46"/>
                                    <line x1="65" y1="28" x2="65" y2="35"/>
                                    <line x1="101" y1="43" x2="95" y2="46"/>
                                    <line x1="116" y1="76" x2="111" y2="71"/>
                                </g>
                                <path d="M14 76 A52 52 0 0 1 116 76" fill="none" stroke="#1a2a1a" stroke-width="12" stroke-linecap="butt"/>
                                <path d="M14 76 A52 52 0 0 1 116 76" fill="none" stroke="url(#eg)" stroke-width="12" stroke-linecap="butt" opacity="0.8"/>
                                <line x1="65" y1="76" x2="{{ eng_x2 }}" y2="{{ eng_y2 }}" stroke="#000" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
                                <line x1="65" y1="76" x2="{{ eng_x2 }}" y2="{{ eng_y2 }}" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                                <circle cx="65" cy="76" r="5" fill="#0d0d1a" stroke="{{ eng_color }}" stroke-width="1.5"/>
                                <circle cx="65" cy="76" r="2" fill="{{ eng_color }}"/>
                                <text x="65" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="{{ eng_color }}" font-family="monospace">{{ eng_pct }}%</text>
                            </svg>
                            <div class="gauge-val">{{ listing.hours_engine|int }}h SMOH</div>
                            <div class="gauge-sub">TBO {{ listing.hours_engine_tbo|int }}h · {{ (listing.hours_engine_tbo - listing.hours_engine)|int }}h LEFT</div>
                        </div>
                        {% endif %}

                        {% if listing.hours_total %}
                        {% set af_pct = [listing.hours_total / 10000 * 100, 100]|min|int %}
                        {% set af_color = '#4caf50' if af_pct < 40 else ('#ffc107' if af_pct < 70 else '#f44336') %}
                        {% set af_angle = af_pct / 100 * 180 %}
                        {% set af_x2 = (65 + 52 * (af_angle - 180)|float|radians|cos)|int %}
                        {% set af_y2 = (76 + 52 * (af_angle - 180)|float|radians|sin)|int %}
                        <div class="gauge-card">
                            <div class="gauge-lbl">AIRFRAME · TT</div>
                            <svg width="130" height="82" viewBox="0 0 130 82">
                                <defs>
                                    <linearGradient id="ag" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" stop-color="#4caf50"/>
                                        <stop offset="55%" stop-color="#ffc107"/>
                                        <stop offset="100%" stop-color="#f44336"/>
                                    </linearGradient>
                                </defs>
                                <g stroke="#2a3a2a" stroke-width="1">
                                    <line x1="14" y1="76" x2="19" y2="71"/>
                                    <line x1="29" y1="43" x2="35" y2="46"/>
                                    <line x1="65" y1="28" x2="65" y2="35"/>
                                    <line x1="101" y1="43" x2="95" y2="46"/>
                                    <line x1="116" y1="76" x2="111" y2="71"/>
                                </g>
                                <path d="M14 76 A52 52 0 0 1 116 76" fill="none" stroke="#1a2a1a" stroke-width="12" stroke-linecap="butt"/>
                                <path d="M14 76 A52 52 0 0 1 116 76" fill="none" stroke="url(#ag)" stroke-width="12" stroke-linecap="butt" opacity="0.8"/>
                                <line x1="65" y1="76" x2="{{ af_x2 }}" y2="{{ af_y2 }}" stroke="#000" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
                                <line x1="65" y1="76" x2="{{ af_x2 }}" y2="{{ af_y2 }}" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                                <circle cx="65" cy="76" r="5" fill="#0d0d1a" stroke="{{ af_color }}" stroke-width="1.5"/>
                                <circle cx="65" cy="76" r="2" fill="{{ af_color }}"/>
                                <text x="65" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="{{ af_color }}" font-family="monospace">{{ listing.hours_total|int }}h</text>
                            </svg>
                            <div class="gauge-val">{{ listing.hours_total|int }}h TT</div>
                            <div class="gauge-sub">MFR {{ listing.year }} · {% if listing.engine_overhauls %}{{ listing.engine_overhauls }}x OH{% else %}NO OVERHAUL{% endif %}</div>
                        </div>
                        {% endif %}

                        {% if listing.hours_prop and listing.hours_prop_tbo %}
                        {% set prop_pct = (listing.hours_prop / listing.hours_prop_tbo * 100)|int %}
                        {% set prop_color = '#4caf50' if prop_pct < 50 else ('#ffc107' if prop_pct < 75 else '#f44336') %}
                        <div class="gauge-card">
                            <div class="gauge-lbl">PROP · OH INTERVAL</div>
                            <svg width="130" height="82" viewBox="0 0 130 82">
                                <defs>
                                    <linearGradient id="pg" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" stop-color="#4caf50"/>
                                        <stop offset="55%" stop-color="#ffc107"/>
                                        <stop offset="100%" stop-color="#f44336"/>
                                    </linearGradient>
                                </defs>
                                <g stroke="#2a3a2a" stroke-width="1">
                                    <line x1="14" y1="76" x2="19" y2="71"/>
                                    <line x1="29" y1="43" x2="35" y2="46"/>
                                    <line x1="65" y1="28" x2="65" y2="35"/>
                                    <line x1="101" y1="43" x2="95" y2="46"/>
                                    <line x1="116" y1="76" x2="111" y2="71"/>
                                </g>
                                <path d="M14 76 A52 52 0 0 1 116 76" fill="none" stroke="#1a2a1a" stroke-width="12" stroke-linecap="butt"/>
                                <path d="M14 76 A52 52 0 0 1 116 76" fill="none" stroke="url(#pg)" stroke-width="12" stroke-linecap="butt" opacity="0.8"/>
                                {% set prop_x2 = (65 + 52 * (prop_pct / 100 * 3.14159 - 3.14159)|cos)|int %}
                                {% set prop_y2 = (76 - 52 * (prop_pct / 100 * 3.14159 - 3.14159)|sin)|int %}
                                <line x1="65" y1="76" x2="{{ prop_x2 }}" y2="{{ prop_y2 }}" stroke="#000" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
                                <line x1="65" y1="76" x2="{{ prop_x2 }}" y2="{{ prop_y2 }}" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
                                <circle cx="65" cy="76" r="5" fill="#0d0d1a" stroke="{{ prop_color }}" stroke-width="1.5"/>
                                <circle cx="65" cy="76" r="2" fill="{{ prop_color }}"/>
                                <text x="65" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="{{ prop_color }}" font-family="monospace">{{ prop_pct }}%</text>
                            </svg>
                            <div class="gauge-val">{{ listing.hours_prop|int }}h</div>
                            <div class="gauge-sub">OH INTERVAL {{ listing.hours_prop_tbo|int }}h · {{ (listing.hours_prop_tbo - listing.hours_prop)|int }}h LEFT</div>
                        </div>
                        {% endif %}
                    </div>
                </div>
                {% endif %}
                <!-- END GAUGE PANEL -->

                {% if highlights %}'''

if old_listing_header in content:
    content = content.replace(old_listing_header, new_listing_header)
    print("Gauge panel OK!")
else:
    print("Gauge panel IKKE FUNDET")

# ─────────────────────────────────────────────
# 5. TILFØJ CSS TIL LISTING SIDEN
# ─────────────────────────────────────────────
old_css = '''        /* AI description */
        .ai-desc {'''

new_css = '''        /* Health panel */
        .health-panel { background: #0d0d1a; border: 1px solid #1e2a1e; border-radius: 12px; padding: 16px; margin-bottom: 24px; font-family: monospace; }
        .health-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; }
        .hbadge { padding: 4px 12px; border-radius: 4px; font-size: 10px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
        .hbadge.yes { background: rgba(76,175,80,0.12); color: #4caf50; border: 1px solid rgba(76,175,80,0.4); }
        .hbadge.no  { background: rgba(244,67,54,0.10); color: #f44336; border: 1px solid rgba(244,67,54,0.3); }
        .health-gauges { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; }
        .gauge-card { background: #080810; border: 1px solid #1a2a1a; border-radius: 8px; padding: 12px 8px 8px; text-align: center; }
        .gauge-lbl { font-size: 9px; color: #4a8a4a; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 6px; }
        .gauge-val { font-size: 13px; font-weight: 700; color: #ccc; margin-top: 4px; }
        .gauge-sub { font-size: 9px; color: #456; margin-top: 2px; letter-spacing: 0.5px; }

        /* AI description */
        .ai-desc {'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("CSS OK!")
else:
    print("CSS IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)

print("\nFaerdig! Kør: git add app.py && git commit -m 'Aircraft gauge panel' && git push")
