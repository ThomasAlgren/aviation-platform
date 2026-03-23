import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
load_dotenv()

from flask import Flask, render_template_string, request, redirect
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/thomasalgrenwest/aviation-platform/instance/panpanparts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(100))
    serial_number = db.Column(db.String(100))
    issued_by = db.Column(db.String(200))
    issue_date = db.Column(db.String(50))
    part_condition = db.Column(db.String(50))
    condition_notes = db.Column(db.Text)
    ai_recommendation = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    contact_name = db.Column(db.String(200))
    contact_email = db.Column(db.String(200))
    contact_phone = db.Column(db.String(50))
    location = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    part_image = db.Column(db.Text)
    doc_image = db.Column(db.Text)

with app.app_context():
    db.create_all()
print("Loader FAA data...")
df = pd.read_pickle("faa_master.pkl")
ref = pd.read_pickle("faa_ref.pkl")
dk = pd.read_pickle("denmark.pkl")
ln = pd.read_pickle("ln_register.pkl")
vh = pd.read_pickle("vh_register.pkl")
hb = pd.read_csv("hb_register.csv", sep=';', encoding='utf-16', skipinitialspace=True, low_memory=False)
print("Klar!")
LISTING_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>List Your Part - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #f0f4f8; color: #1a1a2e; }
        .header { background: #1a1a2e; color: white; padding: 20px 40px; }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header span { color: #4a9eff; }
        .container { max-width: 600px; margin: 40px auto; padding: 0 20px; }
        .ai-card { background: #e8f5e9; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
        .ai-card h3 { color: #2d7a3a; margin-bottom: 12px; }
        .field { display: flex; justify-content: space-between; padding: 6px 0; font-size: 14px; border-bottom: 1px solid #c8e6c9; }
        .field:last-child { border-bottom: none; }
        .card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
        .card h3 { margin-bottom: 16px; font-size: 16px; }
        input, textarea { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 8px; font-size: 15px; margin-bottom: 12px; }
        textarea { height: 100px; resize: vertical; }
        button { background: #1a1a2e; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 15px; cursor: pointer; width: 100%; }
        .warn { background: #fff3e0; border-radius: 8px; padding: 12px; margin-bottom: 16px; font-size: 14px; color: #e65100; }
    </style>
</head>
<body>
    <div class="header"><h1>PanPan<span>Parts</span></h1></div>
    <div class="container">
        <div class="ai-card">
            <h3>AI Analysis Result</h3>
            <div class="field"><span>Part number</span><span>{{ part.part_number or 'Not found' }}</span></div>
            <div class="field"><span>Serial number</span><span>{{ part.serial_number or 'Not found' }}</span></div>
            <div class="field"><span>Issued by</span><span>{{ part.issued_by or 'Not found' }}</span></div>
            <div class="field"><span>Condition</span><span>{{ part.part_condition }}</span></div>
            <div class="field"><span>AI recommendation</span><span>{{ part.ai_recommendation }}</span></div>
            <div class="field"><span>Notes</span><span>{{ part.condition_notes }}</span></div>
        </div>
        {% if part.ai_recommendation == 'Not recommended' %}
        <div class="warn">AI has flagged this part. You can still list it but buyers will see this warning.</div>
        {% endif %}
        <div class="card">
            <h3>Add your listing details</h3>
            <form method="POST">
                <input name="price" type="number" placeholder="Price (EUR)" required>
                <<textarea name="description" placeholder="Description — condition, history, why are you selling?">{{ part.condition_notes or '' }}</textarea>
                <input name="location" placeholder="Location (e.g. Roskilde, Denmark)">
               
                <button type="submit">Publish listing</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

PARTS_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Parts for Sale - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #f0f4f8; color: #1a1a2e; }
        .header { background: #1a1a2e; color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header span { color: #ff6b35; }
        .header a { color: #4a9eff; font-size: 14px; text-decoration: none; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .part-card { background: white; border-radius: 12px; padding: 20px 24px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; justify-content: space-between; align-items: center; }
        .part-info h3 { font-size: 16px; margin-bottom: 4px; }
        .part-info p { color: #666; font-size: 14px; }
        .price { font-size: 22px; font-weight: 700; color: #1a1a2e; }
        .location { color: #999; font-size: 13px; margin-top: 4px; }
        .badge { background: #e8f5e9; color: #2d7a3a; padding: 4px 10px; border-radius: 20px; font-size: 12px; display: inline-block; margin-top: 6px; }
        .badge-warn { background: #fff3e0; color: #e65100; }
        .empty { text-align: center; color: #999; padding: 60px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>PanPan<span>Parts</span></h1>
        <a href="/upload">+ List a part</a>
    </div>
    <div class="container">
        {% if parts %}
            {% for p in parts %}
            <div class="part-card">
                <div class="part-info">
                    <h3>{{ p.part_number or 'Unknown part' }}</h3>
                    <p>{{ p.description[:80] if p.description else 'No description' }}</p>
                    <p>{{ p.contact_name }} &bull; {{ p.location }}</p>
                    <span class="badge {% if p.ai_recommendation != 'Approved for listing' %}badge-warn{% endif %}">
                        {{ p.ai_recommendation }}
                    </span>
                </div>
                <div style="text-align:right">
                    <div class="price">€{{ p.price }}</div>
                    <div class="location">{{ p.part_condition }}</div>
                </div>
            </div>
            {% endfor %}
        {% else %}
            <div class="empty">
                <p>No parts listed yet</p>
                <a href="/upload" style="color:#4a9eff">Be the first to list a part</a>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""
SEARCH_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>PanPanParts — Aviation Parts & Aircraft Registry</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; min-height: 100vh; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav { display: flex; gap: 24px; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; }
        .nav a:hover { color: white; }
        .nav a.primary { background: #ff6b35; color: white; padding: 8px 18px; border-radius: 8px; }
        .hero { text-align: center; padding: 80px 20px 60px; }
        .hero h1 { font-size: 52px; font-weight: 700; line-height: 1.15; margin-bottom: 16px; }
        .hero h1 span { color: #ff6b35; }
        .hero p { font-size: 18px; color: #aaa; margin-bottom: 48px; max-width: 560px; margin-left: auto; margin-right: auto; }
        .search-box { background: white; border-radius: 16px; padding: 8px; display: flex; max-width: 640px; margin: 0 auto 48px; box-shadow: 0 20px 60px rgba(255,107,53,0.2); }
        .search-box input { flex: 1; border: none; outline: none; padding: 14px 20px; font-size: 16px; color: #1a1a2e; background: transparent; }
        .search-box button { background: #ff6b35; color: white; border: none; padding: 14px 28px; border-radius: 10px; font-size: 15px; cursor: pointer; white-space: nowrap; }
        .search-box button:hover { background: #e55a25; }
        .tabs { display: flex; gap: 8px; justify-content: center; margin-bottom: 48px; }
        .tab { padding: 8px 20px; border-radius: 20px; font-size: 14px; cursor: pointer; border: 1px solid #333; color: #aaa; background: transparent; }
        .tab.active { background: #ff6b35; color: white; border-color: #ff6b35; }
        .stats { display: flex; gap: 40px; justify-content: center; margin-bottom: 80px; }
        .stat { text-align: center; }
        .stat-value { font-size: 32px; font-weight: 700; color: #ff6b35; }
        .stat-label { font-size: 13px; color: #666; margin-top: 4px; }
        .features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 900px; margin: 0 auto 80px; padding: 0 20px; }
        .feature { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; }
        .feature-icon { font-size: 28px; margin-bottom: 12px; }
        .feature h3 { font-size: 15px; margin-bottom: 8px; }
        .feature p { font-size: 13px; color: #666; line-height: 1.6; }
        .results { max-width: 800px; margin: 0 auto 40px; padding: 0 20px; }
        .result-count { color: #666; font-size: 14px; margin-bottom: 16px; }
        .aircraft-card { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 10px; border: 1px solid #2a2a3e; display: flex; justify-content: space-between; align-items: center; text-decoration: none; color: inherit; transition: border-color 0.15s; }
        .aircraft-card:hover { border-color: #ff6b35; }
        .aircraft-info h3 { font-size: 16px; margin-bottom: 4px; }
        .aircraft-info p { color: #666; font-size: 14px; }
        .tail { font-size: 22px; font-weight: 700; color: #ff6b35; font-family: monospace; }
        .status-v { background: rgba(45,122,58,0.2); color: #4caf50; padding: 4px 10px; border-radius: 20px; font-size: 12px; margin-top: 6px; display: inline-block; border: 1px solid rgba(76,175,80,0.3); }
        select { background: #1a1a2e; color: white; border: 1px solid #333; padding: 10px 14px; border-radius: 8px; font-size: 14px; }
    </style>
</head>
<body>
<div class="header">
        <div class="logo">PanPan<span>Parts</span></div>
        <div class="nav">
            <a href="/parts">Parts for sale</a>
            <a href="/upload" class="primary">+ List a part</a>
        </div>
    </div>
    {% if not results %}
    <div class="hero">
        <h1>Find <span>any aviation part</span><br>anywhere in the world</h1>
        <p>The verified marketplace for aircraft parts — with AI-powered documentation checking</p>
        <form method="GET">
            <div class="search-box">
                <input name="tail" placeholder="Search by tail number or aircraft type..." value="{{ tail }}">
                <button type="submit">Search</button>
            </div>
        </form>
        <div class="stats">
            <div class="stat"><div class="stat-value">310K+</div><div class="stat-label">Aircraft registered</div></div>
            <div class="stat"><div class="stat-value">7K+</div><div class="stat-label">Danish aircraft</div></div>
            <div class="stat"><div class="stat-value">AI</div><div class="stat-label">Verified parts</div></div>
        </div>
        <div class="features">
            <div class="feature"><div class="feature-icon">📷</div><h3>Photo to listing in 2 minutes</h3><p>Take photos, AI extracts all data automatically. Just add a price.</p></div>
            <div class="feature"><div class="feature-icon">✓</div><h3>AI verified documentation</h3><p>Every part checked for valid airworthiness documentation.</p></div>
            <div class="feature"><div class="feature-icon">🌍</div><h3>European focus</h3><p>Search across USA, Denmark and Europe.</p></div>
        </div>
    </div>
    {% endif %}
    {% if results is not none %}
    <div class="results">
        <p class="result-count">{{ result_count }} aircraft found</p>
        {% for r in results %}
        <a class="aircraft-card" href="/aircraft/{{ r.tail }}">
            <div class="aircraft-info">
                <h3>{{ r.manufacturer }} {{ r.model }}</h3>
                <p>{{ r.name }} &bull; {{ r.city }}, {{ r.state }}</p>
                <p style="color:#555; font-size:13px; margin-top:4px;">{{ r.year }}</p>
            </div>
            <div style="text-align:right">
                <div class="tail">{% if r.tail.startswith("OY") or r.tail.startswith("LN") or r.tail.startswith("HB") or r.tail.startswith("VH") %}{{ r.tail }}{% else %}N{{ r.tail }}{% endif %}</div>
                <div class="status-v">Active</div>
            </div>
        </a>
        {% endfor %}
    </div>
    {% endif %}
</body>
</html>
"""

OY_DETAIL_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ aircraft.tail }} - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #f0f4f8; color: #1a1a2e; }
        .header { background: #1a1a2e; color: white; padding: 20px 40px; display: flex; align-items: center; justify-content: space-between; }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header span { color: #ff6b35; }
        .header a { color: #aaa; font-size: 14px; text-decoration: none; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .hero { background: #1a1a2e; border-radius: 16px; padding: 40px; margin-bottom: 20px; color: white; position: relative; overflow: hidden; }
        .hero-bg { position: absolute; top: 0; right: 0; width: 300px; height: 100%; background: linear-gradient(135deg, transparent, rgba(255,107,53,0.1)); }
        .tail-number { font-size: 56px; font-weight: 700; color: #ff6b35; font-family: monospace; letter-spacing: -2px; }
        .model-name { font-size: 22px; font-weight: 500; margin: 8px 0 4px; color: white; }
        .manufacturer { font-size: 15px; color: #aaa; margin-bottom: 16px; }
        .badges { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
        .badge { padding: 6px 14px; border-radius: 20px; font-size: 13px; }
        .badge-green { background: rgba(45,122,58,0.3); color: #4caf50; border: 1px solid rgba(76,175,80,0.3); }
        .badge-blue { background: rgba(74,158,255,0.2); color: #4a9eff; border: 1px solid rgba(74,158,255,0.3); }
        .badge-orange { background: rgba(255,107,53,0.2); color: #ff6b35; border: 1px solid rgba(255,107,53,0.3); }
        .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px; }
        .stat-card { background: white; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
        .stat-value { font-size: 28px; font-weight: 700; color: #1a1a2e; }
        .stat-label { font-size: 12px; color: #999; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
        .card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
        .card h3 { font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; color: #999; margin-bottom: 16px; }
        .field { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 14px; }
        .field:last-child { border-bottom: none; }
        .field-label { color: #666; }
        .field-value { font-weight: 500; text-align: right; max-width: 60%; }
        .timeline { position: relative; padding-left: 24px; }
        .timeline-item { position: relative; padding-bottom: 20px; }
        .timeline-item:before { content: ''; position: absolute; left: -20px; top: 6px; width: 8px; height: 8px; background: #ff6b35; border-radius: 50%; }
        .timeline-item:after { content: ''; position: absolute; left: -17px; top: 14px; width: 2px; height: calc(100% - 8px); background: #f0f0f0; }
        .timeline-item:last-child:after { display: none; }
        .timeline-reg { font-weight: 600; font-size: 15px; color: #1a1a2e; font-family: monospace; }
        .timeline-date { font-size: 12px; color: #999; margin-top: 2px; }
        .sell-btn { background: #ff6b35; color: white; border: none; padding: 16px 32px; border-radius: 10px; font-size: 16px; cursor: pointer; width: 100%; margin-top: 8px; font-weight: 500; }
        .sell-btn:hover { background: #e55a25; }
    </style>
</head>
<body>
    <div class="header">
        <h1>PanPan<span>Parts</span></h1>
        <a href="/">← Search</a>
    </div>
    <div class="container">
        <div class="hero">
            <div class="hero-bg"></div>
            <div class="tail-number">{{ aircraft.tail }}</div>
            <div class="model-name">{{ aircraft.model }}</div>
            <div class="manufacturer">{{ aircraft.manufacturer }}{% if aircraft.build_place %} · {{ aircraft.build_place }}{% endif %}</div>
            <div class="badges">
                <span class="badge badge-green">✓ Active — {{ aircraft.country }}</span>
                <span class="badge badge-blue">{{ aircraft.year }}</span>
                {% if aircraft.previous %}
                <span class="badge badge-orange">{{ aircraft.previous.split()|length }} previous identities</span>
                {% endif %}
            </div>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">{{ aircraft.year }}</div>
                <div class="stat-label">Year built</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ aircraft.serial }}</div>
                <div class="stat-label">Serial number</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ aircraft.country[:2].upper() }}</div>
                <div class="stat-label">Current country</div>
            </div>
        </div>

        <div class="card">
            <h3>Aircraft details</h3>
            <div class="field"><span class="field-label">Registration</span><span class="field-value">{{ aircraft.tail }}</span></div>
            <div class="field"><span class="field-label">Type</span><span class="field-value">{{ aircraft.model }}</span></div>
            <div class="field"><span class="field-label">Manufacturer</span><span class="field-value">{{ aircraft.manufacturer }}</span></div>
            <div class="field"><span class="field-label">Built in</span><span class="field-value">{{ aircraft.build_place }}</span></div>
            <div class="field"><span class="field-label">Serial number</span><span class="field-value">{{ aircraft.serial }}</span></div>
            <div class="field"><span class="field-label">Registered</span><span class="field-value">{{ aircraft.reg_date }}</span></div>
        </div>

        {% if aircraft.previous %}
        <div class="card">
            <h3>Life history</h3>
            <div class="timeline">
                {% for reg in aircraft.previous.split() %}
                <div class="timeline-item">
                    <div class="timeline-reg">{{ reg }}</div>
                    <div class="timeline-date">Previous registration</div>
                </div>
                {% endfor %}
                <div class="timeline-item">
                    <div class="timeline-reg" style="color:#ff6b35">{{ aircraft.tail }}</div>
                    <div class="timeline-date">Current — registered {{ aircraft.reg_date }}</div>
                </div>
            </div>
        </div>
        {% endif %}

        <div class="card">
            <h3>Own this aircraft?</h3>
            <p style="color:#666; font-size:14px; margin-bottom:16px">Claim your aircraft profile to add photos, flight hours, avionics and maintenance history. List it for sale with one click.</p>
            <button class="sell-btn">Claim {{ aircraft.tail }} — it's free</button>
        </div>

    </div>
</body>
</html>
"""
DETAIL_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>N{{ aircraft.tail }} - PanPanParts</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #f0f4f8; color: #1a1a2e; }
        .header { background: #1a1a2e; color: white; padding: 20px 40px; display: flex; align-items: center; gap: 16px; }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header span { color: #4a9eff; }
        .header a { color: #aaa; font-size: 14px; text-decoration: none; margin-left: 20px; }
        .header a:hover { color: white; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .hero { background: white; border-radius: 12px; padding: 32px; margin-bottom: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
        .tail-number { font-size: 48px; font-weight: 700; color: #4a9eff; font-family: monospace; }
        .model-name { font-size: 24px; font-weight: 600; margin: 8px 0 4px; }
        .status-v { background: #e6f4ea; color: #2d7a3a; padding: 6px 14px; border-radius: 20px; font-size: 13px; display: inline-block; margin-top: 8px; }
        .card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
        .card h3 { font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; color: #999; margin-bottom: 16px; }
        .field { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
        .field:last-child { border-bottom: none; }
        .field-label { color: #666; font-size: 14px; }
        .field-value { font-weight: 500; font-size: 14px; text-align: right; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Sky<span>Reg</span></h1>
        <a href="/">← Back to search</a>
    </div>
    <div class="container">
        <div class="hero">
            <div class="tail-number">{% if aircraft.tail.startswith("OY") %}{{ aircraft.tail }}{% else %}N{{ aircraft.tail }}{% endif %}</div>
            <div class="model-name">{{ aircraft.manufacturer }} {{ aircraft.model }}</div>
            <div class="status-v">✓ Active Registration</div>
        </div>
        <div class="card">
            <h3>Registration</h3>
            <div class="field"><span class="field-label">Owner</span><span class="field-value">{{ aircraft.name }}</span></div>
            <div class="field"><span class="field-label">Street</span><span class="field-value">{{ aircraft.street }}</span></div>
            <div class="field"><span class="field-label">City</span><span class="field-value">{{ aircraft.city }}, {{ aircraft.state }} {{ aircraft.zip }}</span></div>
            <div class="field"><span class="field-label">Country</span><span class="field-value">{{ aircraft.country }}</span></div>
        </div>
        <div class="card">
            <h3>Aircraft Details</h3>
            <div class="field"><span class="field-label">Year manufactured</span><span class="field-value">{{ aircraft.year }}</span></div>
            <div class="field"><span class="field-label">Serial number</span><span class="field-value">{{ aircraft.serial }}</span></div>
            <div class="field"><span class="field-label">Engine type</span><span class="field-value">{{ aircraft.engine }}</span></div>
            <div class="field"><span class="field-label">Cert issued</span><span class="field-value">{{ aircraft.cert_date }}</span></div>
            <div class="field"><span class="field-label">Last action</span><span class="field-value">{{ aircraft.last_action }}</span></div>
            <div class="field"><span class="field-label">Expiration</span><span class="field-value">{{ aircraft.expiration }}</span></div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    tail = request.args.get("tail", "")
    model = request.args.get("model", "")
    state = request.args.get("state", "")
    year_from = request.args.get("year_from", "")
    year_to = request.args.get("year_to", "")
    states = sorted(df["STATE"].dropna().unique().tolist())
    results = None
    result_count = 0
    if tail and tail.upper().startswith("OY-"):
        pass
    if tail and tail.upper().startswith("LN-"):
        ln_result = ln[ln["registration"] == tail.upper()]
        if len(ln_result) > 0:
            r = ln_result.iloc[0]
            results = [{
                "tail": r["registration"],
                "model": str(r["type"]).strip(),
                "manufacturer": str(r["manufacturer"]).strip(),
                "name": "",
                "city": "",
                "state": "Norway",
                "year": str(r["year_built"]).strip(),
            }]
            result_count = 1
            return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
                year_from=year_from, year_to=year_to, states=states,
                results=results, result_count=result_count)

    if tail and tail.upper().startswith("HB-"):
        pass
    if tail and tail.upper().startswith("VH-"):
        vh_search = tail.upper().replace("VH-", "")
        vh_result = vh[vh["Mark"].str.strip() == vh_search]
        if len(vh_result) > 0:
            r = vh_result.iloc[0]
            results = [{
                "tail": "VH-" + str(r["Mark"]).strip(),
                "model": str(r["Model"]).strip(),
                "manufacturer": str(r["Manu"]).strip(),
                "name": str(r.get("regholdname", "")).strip(),
                "city": str(r.get("regholdSuburb", "")).strip(),
                "state": "Australia",
                "year": str(r.get("Yearmanu", "")).strip(),
            }]
            result_count = 1
            return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
                year_from=year_from, year_to=year_to, states=states,
                results=results, result_count=result_count)
        hb_result = hb[hb[" Registration"].str.strip() == tail.upper()]
        if len(hb_result) > 0:
            r = hb_result.iloc[0]
            results = [{
                "tail": r[" Registration"].strip(),
                "model": str(r[" Aicraft Model"]).strip(),
                "manufacturer": str(r[" Manufacturer"]).strip(),
                "name": "",
                "city": "",
                "state": "Switzerland",
                "year": str(r[" Year of Manufacture"]).strip(),
            }]
            result_count = 1
            return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
                year_from=year_from, year_to=year_to, states=states,
                results=results, result_count=result_count)
        oy_result = dk[dk["registration"] == tail.upper()]
        if len(oy_result) > 0:
            r = oy_result.iloc[0]
            results = [{
                "tail": r["registration"],
                "model": r["type"],
                "manufacturer": "",
                "name": "",
                "city": "",
                "state": "Denmark",
                "year": str(r.get("year_built", r.get("year_mfr", ""))),
            }]
            result_count = 1
            return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
                year_from=year_from, year_to=year_to, states=states,
                results=results, result_count=result_count)
    if any([tail, model, state, year_from, year_to]):
        filtered = df[df["STATUS CODE"].str.strip() == "V"].copy()
        ref2 = ref[["ï»¿CODE","MFR","MODEL"]].copy()
        ref2.columns = ["MFR MDL CODE","MANUFACTURER","MODEL_NAME"]
        ref2["MFR MDL CODE"] = ref2["MFR MDL CODE"].astype(str).str.strip()
        filtered["MFR MDL CODE"] = filtered["MFR MDL CODE"].astype(str).str.strip()
        filtered = filtered.merge(ref2, on="MFR MDL CODE", how="left")
        if tail:
            filtered = filtered[filtered["ï»¿N-NUMBER"].astype(str).str.strip() == tail.upper().replace("N","")]
        if state:
            filtered = filtered[filtered["STATE"] == state]
        if year_from:
            filtered = filtered[pd.to_numeric(filtered["YEAR MFR"], errors="coerce") >= int(year_from)]
        if year_to:
            filtered = filtered[pd.to_numeric(filtered["YEAR MFR"], errors="coerce") <= int(year_to)]
        if model:
            filtered = filtered[filtered["MODEL_NAME"].astype(str).str.contains(model.upper(), na=False)]
        result_count = len(filtered)
        filtered = filtered.head(50)
        results = []
        for _, row in filtered.iterrows():
            results.append({
                "tail": str(row["ï»¿N-NUMBER"]).strip(),
                "model": str(row.get("MODEL_NAME", "")).strip(),
                "manufacturer": str(row.get("MANUFACTURER", "")).strip(),
                "name": str(row["NAME"]).strip(),
                "city": str(row["CITY"]).strip(),
                "state": str(row["STATE"]).strip(),
                "year": str(row["YEAR MFR"]).strip(),
            })
    return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
        year_from=year_from, year_to=year_to, states=states,
        results=results, result_count=result_count)

@app.route("/aircraft/<tail>")
def aircraft_detail(tail):
    ref2 = ref[["ï»¿CODE","MFR","MODEL"]].copy()
    ref2.columns = ["MFR MDL CODE","MANUFACTURER","MODEL_NAME"]
    ref2["MFR MDL CODE"] = ref2["MFR MDL CODE"].astype(str).str.strip()
    merged = df.copy()
    merged["MFR MDL CODE"] = merged["MFR MDL CODE"].astype(str).str.strip()
    merged = merged.merge(ref2, on="MFR MDL CODE", how="left")
    row = merged[merged["ï»¿N-NUMBER"].astype(str).str.strip() == tail.upper()]
    if len(row) == 0:
        return "Aircraft not found", 404
    r = row.iloc[0]
    aircraft = {
        "tail": str(r["ï»¿N-NUMBER"]).strip(),
        "model": str(r.get("MODEL_NAME", "")).strip(),
        "manufacturer": str(r.get("MANUFACTURER", "")).strip(),
        "name": str(r["NAME"]).strip(),
        "street": str(r["STREET"]).strip(),
        "city": str(r["CITY"]).strip(),
        "state": str(r["STATE"]).strip(),
        "zip": str(r["ZIP CODE"]).strip(),
        "country": str(r["COUNTRY"]).strip(),
        "year": str(r["YEAR MFR"]).strip(),
        "serial": str(r["SERIAL NUMBER"]).strip(),
        "engine": str(r["ENG MFR MDL"]).strip(),
        "cert_date": str(r["CERT ISSUE DATE"]).strip(),
        "last_action": str(r["LAST ACTION DATE"]).strip(),
        "expiration": str(r["EXPIRATION DATE"]).strip(),
    }
    return render_template_string(DETAIL_HTML, aircraft=aircraft)

@app.route("/upload")
def upload():
    return open("upload.html").read()

@app.route("/analyze", methods=["POST"])
@app.route("/analyze", methods=["POST"])
def analyze():
    import anthropic
    import json

    data = request.get_json()
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data["part_image"]}},
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data["doc_image"]}},
            {"type": "text", "text": """You are an aviation parts inspector. Analyze these two images:
1. First image: the aircraft part
2. Second image: the airworthiness document (Form 1 or EASA Form 1 or FAA 8130-3)

Respond ONLY with a JSON object:
{
  "part_number": "extracted part number or null",
  "serial_number": "extracted serial number or null",
  "issued_by": "organization or null",
  "issue_date": "date or null",
  "part_condition": "Good / Fair / Poor",
  "condition_notes": "brief note",
  "document_readable": true or false,
  "ai_recommendation": "Approved for listing / Needs inspection / Not recommended",
  "recommendation_reason": "brief reason"
}"""}
        ]
    }]

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=messages
    )

    text = response.content[0].text
    clean = text.replace("```json", "").replace("```", "").strip()
    result = json.loads(clean)

    part = Part(
        part_number=result.get("part_number"),
        serial_number=result.get("serial_number"),
        issued_by=result.get("issued_by"),
        issue_date=result.get("issue_date"),
        part_condition=result.get("part_condition"),
        condition_notes=result.get("condition_notes"),
        ai_recommendation=result.get("ai_recommendation"),
        part_image=data["part_image"][:500],
        doc_image=data["doc_image"][:500]
    )

    with app.app_context():
        db.session.add(part)
        db.session.commit()
        part_id = part.id

    result["part_id"] = part_id
    return json.dumps(result)
    import anthropic
    import base64
    import json
    
    data = request.get_json()
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data["part_image"]}},
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data["doc_image"]}},
            {"type": "text", "text": """You are an aviation parts inspector. Analyze these two images:
1. First image: the aircraft part
2. Second image: the airworthiness document

Respond ONLY with a JSON object:
{
  "part_number": "extracted part number or null",
  "serial_number": "extracted serial number or null",
  "issued_by": "organization or null",
  "issue_date": "date or null",
  "part_condition": "Good / Fair / Poor",
  "condition_notes": "brief note",
  "document_readable": true or false,
  "ai_recommendation": "Approved for listing / Needs inspection / Not recommended",
  "recommendation_reason": "brief reason"
}"""}
        ]
    }]
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=messages
    )
    
    text = response.content[0].text
    clean = text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)

@app.route("/listing/<int:part_id>", methods=["GET", "POST"])
def listing(part_id):
    with app.app_context():
        part = Part.query.get_or_404(part_id)
        if request.method == "POST":
            part.price = float(request.form.get("price", 0))
            part.description = request.form.get("description", "")
            part.contact_name = request.form.get("contact_name", "")
            part.contact_email = request.form.get("contact_email", "")
            part.contact_phone = request.form.get("contact_phone", "")
            part.location = request.form.get("location", "")
            db.session.commit()
            return redirect("/parts")
        return render_template_string(LISTING_HTML, part=part)

@app.route("/parts")
def parts():
    query = request.args.get("q", "")
    with app.app_context():
        if query:
            all_parts = Part.query.filter(
                Part.price != None,
                db.or_(
                    Part.part_number.ilike(f"%{query}%"),
                    Part.description.ilike(f"%{query}%"),
                    Part.condition_notes.ilike(f"%{query}%")
                )
            ).order_by(Part.created_at.desc()).all()
        else:
            all_parts = Part.query.filter(Part.price != None).order_by(Part.created_at.desc()).all()
        return render_template_string(PARTS_HTML, parts=all_parts, query=query)

@app.route("/aircraft/OY-<reg>")
def oy_detail(reg):
    registration = f"OY-{reg}"
    
    oy_row = dk[dk["registration"] == registration]
    da_row = dk[dk["registration"] == registration]
    
    if len(oy_row) == 0:
        return f"Aircraft {registration} not found", 404
    
    r = oy_row.iloc[0]
    
    def s(val):
        v = str(val).strip()
        return "" if v == "nan" else v

    aircraft = {
        "tail": registration,
        "model": s(r.get("type", "")),
        "manufacturer": s(r.get("manufacturer", "")),
        "build_place": s(r.get("build_place", "")),
        "serial": s(r.get("serial", "")),
        "year": s(r.get("year_built", "")),
        "reg_date": s(r.get("reg_date", "")),
        "previous": s(r.get("previous", "")),
        "country": "DK",
        "name": "",
        "street": "",
        "city": "",
        "state": "Denmark",
        "zip": "",
        "engine": "",
        "cert_date": "",
        "last_action": s(r.get("year_reg", "")),
        "expiration": "",
    }
    return render_template_string(OY_DETAIL_HTML, aircraft=aircraft)
@app.route("/aircraft/LN-<reg>")
def ln_detail(reg):
    registration = f"LN-{reg}"
    row = ln[ln["registration"] == registration]
    if len(row) == 0:
        return f"Aircraft {registration} not found", 404
    r = row.iloc[0]
    def s(val):
        v = str(val).strip()
        return "" if v == "nan" else v
    aircraft = {
        "tail": registration,
        "model": s(r.get("type", "")),
        "manufacturer": s(r.get("manufacturer", "")),
        "build_place": "Norway",
        "serial": s(r.get("serial", "")),
        "year": s(r.get("year_built", "")),
        "reg_date": s(r.get("reg_date", "")),
        "previous": "",
        "country": "NO",
        "name": "", "street": "", "city": "",
        "state": "Norway", "zip": "",
        "engine": "", "cert_date": "",
        "last_action": "", "expiration": "",
    }
    return render_template_string(OY_DETAIL_HTML, aircraft=aircraft)

@app.route("/aircraft/HB-<reg>")
def hb_detail(reg):
    registration = f"HB-{reg}"
    row = hb[hb[" Registration"].str.strip() == registration]
    if len(row) == 0:
        return f"Aircraft {registration} not found", 404
    r = row.iloc[0]
    def s(val):
        v = str(val).strip()
        return "" if v == "nan" else v
    aircraft = {
        "tail": registration,
        "model": s(r.get(" Aicraft Model", "")),
        "manufacturer": s(r.get(" Manufacturer", "")),
        "build_place": "Switzerland",
        "serial": s(r.get(" Serial Number", "")),
        "year": s(r.get(" Year of Manufacture", "")),
        "reg_date": s(r.get(" Date of Registration", "")),
        "previous": "",
        "country": "CH",
        "name": "", "street": "", "city": "",
        "state": "Switzerland", "zip": "",
        "engine": s(r.get(" Engine", "")),
        "cert_date": "", "last_action": "", "expiration": "",
    }
    return render_template_string(OY_DETAIL_HTML, aircraft=aircraft)
if __name__ == "__main__":
    app.run(debug=True, port=8080)