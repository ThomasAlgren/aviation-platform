"""
fix_aircraft_listing_html.py
Erstatter AIRCRAFT_LISTING_DETAIL_HTML og AIRCRAFT_FOR_SALE_HTML
med flot nyt design og AI-søgning
"""

NEW_LISTING_HTML = '''
AIRCRAFT_LISTING_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>{{ listing.tail }} — {{ listing.manufacturer }} {{ listing.model }} for Sale</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0a0a14; color: white; }
        .header { padding: 16px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; position: sticky; top: 0; background: rgba(10,10,20,0.95); backdrop-filter: blur(10px); z-index: 100; }
        .logo { font-size: 20px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; padding: 8px 0; }
        
        /* Hero billede */
        .hero-img { width: 100%; height: 60vh; min-height: 380px; object-fit: cover; display: block; }
        .hero-placeholder { width: 100%; height: 40vh; background: linear-gradient(135deg, #1a1a2e, #2a1a3e); display: flex; align-items: center; justify-content: center; font-size: 80px; }
        
        /* Thumbnail strip */
        .thumb-strip { display: flex; gap: 6px; padding: 6px; background: #0a0a14; overflow-x: auto; }
        .thumb { width: 80px; height: 60px; object-fit: cover; border-radius: 4px; cursor: pointer; opacity: 0.6; flex-shrink: 0; }
        .thumb.active { opacity: 1; outline: 2px solid #ff6b35; }
        
        .container { max-width: 1000px; margin: 0 auto; padding: 32px 20px; }
        .layout { display: grid; grid-template-columns: 1fr 320px; gap: 32px; }
        @media (max-width: 768px) { .layout { grid-template-columns: 1fr; } }
        
        /* Left column */
        .main-col {}
        
        /* Titel sektion */
        .listing-header { margin-bottom: 24px; }
        .tail-reg { font-size: 14px; color: #666; font-family: monospace; letter-spacing: 1px; margin-bottom: 4px; }
        .listing-title { font-size: 32px; font-weight: 800; line-height: 1.1; margin-bottom: 8px; }
        .listing-subtitle { font-size: 16px; color: #aaa; margin-bottom: 16px; }
        .badges { display: flex; gap: 8px; flex-wrap: wrap; }
        .badge { padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-verified { background: rgba(76,175,80,0.2); color: #4caf50; border: 1px solid rgba(76,175,80,0.3); }
        .badge-condition { background: rgba(255,107,53,0.15); color: #ff6b35; border: 1px solid rgba(255,107,53,0.3); }
        .badge-seller { background: rgba(255,255,255,0.05); color: #aaa; border: 1px solid #333; }
        
        /* AI description */
        .ai-desc { background: linear-gradient(135deg, #1a1a2e, #1a2a1e); border-radius: 12px; padding: 20px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.7; font-style: italic; }
        
        /* Highlights */
        .highlights { margin-bottom: 24px; }
        .highlights h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 12px; }
        .highlight-item { display: flex; align-items: flex-start; gap: 10px; padding: 10px 0; border-bottom: 1px solid #1a1a2e; font-size: 15px; }
        .highlight-item:last-child { border-bottom: none; }
        .highlight-check { color: #4caf50; font-size: 16px; flex-shrink: 0; }
        
        /* Specs grid */
        .specs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #1a1a2e; border-radius: 12px; overflow: hidden; margin-bottom: 24px; }
        .spec-item { background: #0d0d1a; padding: 16px; }
        .spec-label { font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
        .spec-value { font-size: 18px; font-weight: 700; color: white; font-family: monospace; }
        
        /* Beskrivelse */
        .description-card { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-bottom: 24px; }
        .description-card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .description-text { color: #aaa; font-size: 14px; line-height: 1.8; white-space: pre-wrap; }
        
        /* Right column — sticky sidebar */
        .sidebar { position: sticky; top: 72px; height: fit-content; }
        .price-card { background: #1a1a2e; border-radius: 16px; padding: 28px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .price-label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
        .price-amount { font-size: 40px; font-weight: 800; color: #ff6b35; font-family: monospace; line-height: 1; }
        .price-currency { font-size: 18px; color: #666; }
        .hours-row { display: flex; gap: 16px; margin-top: 16px; padding-top: 16px; border-top: 1px solid #2a2a3e; }
        .hours-item { flex: 1; }
        .hours-label { font-size: 11px; color: #666; text-transform: uppercase; }
        .hours-value { font-size: 20px; font-weight: 700; font-family: monospace; margin-top: 2px; }
        .location-row { margin-top: 16px; padding-top: 16px; border-top: 1px solid #2a2a3e; font-size: 14px; color: #666; }
        .location-row span { color: white; }
        
        .contact-card { background: #1a1a2e; border-radius: 16px; padding: 24px; border: 1px solid #2a2a3e; }
        .contact-card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .contact-name { font-size: 16px; font-weight: 600; margin-bottom: 4px; }
        .contact-email { font-size: 14px; color: #aaa; margin-bottom: 16px; }
        .btn-contact { display: block; background: #ff6b35; color: white; text-align: center; padding: 14px; border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 15px; margin-bottom: 8px; }
        .btn-contact:hover { background: #e55a25; }
        .views-count { font-size: 12px; color: #444; text-align: center; margin-top: 12px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/aircraft-for-sale">All listings</a>
            {% if current_user.is_authenticated %}
            <a href="/my-logbook">My logbook</a>
            {% else %}
            <a href="/login">Log in</a>
            {% endif %}
        </div>
    </div>

    <!-- Hero billede -->
    {% if listing.hero_image %}
    <img class="hero-img" id="hero-img" src="{{ listing.hero_image }}" alt="{{ listing.tail }}">
    {% elif images %}
    <img class="hero-img" id="hero-img" src="{{ images[0] }}" alt="{{ listing.tail }}">
    {% else %}
    <div class="hero-placeholder">✈️</div>
    {% endif %}

    {% if images|length > 1 %}
    <div class="thumb-strip">
        {% for img in images %}
        <img class="thumb {% if loop.first %}active{% endif %}" src="{{ img }}" onclick="setHero(this, '{{ img }}')">
        {% endfor %}
    </div>
    {% endif %}

    <div class="container">
        <a href="/aircraft-for-sale" class="back">← Back to listings</a>
        
        <div class="layout">
            <!-- Venstre kolonne -->
            <div class="main-col">
                <div class="listing-header">
                    <div class="tail-reg">{{ listing.tail }}</div>
                    <h1 class="listing-title">{{ listing.manufacturer }} {{ listing.model }}</h1>
                    <div class="listing-subtitle">{{ listing.year }}{% if listing.location %} · {{ listing.location }}{% endif %}</div>
                    <div class="badges">
                        {% if listing.condition %}<span class="badge badge-condition">{{ listing.condition|title }}</span>{% endif %}
                        {% if listing.seller_type %}<span class="badge badge-seller">{{ listing.seller_type|title }}</span>{% endif %}
                        {% if listing.arc_verified %}<span class="badge badge-verified">✓ ARC Verified</span>{% endif %}
                    </div>
                </div>

                {% if listing.ai_description %}
                <div class="ai-desc">{{ listing.ai_description }}</div>
                {% endif %}

                {% if highlights %}
                <div class="highlights">
                    <h3>Highlights</h3>
                    {% for h in highlights %}
                    <div class="highlight-item">
                        <span class="highlight-check">✓</span>
                        <span>{{ h }}</span>
                    </div>
                    {% endfor %}
                </div>
                {% endif %}

                {% if specs %}
                <div class="specs-grid">
                    {% if specs.engine %}<div class="spec-item"><div class="spec-label">Engine</div><div class="spec-value" style="font-size:14px">{{ specs.engine }}</div></div>{% endif %}
                    {% if specs.avionics %}<div class="spec-item"><div class="spec-label">Avionics</div><div class="spec-value" style="font-size:14px">{{ specs.avionics }}</div></div>{% endif %}
                    {% if specs.seats %}<div class="spec-item"><div class="spec-label">Seats</div><div class="spec-value">{{ specs.seats }}</div></div>{% endif %}
                    {% if specs.range_nm %}<div class="spec-item"><div class="spec-label">Range</div><div class="spec-value">{{ specs.range_nm }} nm</div></div>{% endif %}
                    {% if specs.cruise_kt %}<div class="spec-item"><div class="spec-label">Cruise</div><div class="spec-value">{{ specs.cruise_kt }} kt</div></div>{% endif %}
                    {% if specs.useful_load_kg %}<div class="spec-item"><div class="spec-label">Useful load</div><div class="spec-value">{{ specs.useful_load_kg }} kg</div></div>{% endif %}
                </div>
                {% endif %}

                {% if listing.description %}
                <div class="description-card">
                    <h3>Full description</h3>
                    <div class="description-text">{{ listing.description }}</div>
                </div>
                {% endif %}
            </div>

            <!-- Højre kolonne — sidebar -->
            <div class="sidebar">
                <div class="price-card">
                    <div class="price-label">Asking price</div>
                    <div class="price-amount">
                        <span class="price-currency">EUR </span>{{ "{:,.0f}".format(listing.price) }}
                    </div>
                    {% if listing.hours_total or listing.hours_engine %}
                    <div class="hours-row">
                        {% if listing.hours_total %}
                        <div class="hours-item">
                            <div class="hours-label">Airframe TT</div>
                            <div class="hours-value">{{ listing.hours_total|int }}h</div>
                        </div>
                        {% endif %}
                        {% if listing.hours_engine %}
                        <div class="hours-item">
                            <div class="hours-label">Engine SMOH</div>
                            <div class="hours-value">{{ listing.hours_engine|int }}h</div>
                        </div>
                        {% endif %}
                    </div>
                    {% endif %}
                    {% if listing.location %}
                    <div class="location-row">📍 <span>{{ listing.location }}</span></div>
                    {% endif %}
                </div>

                <div class="contact-card">
                    <h3>Contact seller</h3>
                    <div class="contact-name">{{ listing.contact_name }}</div>
                    <div class="contact-email">{{ listing.contact_email }}</div>
                    {% if listing.contact_phone %}
                    <div class="contact-email">{{ listing.contact_phone }}</div>
                    {% endif %}
                    <a href="mailto:{{ listing.contact_email }}?subject=Re: {{ listing.tail }} for sale on PanPanParts" class="btn-contact">✉ Send message</a>
                    <div class="views-count">{{ listing.views or 0 }} views</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function setHero(thumb, src) {
            document.getElementById('hero-img').src = src;
            document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
            thumb.classList.add('active');
        }
    </script>
</body>
</html>"""

'''

NEW_FOR_SALE_HTML = '''
AIRCRAFT_FOR_SALE_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Aircraft for Sale — PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0a0a14; color: white; }
        .header { padding: 16px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 20px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .nav a.primary { background: #ff6b35; color: white; padding: 8px 16px; border-radius: 8px; }
        .container { max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
        
        /* Konversations-søgning */
        .search-section { margin-bottom: 40px; }
        .search-section h1 { font-size: 36px; font-weight: 800; margin-bottom: 8px; }
        .search-section h1 span { color: #ff6b35; }
        .search-section p { color: #666; margin-bottom: 24px; font-size: 15px; }
        
        .search-history { margin-bottom: 12px; }
        .search-bubble { display: inline-block; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 20px; padding: 6px 14px; font-size: 13px; color: #aaa; margin: 4px; }
        .search-bubble .remove { color: #666; cursor: pointer; margin-left: 6px; }
        .search-bubble .remove:hover { color: #ff6b35; }
        
        .search-box { display: flex; gap: 12px; }
        .search-input { flex: 1; padding: 16px 20px; border: 2px solid #2a2a3e; border-radius: 12px; font-size: 15px; background: #1a1a2e; color: white; transition: border-color 0.2s; }
        .search-input:focus { outline: none; border-color: #ff6b35; }
        .search-btn { background: #ff6b35; color: white; border: none; padding: 16px 28px; border-radius: 12px; font-size: 15px; cursor: pointer; font-weight: 700; white-space: nowrap; }
        .search-btn:hover { background: #e55a25; }
        
        .ai-suggestion { background: #1a1a2e; border-radius: 10px; padding: 12px 16px; margin-top: 12px; font-size: 13px; color: #666; display: none; }
        .ai-suggestion span { color: #ff6b35; cursor: pointer; }
        .ai-suggestion span:hover { text-decoration: underline; }
        
        /* Resultater */
        .results-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .results-count { font-size: 14px; color: #666; }
        
        .listings-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
        
        .listing-card { background: #1a1a2e; border-radius: 16px; overflow: hidden; border: 1px solid #2a2a3e; text-decoration: none; color: white; display: block; transition: transform 0.2s, border-color 0.2s; }
        .listing-card:hover { transform: translateY(-2px); border-color: #ff6b35; }
        .card-img { width: 100%; height: 180px; object-fit: cover; display: block; }
        .card-img-placeholder { width: 100%; height: 180px; background: linear-gradient(135deg, #1a1a2e, #2a1a3e); display: flex; align-items: center; justify-content: center; font-size: 48px; }
        .card-body { padding: 16px; }
        .card-tail { font-size: 12px; color: #666; font-family: monospace; letter-spacing: 1px; margin-bottom: 4px; }
        .card-title { font-size: 16px; font-weight: 700; margin-bottom: 4px; line-height: 1.3; }
        .card-meta { font-size: 13px; color: #666; margin-bottom: 12px; }
        .card-price { font-size: 22px; font-weight: 800; color: #ff6b35; font-family: monospace; }
        .card-hours { font-size: 12px; color: #666; margin-top: 4px; }
        
        .empty { text-align: center; padding: 80px 0; }
        .empty-icon { font-size: 64px; margin-bottom: 16px; }
        .empty h3 { font-size: 20px; margin-bottom: 8px; }
        .empty p { color: #666; margin-bottom: 24px; }
        .btn-list { display: inline-block; background: #ff6b35; color: white; padding: 14px 28px; border-radius: 10px; text-decoration: none; font-weight: 700; }
        
        .spinner { display: inline-block; width: 20px; height: 20px; border: 3px solid #333; border-top-color: #ff6b35; border-radius: 50%; animation: spin 0.8s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/parts">Parts for sale</a>
            {% if current_user.is_authenticated %}
            <a href="/my-listings" class="primary">+ List aircraft</a>
            {% else %}
            <a href="/register" class="primary">+ List aircraft</a>
            {% endif %}
        </div>
    </div>

    <div class="container">
        <div class="search-section">
            <h1>Find your <span>next aircraft</span></h1>
            <p>Search naturally — describe what you want, then refine step by step</p>
            
            <div class="search-history" id="search-history"></div>
            
            <div class="search-box">
                <input type="text" class="search-input" id="search-input" 
                    placeholder="e.g. 4-seat single engine with glass cockpit..."
                    onkeydown="if(event.key==='Enter') doSearch()">
                <button class="search-btn" onclick="doSearch()">Search →</button>
            </div>
            <div class="ai-suggestion" id="ai-suggestion"></div>
        </div>

        <div class="results-header">
            <div class="results-count" id="results-count">{{ listings|length }} aircraft listed</div>
            {% if listings|length > 0 %}
            <div style="font-size:13px;color:#666">Sorted by relevance</div>
            {% endif %}
        </div>

        <div class="listings-grid" id="listings-grid">
            {% if listings %}
                {% for l in listings %}
                <a class="listing-card" href="/aircraft-listing/{{ l.id }}">
                    {% if l.hero_image %}
                    <img class="card-img" src="{{ l.hero_image }}" alt="{{ l.tail }}">
                    {% elif l.images %}
                    <img class="card-img" src="{{ l.images|replace('|||', '') }}" alt="{{ l.tail }}">
                    {% else %}
                    <div class="card-img-placeholder">✈️</div>
                    {% endif %}
                    <div class="card-body">
                        <div class="card-tail">{{ l.tail }}</div>
                        <div class="card-title">{{ l.manufacturer }} {{ l.model }}</div>
                        <div class="card-meta">{{ l.year }}{% if l.location %} · {{ l.location }}{% endif %}</div>
                        <div class="card-price">EUR {{ "{:,.0f}".format(l.price) }}</div>
                        {% if l.hours_total %}
                        <div class="card-hours">{{ l.hours_total|int }}h TT{% if l.hours_engine %} · {{ l.hours_engine|int }}h SMOH{% endif %}</div>
                        {% endif %}
                    </div>
                </a>
                {% endfor %}
            {% else %}
            <div class="empty" style="grid-column:1/-1">
                <div class="empty-icon">✈️</div>
                <h3>No aircraft listed yet</h3>
                <p>Be the first to list your aircraft on PanPanParts</p>
                <a href="/sell-aircraft" class="btn-list">+ List your aircraft — free</a>
            </div>
            {% endif %}
        </div>
    </div>

    <script>
        var searchHistory = [];
        var allListings = {{ listings_json|safe }};

        function doSearch() {
            var query = document.getElementById('search-input').value.trim();
            if (!query) return;
            
            searchHistory.push(query);
            document.getElementById('search-input').value = '';
            renderHistory();
            
            document.getElementById('results-count').innerHTML = '<span class="spinner"></span> Searching...';
            document.getElementById('ai-suggestion').style.display = 'none';

            fetch('/api/aircraft-search', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({queries: searchHistory, listings: allListings})
            })
            .then(r => r.json())
            .then(result => {
                renderResults(result.matches);
                document.getElementById('results-count').textContent = result.matches.length + ' aircraft found';
                if (result.suggestion) {
                    var sug = document.getElementById('ai-suggestion');
                    sug.style.display = 'block';
                    sug.innerHTML = '💡 ' + result.suggestion;
                }
            });
        }

        function renderHistory() {
            var div = document.getElementById('search-history');
            div.innerHTML = searchHistory.map(function(q, i) {
                return '<span class="search-bubble">' + q + 
                    '<span class="remove" onclick="removeSearch(' + i + ')">×</span></span>';
            }).join('');
        }

        function removeSearch(idx) {
            searchHistory.splice(idx, 1);
            renderHistory();
            if (searchHistory.length === 0) {
                renderResults(allListings);
                document.getElementById('results-count').textContent = allListings.length + ' aircraft listed';
            } else {
                doSearchWithHistory();
            }
        }

        function doSearchWithHistory() {
            fetch('/api/aircraft-search', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({queries: searchHistory, listings: allListings})
            })
            .then(r => r.json())
            .then(result => {
                renderResults(result.matches);
                document.getElementById('results-count').textContent = result.matches.length + ' aircraft found';
            });
        }

        function renderResults(listings) {
            var grid = document.getElementById('listings-grid');
            if (listings.length === 0) {
                grid.innerHTML = '<div class="empty" style="grid-column:1/-1"><div class="empty-icon">🔍</div><h3>No matches found</h3><p>Try broadening your search or removing a filter</p></div>';
                return;
            }
            grid.innerHTML = listings.map(function(l) {
                var img = l.hero_image ? 
                    '<img class="card-img" src="' + l.hero_image + '">' :
                    '<div class="card-img-placeholder">✈️</div>';
                var hours = l.hours_total ? l.hours_total + 'h TT' + (l.hours_engine ? ' · ' + l.hours_engine + 'h SMOH' : '') : '';
                return '<a class="listing-card" href="/aircraft-listing/' + l.id + '">' +
                    img +
                    '<div class="card-body">' +
                    '<div class="card-tail">' + (l.tail || '') + '</div>' +
                    '<div class="card-title">' + (l.manufacturer || '') + ' ' + (l.model || '') + '</div>' +
                    '<div class="card-meta">' + (l.year || '') + (l.location ? ' · ' + l.location : '') + '</div>' +
                    '<div class="card-price">EUR ' + Number(l.price).toLocaleString() + '</div>' +
                    (hours ? '<div class="card-hours">' + hours + '</div>' : '') +
                    '</div></a>';
            }).join('');
        }
    </script>
</body>
</html>"""

'''

with open('app.py', 'r') as f:
    content = f.read()

# Erstat AIRCRAFT_LISTING_DETAIL_HTML med AIRCRAFT_LISTING_HTML
old_detail = 'AIRCRAFT_LISTING_DETAIL_HTML = """<!DOCTYPE html>'
detail_end = content.find('\n@app.route(\'/aircraft-for-sale\')')

if old_detail in content:
    detail_start = content.find(old_detail)
    content = content[:detail_start] + NEW_LISTING_HTML + content[detail_end:]
    print("LISTING HTML OK!")
else:
    print("LISTING HTML IKKE FUNDET")

# Erstat AIRCRAFT_FOR_SALE_HTML
old_for_sale = 'AIRCRAFT_FOR_SALE_HTML = """<!DOCTYPE html>'
for_sale_end = content.find('\n@app.route(\'/type/')

if old_for_sale in content:
    for_sale_start = content.find(old_for_sale)
    content = content[:for_sale_start] + NEW_FOR_SALE_HTML + content[for_sale_end:]
    print("FOR SALE HTML OK!")
else:
    print("FOR SALE HTML IKKE FUNDET")

# Opdater aircraft_for_sale ruten til at sende listings_json
old_forsale_route = '''@app.route('/aircraft-for-sale')
def aircraft_for_sale():
    listings = AircraftListing.query.order_by(AircraftListing.created_at.desc()).all()
    return render_template_string(AIRCRAFT_FOR_SALE_HTML, listings=listings)'''

new_forsale_route = '''@app.route('/aircraft-for-sale')
def aircraft_for_sale():
    import json as _json
    listings = AircraftListing.query.order_by(AircraftListing.created_at.desc()).all()
    # Serialiser listings til JSON for frontend search
    listings_data = []
    for l in listings:
        listings_data.append({
            'id': l.id, 'tail': l.tail, 'manufacturer': l.manufacturer,
            'model': l.model, 'year': l.year, 'price': l.price or 0,
            'hours_total': l.hours_total, 'hours_engine': l.hours_engine,
            'location': l.location, 'hero_image': l.hero_image,
            'condition': l.condition, 'seller_type': l.seller_type,
            'ai_highlights': l.ai_highlights, 'description': l.description
        })
    return render_template_string(AIRCRAFT_FOR_SALE_HTML, listings=listings,
        listings_json=_json.dumps(listings_data), current_user=current_user)

@app.route('/api/aircraft-search', methods=['POST'])
def api_aircraft_search():
    import json as _json
    import anthropic as ac
    data = request.get_json()
    queries = data.get('queries', [])
    listings = data.get('listings', [])

    if not queries or not listings:
        return _json.dumps({'matches': listings, 'suggestion': None})

    combined_query = ' AND '.join(queries)

    client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"""You are an aircraft search engine. Filter and rank these aircraft listings based on the search criteria.

Search criteria (applied cumulatively): {combined_query}

Listings:
{_json.dumps(listings, indent=2)}

Return ONLY a JSON object:
{{
  "matching_ids": [list of matching listing IDs, ranked by relevance],
  "suggestion": "A helpful follow-up suggestion for narrowing the search, or null"
}}

Be smart about interpreting criteria:
- "glass cockpit" = Garmin G1000, Avidyne, or similar mentioned in description/specs
- "4-seat" = 4 seats
- Price ranges: "under 200k" = price < 200000
- Motor hours: "500h to TBO" = hours_engine < 500 (approximately)
- If no listings match, suggest broadening the search"""
        }]
    )
    
    text = response.content[0].text.replace("```json", "").replace("```", "").strip()
    try:
        result = _json.loads(text)
        matching_ids = result.get('matching_ids', [])
        id_to_listing = {l['id']: l for l in listings}
        matches = [id_to_listing[i] for i in matching_ids if i in id_to_listing]
        return _json.dumps({'matches': matches, 'suggestion': result.get('suggestion')})
    except:
        return _json.dumps({'matches': listings, 'suggestion': None})'''

if old_forsale_route in content:
    content = content.replace(old_forsale_route, new_forsale_route)
    print("For sale route OK!")
else:
    print("For sale route IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)

print("\nFaerdig!")
