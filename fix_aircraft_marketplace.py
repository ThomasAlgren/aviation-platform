"""
fix_aircraft_marketplace.py
Erstatter sell-aircraft og aircraft-for-sale med nyt AI-drevet system:
- Fri tekst + billeder → AI strukturerer alt
- Altid pris (obligatorisk)
- Flot præsentation med hero-billede
- AI-drevet naturlig sprogsøgning
"""

with open('app.py', 'r') as f:
    content = f.read()

# ─────────────────────────────────────────────
# 1. OPDATER AircraftListing MODEL
# ─────────────────────────────────────────────
old_model = '''class AircraftListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tail = db.Column(db.String(20))
    manufacturer = db.Column(db.String(200))
    model = db.Column(db.String(200))
    year = db.Column(db.String(10))
    price = db.Column(db.Float)
    hours_total = db.Column(db.Float)
    hours_engine = db.Column(db.Float)
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    contact_name = db.Column(db.String(200))
    contact_email = db.Column(db.String(200))
    images = db.Column(db.Text)
    arc_valid_until = db.Column(db.String(50))
    arc_verified = db.Column(db.Boolean, default=False)
    arc_document = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)'''

new_model = '''class AircraftListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tail = db.Column(db.String(20))
    manufacturer = db.Column(db.String(200))
    model = db.Column(db.String(200))
    year = db.Column(db.String(10))
    price = db.Column(db.Float)
    hours_total = db.Column(db.Float)
    hours_engine = db.Column(db.Float)
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    contact_name = db.Column(db.String(200))
    contact_email = db.Column(db.String(200))
    contact_phone = db.Column(db.String(50))
    images = db.Column(db.Text)
    hero_image = db.Column(db.Text)
    arc_valid_until = db.Column(db.String(50))
    arc_verified = db.Column(db.Boolean, default=False)
    arc_document = db.Column(db.Text)
    seller_type = db.Column(db.String(50))
    condition = db.Column(db.String(50))
    ai_highlights = db.Column(db.Text)
    ai_specs = db.Column(db.Text)
    ai_description = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)'''

if old_model in content:
    content = content.replace(old_model, new_model)
    print("Model OK!")
else:
    print("Model IKKE FUNDET")

# ─────────────────────────────────────────────
# 2. NY SELL-AIRCRAFT RUTE MED AI
# ─────────────────────────────────────────────
old_route = '''@app.route('/sell-aircraft/<tail>', methods=['GET', 'POST'])
@login_required
def sell_aircraft(tail):
    r = get_aircraft(tail.upper())
    if not r:
        r = get_aircraft('N' + tail.upper())
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v in ["nan", "None"] else v
    aircraft = {
        "tail": tail.upper(),
        "model": s(r["model"]) if r else "",
        "manufacturer": s(r["manufacturer"]) if r else "",
        "year": s(r["year"]).split(".")[0] if r else "",
    }
    if request.method == "POST":
        listing = AircraftListing(
            user_id=current_user.id,
            tail=tail.upper(),
            manufacturer=aircraft["manufacturer"],
            model=aircraft["model"],
            year=aircraft["year"],
            price=float(request.form.get("price", 0) or 0),
            hours_total=float(request.form.get("hours_total", 0) or 0),
            hours_engine=float(request.form.get("hours_engine", 0) or 0),
            description=request.form.get("description", ""),
            location=request.form.get("location", ""),
            contact_name=current_user.name,
            contact_email=current_user.email,
        )
        db.session.add(listing)
        db.session.commit()
        return redirect("/aircraft-for-sale")
    return render_template_string(SELL_AIRCRAFT_HTML, aircraft=aircraft)'''

new_route = '''@app.route('/sell-aircraft/ai-analyze', methods=['POST'])
@login_required
def sell_aircraft_ai_analyze():
    """AI analyserer beskrivelse og returnerer strukturerede data"""
    import anthropic as ac
    import json
    data = request.get_json()
    description = data.get('description', '')
    tail = data.get('tail', '')

    client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=[{
            "role": "user",
            "content": f"""You are an aviation marketplace expert. Extract structured data from this aircraft listing description.

Aircraft registration: {tail}

Description:
{description}

Return ONLY a JSON object with these fields:
{{
  "manufacturer": "e.g. Cessna",
  "model": "e.g. 172 Skyhawk",
  "year": "e.g. 1998",
  "hours_total": number or null,
  "hours_engine": number or null,
  "location": "e.g. Roskilde Airport (EKRK), Denmark",
  "highlights": ["3-5 key selling points as short bullet strings"],
  "specs": {{
    "engine": "e.g. Lycoming O-320",
    "avionics": "e.g. Garmin G1000",
    "seats": number or null,
    "range_nm": number or null,
    "cruise_kt": number or null,
    "useful_load_kg": number or null
  }},
  "ai_description": "A professional 2-3 sentence description of this aircraft"
}}

Be accurate and conservative. If information is not mentioned, use null."""
        }]
    )

    text = response.content[0].text
    clean = text.replace("```json", "").replace("```", "").strip()
    try:
        result = json.loads(clean)
        return json.dumps({"ok": True, "data": result})
    except:
        return json.dumps({"ok": False, "error": "Could not parse AI response"})


@app.route('/sell-aircraft/<tail>', methods=['GET', 'POST'])
@login_required
def sell_aircraft(tail):
    import json as _json
    r = get_aircraft(tail.upper())
    if not r:
        r = get_aircraft('N' + tail.upper())
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v in ["nan", "None"] else v
    aircraft = {
        "tail": tail.upper(),
        "model": s(r["model"]) if r else "",
        "manufacturer": s(r["manufacturer"]) if r else "",
        "year": s(r["year"]).split(".")[0] if r else "",
    }
    if request.method == "POST":
        price_str = request.form.get("price", "").strip()
        if not price_str:
            return render_template_string(SELL_AIRCRAFT_HTML, aircraft=aircraft, error="Price is required — we always show prices.")

        # Håndter billeder
        images_data = request.form.get("images_data", "")
        images_list = [img for img in images_data.split("|||") if img] if images_data else []
        hero = images_list[0] if images_list else None

        # AI highlights og specs fra form
        ai_highlights = request.form.get("ai_highlights", "")
        ai_specs = request.form.get("ai_specs", "")
        ai_description = request.form.get("ai_description", "")

        listing = AircraftListing(
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
        )
        db.session.add(listing)
        db.session.commit()
        return redirect(f"/aircraft-listing/{listing.id}")
    return render_template_string(SELL_AIRCRAFT_HTML, aircraft=aircraft, error=None)'''

if old_route in content:
    content = content.replace(old_route, new_route)
    print("Route OK!")
else:
    print("Route IKKE FUNDET")

# ─────────────────────────────────────────────
# 3. NY SELL_AIRCRAFT_HTML
# ─────────────────────────────────────────────
old_html = 'SELL_AIRCRAFT_HTML = """<!DOCTYPE html>'
new_sell_html = '''SELL_AIRCRAFT_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>List {{ aircraft.tail }} for Sale - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .container { max-width: 700px; margin: 40px auto; padding: 0 20px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }
        h1 { font-size: 28px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 14px; }
        .aircraft-badge { background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 12px; padding: 20px; margin-bottom: 24px; display: flex; align-items: center; gap: 20px; }
        .tail-big { font-size: 36px; font-weight: 800; color: #ff6b35; font-family: monospace; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-bottom: 16px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        label { font-size: 13px; color: #aaa; display: block; margin-bottom: 6px; margin-top: 12px; }
        label:first-child { margin-top: 0; }
        input, textarea, select { width: 100%; padding: 12px; border: 1px solid #333; border-radius: 8px; font-size: 14px; margin-bottom: 4px; background: #0d0d1a; color: white; }
        textarea { height: 140px; resize: vertical; line-height: 1.6; }
        .row2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .btn-primary { background: #ff6b35; color: white; border: none; padding: 16px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 700; margin-top: 8px; }
        .btn-primary:hover { background: #e55a25; }
        .btn-ai { background: #1a1a2e; color: #ff6b35; border: 2px solid #ff6b35; padding: 12px 20px; border-radius: 8px; font-size: 14px; cursor: pointer; font-weight: 600; width: 100%; margin-top: 8px; }
        .btn-ai:hover { background: rgba(255,107,53,0.1); }
        .ai-result { background: #0d0d1a; border: 1px solid #2a2a3e; border-radius: 8px; padding: 16px; margin-top: 12px; display: none; }
        .highlight-item { background: #1a1a2e; border-radius: 6px; padding: 8px 12px; margin-bottom: 6px; font-size: 14px; color: #aaa; }
        .price-required { color: #ff6b35; font-size: 12px; margin-top: 4px; }
        .error-box { background: rgba(244,67,54,0.15); border: 1px solid rgba(244,67,54,0.3); border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; color: #f44336; font-size: 14px; }
        .img-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 12px; }
        .img-thumb { aspect-ratio: 4/3; border-radius: 6px; object-fit: cover; width: 100%; }
        .upload-zone { border: 2px dashed #333; border-radius: 8px; padding: 32px; text-align: center; cursor: pointer; color: #666; font-size: 14px; }
        .upload-zone:hover { border-color: #ff6b35; color: #ff6b35; }
        input[type=file] { display: none; }
        .spinner { display: inline-block; width: 16px; height: 16px; border: 2px solid #ff6b35; border-top-color: transparent; border-radius: 50%; animation: spin 0.8s linear infinite; vertical-align: middle; margin-right: 8px; }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <a href="/aircraft-for-sale" class="back">← Aircraft for sale</a>
        <h1>List <span>{{ aircraft.tail }}</span> for sale</h1>
        <p class="sub">Describe your aircraft freely — AI will structure the listing automatically</p>

        {% if error %}
        <div class="error-box">{{ error }}</div>
        {% endif %}

        <div class="aircraft-badge">
            <div class="tail-big">{{ aircraft.tail }}</div>
            <div>
                <div style="font-size:16px;font-weight:600">{{ aircraft.manufacturer }} {{ aircraft.model }}</div>
                <div style="color:#666;font-size:14px">{{ aircraft.year }}</div>
            </div>
        </div>

        <form method="POST" id="listing-form">
            <input type="hidden" name="images_data" id="images_data">
            <input type="hidden" name="ai_highlights" id="ai_highlights">
            <input type="hidden" name="ai_specs" id="ai_specs">
            <input type="hidden" name="ai_description" id="ai_description">
            <input type="hidden" name="manufacturer" id="h_manufacturer" value="{{ aircraft.manufacturer }}">
            <input type="hidden" name="model" id="h_model" value="{{ aircraft.model }}">
            <input type="hidden" name="year" id="h_year" value="{{ aircraft.year }}">

            <!-- Billeder -->
            <div class="card">
                <h3>Photos — first photo becomes hero image</h3>
                <div class="upload-zone" onclick="document.getElementById('photo-input').click()">
                    📷 Upload photos (up to 10)
                    <input type="file" id="photo-input" accept="image/*" multiple onchange="handlePhotos(this)">
                </div>
                <div class="img-grid" id="img-grid"></div>
            </div>

            <!-- Beskrivelse + AI -->
            <div class="card">
                <h3>Description — write freely, AI does the rest</h3>
                <textarea name="description" id="description" placeholder="E.g.: 2003 Cessna 172SP in excellent condition. Garmin G1000 glass cockpit installed 2019. Engine overhauled 2021 with 450 hours SMOH. Annual done March 2026. Always hangared. Located at Roskilde Airport. Asking 85.000 EUR."></textarea>
                <button type="button" class="btn-ai" onclick="analyzeWithAI()">✦ Analyze with AI →</button>
                <div class="ai-result" id="ai-result">
                    <div style="font-size:12px;color:#666;margin-bottom:8px">AI EXTRACTED DATA — review and edit before publishing</div>
                    <div id="ai-highlights-display"></div>
                </div>
            </div>

            <!-- Pris — ALTID obligatorisk -->
            <div class="card">
                <h3>Price — always required</h3>
                <label>Asking price (EUR)</label>
                <input type="number" name="price" id="price" placeholder="e.g. 85000" min="1" required>
                <div class="price-required">💡 We always show prices — no "contact seller" listings</div>
                <label style="margin-top:16px">Condition</label>
                <select name="condition">
                    <option value="pre-owned">Pre-owned</option>
                    <option value="new">New</option>
                </select>
            </div>

            <!-- Sælger -->
            <div class="card">
                <h3>Seller</h3>
                <label>Seller type</label>
                <select name="seller_type">
                    <option value="owner">Private owner</option>
                    <option value="broker">Broker</option>
                    <option value="dealer">Dealer</option>
                    <option value="school">Flight school</option>
                </select>
                <label>Location</label>
                <input type="text" name="location" id="location" placeholder="e.g. Roskilde Airport (EKRK), Denmark">
                <div class="row2">
                    <div>
                        <label>Contact name</label>
                        <input type="text" name="contact_name" value="{{ current_user.name }}">
                    </div>
                    <div>
                        <label>Phone (optional)</label>
                        <input type="text" name="contact_phone" placeholder="+45 ...">
                    </div>
                </div>
                <label>Contact email</label>
                <input type="email" name="contact_email" value="{{ current_user.email }}">
            </div>

            <button type="submit" class="btn-primary">Publish listing →</button>
        </form>
    </div>

    <script>
        var uploadedImages = [];

        function handlePhotos(input) {
            var files = Array.from(input.files);
            files.forEach(function(file) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var img = new Image();
                    img.onload = function() {
                        var canvas = document.createElement('canvas');
                        var maxSize = 1600;
                        var w = img.width, h = img.height;
                        if (w > maxSize || h > maxSize) {
                            if (w > h) { h = h * maxSize / w; w = maxSize; }
                            else { w = w * maxSize / h; h = maxSize; }
                        }
                        canvas.width = w; canvas.height = h;
                        canvas.getContext('2d').drawImage(img, 0, 0, w, h);
                        var compressed = canvas.toDataURL('image/jpeg', 0.82);
                        uploadedImages.push(compressed);
                        document.getElementById('images_data').value = uploadedImages.join('|||');
                        renderThumbs();
                    };
                    img.src = e.target.result;
                };
                reader.readAsDataURL(file);
            });
        }

        function renderThumbs() {
            var grid = document.getElementById('img-grid');
            grid.innerHTML = '';
            uploadedImages.forEach(function(src, i) {
                var img = document.createElement('img');
                img.src = src;
                img.className = 'img-thumb';
                if (i === 0) img.style.outline = '3px solid #ff6b35';
                grid.appendChild(img);
            });
        }

        function analyzeWithAI() {
            var desc = document.getElementById('description').value.trim();
            if (!desc) { alert('Please write a description first'); return; }
            var btn = document.querySelector('.btn-ai');
            btn.innerHTML = '<span class="spinner"></span> AI is analyzing...';
            btn.disabled = true;

            fetch('/sell-aircraft/ai-analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({description: desc, tail: '{{ aircraft.tail }}'})
            })
            .then(r => r.json())
            .then(result => {
                btn.innerHTML = '✦ Re-analyze with AI →';
                btn.disabled = false;
                if (!result.ok) return;
                var d = result.data;

                // Udfyld skjulte felter
                if (d.manufacturer) document.getElementById('h_manufacturer').value = d.manufacturer;
                if (d.model) document.getElementById('h_model').value = d.model;
                if (d.year) document.getElementById('h_year').value = d.year;
                if (d.hours_total) document.querySelector('[name=hours_total]') && (document.querySelector('[name=hours_total]').value = d.hours_total);
                if (d.location) document.querySelector('[name=location]').value = d.location;
                document.getElementById('ai_highlights').value = JSON.stringify(d.highlights || []);
                document.getElementById('ai_specs').value = JSON.stringify(d.specs || {});
                document.getElementById('ai_description').value = d.ai_description || '';

                // Vis highlights
                var result_div = document.getElementById('ai-result');
                var highlights_div = document.getElementById('ai-highlights-display');
                result_div.style.display = 'block';
                highlights_div.innerHTML = '';
                (d.highlights || []).forEach(function(h) {
                    var div = document.createElement('div');
                    div.className = 'highlight-item';
                    div.textContent = '✓ ' + h;
                    highlights_div.appendChild(div);
                });
                if (d.ai_description) {
                    var desc_div = document.createElement('div');
                    desc_div.style.cssText = 'margin-top:12px;color:#aaa;font-size:13px;line-height:1.6;font-style:italic';
                    desc_div.textContent = d.ai_description;
                    highlights_div.appendChild(desc_div);
                }
            })
            .catch(function() {
                btn.innerHTML = '✦ Analyze with AI →';
                btn.disabled = false;
            });
        }
    </script>
</body>
</html>"""

'''

# Find og erstat SELL_AIRCRAFT_HTML
sell_end = content.find('\n@app.route(\'/aircraft-for-sale\')')
sell_start = content.find('SELL_AIRCRAFT_HTML = """<!DOCTYPE html>')

if sell_start != -1 and sell_end != -1:
    content = content[:sell_start] + new_sell_html + content[sell_end:]
    print("SELL HTML OK!")
else:
    print("SELL HTML IKKE FUNDET")

# ─────────────────────────────────────────────
# 4. NY AIRCRAFT LISTING SIDE (individuel)
# ─────────────────────────────────────────────
old_listing_route = '''@app.route('/aircraft-listing/<int:listing_id>')
def aircraft_listing(listing_id):'''

new_listing_route = '''@app.route('/aircraft-listing/<int:listing_id>')
def aircraft_listing(listing_id):
    import json as _json
    listing = AircraftListing.query.get_or_404(listing_id)
    # Opdater views
    listing.views = (listing.views or 0) + 1
    db.session.commit()
    # Parse billeder
    images = []
    if listing.images:
        try:
            images = _json.loads(listing.images)
        except:
            images = []
    highlights = []
    if listing.ai_highlights:
        try:
            highlights = _json.loads(listing.ai_highlights)
        except:
            highlights = []
    specs = {}
    if listing.ai_specs:
        try:
            specs = _json.loads(listing.ai_specs)
        except:
            specs = {}
    return render_template_string(AIRCRAFT_LISTING_HTML, listing=listing, images=images, highlights=highlights, specs=specs, current_user=current_user)

def aircraft_listing_OLD(listing_id):'''

if old_listing_route in content:
    content = content.replace(old_listing_route, new_listing_route)
    print("Listing route OK!")
else:
    print("Listing route IKKE FUNDET — søger alternativ...")
    # Prøv at finde ruten
    idx = content.find("'/aircraft-listing/<int:listing_id>'")
    if idx != -1:
        print(f"Fundet på index {idx}")
        print(content[idx-5:idx+100])

with open('app.py', 'w') as f:
    f.write(content)

print("\nFaerdig! Kør nu: python3 fix_aircraft_listing_html.py")
