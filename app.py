import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
load_dotenv()

from flask import Flask, render_template_string, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(DB_PATH, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(DB_PATH, 'panpanparts.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = ''

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    password_hash = db.Column(db.String(200))
    country = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    claimed_aircraft = db.Column(db.Text)  # JSON liste af tail numre
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class ClaimedAircraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tail = db.Column(db.String(20), unique=True)
    arc_valid_until = db.Column(db.String(50))
    arc_verified = db.Column(db.Boolean, default=False)
    arc_document = db.Column(db.Text)
    arc_checked_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AircraftListing(db.Model):
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    try:
        with db.engine.connect() as conn:
            conn.execute(db.text("ALTER TABLE user ADD COLUMN claimed_aircraft TEXT"))
            conn.commit()
    except: pass
    try:
        with db.engine.connect() as conn:
            conn.execute(db.text("ALTER TABLE aircraft_listing ADD COLUMN arc_valid_until TEXT"))
            conn.execute(db.text("ALTER TABLE aircraft_listing ADD COLUMN arc_verified INTEGER DEFAULT 0"))
            conn.execute(db.text("ALTER TABLE aircraft_listing ADD COLUMN arc_document TEXT"))
            conn.commit()
    except: pass
print("Loader FAA data...")
import sqlite3 as sql
DB = os.path.join(DB_PATH, 'panpanparts.db')

def search_aircraft(query, limit=50):
    conn = sql.connect(DB)
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM aircraft 
        WHERE registration LIKE ? 
        OR manufacturer LIKE ? 
        OR model LIKE ?
        LIMIT ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%', limit))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_aircraft(registration):
    conn = sql.connect(DB)
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM aircraft WHERE registration = ?', (registration,))
    row = cur.fetchone()
    conn.close()
    return row
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
        .header a { color: #aaa; font-size: 14px; text-decoration: none; margin-left: 20px; }
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
    <div class="header"><h1>PanPan<span>Parts</span></h1><a href="/parts">← Back to listings</a></div>
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
            <a class="part-card" href="/part/{{ p.id }}" style="text-decoration:none;color:inherit">
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
            </a>
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
        .nav a.primary { background: #ff6b35; color: white; padding: 12px 24px; border-radius: 8px; font-size: 16px; font-weight: 600; }
        .nav-login { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 8px; }
        .nav a.nav-signup { color: #ff6b35; border: 1px solid #ff6b35; padding: 8px 16px; border-radius: 8px; font-size: 14px; text-decoration: none; }
        .user-menu { position: relative; margin-left: 8px; }
        .user-btn { background: #1a1a2e; color: #aaa; border: 1px solid #333; padding: 8px 16px; border-radius: 8px; font-size: 14px; cursor: pointer; }
        .dropdown { display: none; position: absolute; right: 0; top: 44px; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 8px; min-width: 140px; z-index: 100; }
        .dropdown a { display: block; padding: 12px 16px; color: #aaa; text-decoration: none; font-size: 14px; }
        .dropdown a:hover { color: white; background: #2a2a3e; }
        .dropdown.open { display: block; }
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
            <a href="/aircraft-for-sale" class="primary">Aircraft for sale</a>
            <a href="/parts" class="primary">Parts for sale</a>
            <a href="/upload" class="primary">+ List a part</a>
            {% if current_user.is_authenticated %}
            <div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} ▾</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div>
            {% else %}
            <a href="/login" class="primary">Log in</a>
            <a href="/register" class="primary">Sign up</a>
            {% endif %}
        </div>
    </div>
    {% if not results %}
    <div class="hero">
        <h1>Find <span>any aviation part</span><br>anywhere in the world</h1>
        <p>The verified marketplace for aircraft parts — with AI-powered documentation checking</p>
        <form method="GET">
            <div class="search-box">
                <input name="tail" placeholder="Search by tail number, e.g. OY-RYY or N12345..." value="{{ tail }}">
                <button type="submit">Search</button>
            </div>
        </form>
        <div class="stats">
            <div class="stat"><div class="stat-value">{{ "{:,.0f}".format(registry_count) }}</div><div class="stat-label">Aircraft registered</div></div>
            <div class="stat"><div class="stat-value">{{ part_count }}</div><div class="stat-label">Parts for sale</div></div>
            <div class="stat"><div class="stat-value">{{ aircraft_count }}</div><div class="stat-label">Aircraft for sale</div></div>
            <div class="stat"><div class="stat-value">AI</div><div class="stat-label">Verified parts</div></div>
        </div>
        <div class="features">
            <div class="feature"><div class="feature-icon">📷</div><h3>Photo to listing in 2 minutes</h3><p>Take photos, AI extracts all data automatically. Just add a price.</p></div>
            <div class="feature"><div class="feature-icon">✓</div><h3>AI verified documentation</h3><p>Every part checked for valid airworthiness documentation.</p></div>
            <div class="feature"><div class="feature-icon">🚚</div><h3>Worldwide shipping</h3><p>Search across USA, Denmark, Norway, Switzerland, Australia and more — with new registries added continuously.</p></div>
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
                <div class="tail">{{ r.tail }}</div>
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
                {% if arc_info and arc_info.arc_verified %}
                <span class="badge badge-green">✓ ARC verified — valid until {{ arc_info.arc_valid_until }}</span>
                {% endif %}
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

        {% if type_total %}
        <div class="card">
            <h3>Fleet statistics</h3>
            <div class="field"><span class="field-label">{{ aircraft.model }} in {{ country_name }}</span><span class="field-value">{{ type_in_country }} aircraft</span></div>
            <div class="field"><span class="field-label">{{ aircraft.model }} worldwide</span><span class="field-value">{{ type_total }} aircraft</span></div>
        </div>
        {% endif %}

        <div class="card">
            <h3>Own this aircraft?</h3>
            <p style="color:#666; font-size:14px; margin-bottom:16px">Claim your aircraft profile to add photos, flight hours, avionics and maintenance history.</p>
            <a href="/claim/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;margin-bottom:10px">Claim {{ aircraft.tail }} — it's free</a>
            <a href="/upload-arc/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2d7a3a;margin-bottom:10px">✓ Upload ARC — verify airworthiness</a>
            <a href="/upload-aircraft?tail={{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2a2a3e">List {{ aircraft.tail }} for sale</a>
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
        <h1>PanPan<span>Parts</span></h1>
        <a href="/">← Back to search</a>
    </div>
    <div class="container">
        <div class="hero">
            <div class="tail-number">{% if aircraft.tail.startswith("OY") or aircraft.tail.startswith("LN") or aircraft.tail.startswith("HB") or aircraft.tail.startswith("VH") %}{{ aircraft.tail }}{% else %}N{{ aircraft.tail }}{% endif %}</div>
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
    import os
    if not os.path.exists('instance/panpanparts.db'):
        return "<html><body style='font-family:sans-serif;text-align:center;padding:100px'><h1>PanPanParts</h1><p>Loading aircraft database... please refresh in 30 seconds.</p></body></html>"
    tail = request.args.get("tail", "")
    # Hvis søgning ikke ligner et tail-nummer, send til type-søgning
    if tail and not any(tail.upper().startswith(p) for p in ["OY", "LN", "HB", "VH", "N", "C-", "G-", "D-", "F-", "OE"]):
        return redirect("/type/" + tail.strip().replace(" ", "-"))
    model = request.args.get("model", "")
    state = request.args.get("state", "")
    year_from = request.args.get("year_from", "")
    year_to = request.args.get("year_to", "")
    states = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]
    results = None
    result_count = 0
    if any([tail, model, state, year_from, year_to]):
        conn = sql.connect(DB)
        conn.row_factory = sql.Row
        cur = conn.cursor()
        query = "SELECT * FROM aircraft WHERE 1=1"
        params = []
        if tail:
            t = tail.upper()
            query += " AND registration LIKE ?"
            params.append(f'%{t}%')
        if model:
            query += " AND model LIKE ?"
            params.append(f'%{model}%')
        if state:
            query += " AND state = ?"
            params.append(state)
        if year_from:
            query += " AND CAST(year AS INTEGER) >= ?"
            params.append(int(year_from))
        if year_to:
            query += " AND CAST(year AS INTEGER) <= ?"
            params.append(int(year_to))
        query += " LIMIT 20"
        cur.execute(query, params)
        rows = cur.fetchall()
        conn.close()
        result_count = len(rows)
        results = []
        for row in rows:
            results.append({
                "tail": row["registration"],
                "model": "" if str(row["model"]).strip() in ["nan", "None", ""] else str(row["model"]).strip(),
                "manufacturer": "" if str(row["manufacturer"]).strip() in ["nan", "None", ""] else str(row["manufacturer"]).strip(),
                "name": row["owner"],
                "city": row["city"],
                "state": row["state"],
                "year": row["year"],
            })
    with app.app_context():
        part_count = Part.query.filter(Part.price != None).count()
        aircraft_count = AircraftListing.query.count()
        import sqlite3 as sql2
        conn2 = sql2.connect(DB)
        registry_count = conn2.execute("SELECT COUNT(*) FROM aircraft").fetchone()[0]
        conn2.close()
    return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
        year_from=year_from, year_to=year_to, states=states,
        results=results, result_count=result_count, part_count=part_count, aircraft_count=aircraft_count, registry_count=registry_count)

@app.route("/aircraft/<tail>")
def aircraft_detail(tail):
    r = get_aircraft('N' + tail.upper())
    if not r:
        r = get_aircraft(tail.upper())
    if not r:
        return render_template_string("""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body{font-family:-apple-system,sans-serif;background:#0d0d1a;color:white;text-align:center;padding:80px 20px}
p{color:#666;margin:16px 0 32px}
a{background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:8px}
.sec{background:#1a1a2e;color:#aaa;padding:14px 28px;border-radius:8px;text-decoration:none;display:inline-block;margin:8px}
</style></head><body>
<p>This aircraft is not in our registry yet.</p>
<a href="/register-aircraft">Register it — it's free</a>
<a href="/" class="sec">← Back to search</a>
</body></html>""")
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v == "nan" or v == "None" else v
    aircraft = {
        "tail": s(r["registration"]),
        "model": s(r["model"]),
        "manufacturer": s(r["manufacturer"]),
        "name": s(r["owner"]),
        "street": "",
        "city": s(r["city"]),
        "state": s(r["state"]),
        "zip": "",
        "country": s(r["country"]),
        "year": s(r["year"]).split(".")[0],
        "serial": s(r["serial"]),
        "engine": "",
        "cert_date": "",
        "last_action": "",
        "expiration": "",
    }
    return render_template_string(OY_DETAIL_HTML, aircraft=aircraft)

@app.route("/upload")
@login_required
def upload():
    return open("upload.html").read()

@app.route("/analyze", methods=["POST"])
@login_required
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
        doc_image=data["doc_image"][:500],
        contact_name=current_user.name,
        contact_email=current_user.email,
        location=data.get("location", ""),
        price=float(data.get("price", 0) or 0),
        description=data.get("description", ""),
        fits_manufacturer=data.get("fits_manufacturer", ""),
        fits_model=data.get("fits_model", "")
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
@login_required
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
@app.route("/aircraft/OY-<reg>")
def oy_detail(reg):
    registration = f"OY-{reg}"
    r = get_aircraft(registration)
    if not r:
        return render_template_string("""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body{font-family:-apple-system,sans-serif;background:#0d0d1a;color:white;text-align:center;padding:80px 20px}
h1{font-size:48px;color:#ff6b35;font-family:monospace}
p{color:#666;margin:16px 0 32px}
a{background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:8px}
.sec{background:#1a1a2e;color:#aaa;padding:14px 28px;border-radius:8px;text-decoration:none;display:inline-block;margin:8px}
</style></head><body>
<h1>{{ tail }}</h1>
<p>This aircraft is not in our registry yet.</p>
<a href="/register-aircraft">Register it — it's free</a>
<a href="/" class="sec">← Back to search</a>
</body></html>""", tail=registration)
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v == "nan" or v == "None" else v
    aircraft = {
        "tail": registration,
        "model": s(r["model"]),
        "manufacturer": s(r["manufacturer"]),
        "build_place": s(r["state"]),
        "serial": s(r["serial"]),
        "year": s(r["year"]).split(".")[0],
        "reg_date": "",
        "previous": "",
        "country": "DK",
        "name": "", "street": "", "city": "",
        "state": "Denmark", "zip": "",
        "engine": "", "cert_date": "",
        "last_action": "", "expiration": "",
    }
    # ARC status
    arc_info = ClaimedAircraft.query.filter_by(tail=registration).first()
    
    # Statistik for flytype
    conn_stat = sql.connect(DB)
    model_query = aircraft["model"] if aircraft["model"] else ""
    if model_query:
        # Søg på præcis model
        total = conn_stat.execute("SELECT COUNT(*) FROM aircraft WHERE model = ?", (model_query,)).fetchone()[0]
        in_country = conn_stat.execute("SELECT COUNT(*) FROM aircraft WHERE model = ? AND country = ?", (model_query, "DK")).fetchone()[0]
    else:
        total = 0
        in_country = 0
    conn_stat.close()
    return render_template_string(OY_DETAIL_HTML, aircraft=aircraft, type_total=total, type_in_country=in_country, country_name="Denmark", arc_info=arc_info)
@app.route("/aircraft/LN-<reg>")
def ln_detail(reg):
    registration = f"LN-{reg}"
    r = get_aircraft(registration)
    if not r:
        return render_template_string("""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body{font-family:-apple-system,sans-serif;background:#0d0d1a;color:white;text-align:center;padding:80px 20px}
h1{font-size:48px;color:#ff6b35;font-family:monospace}
p{color:#666;margin:16px 0 32px}
a{background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:8px}
.sec{background:#1a1a2e;color:#aaa;padding:14px 28px;border-radius:8px;text-decoration:none;display:inline-block;margin:8px}
</style></head><body>
<h1>{{ tail }}</h1>
<p>This aircraft is not in our registry yet.</p>
<a href="/register-aircraft">Register it — it's free</a>
<a href="/" class="sec">← Back to search</a>
</body></html>""", tail=registration)
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v == "nan" or v == "None" else v
    aircraft = {
        "tail": registration,
        "model": s(r["model"]),
        "manufacturer": s(r["manufacturer"]),
        "build_place": "Norway",
        "serial": s(r["serial"]),
        "year": s(r["year"]).split(".")[0],
        "reg_date": "",
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
    r = get_aircraft(registration)
    if not r:
        return render_template_string("""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body{font-family:-apple-system,sans-serif;background:#0d0d1a;color:white;text-align:center;padding:80px 20px}
h1{font-size:48px;color:#ff6b35;font-family:monospace}
p{color:#666;margin:16px 0 32px}
a{background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:8px}
.sec{background:#1a1a2e;color:#aaa;padding:14px 28px;border-radius:8px;text-decoration:none;display:inline-block;margin:8px}
</style></head><body>
<h1>{{ tail }}</h1>
<p>This aircraft is not in our registry yet.</p>
<a href="/register-aircraft">Register it — it's free</a>
<a href="/" class="sec">← Back to search</a>
</body></html>""", tail=registration)
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v == "nan" or v == "None" else v
    aircraft = {
        "tail": registration,
        "model": s(r["model"]),
        "manufacturer": s(r["manufacturer"]),
        "build_place": "Switzerland",
        "serial": s(r["serial"]),
        "year": s(r["year"]).split(".")[0],
        "reg_date": "",
        "previous": "",
        "country": "CH",
        "name": "", "street": "", "city": "",
        "state": "Switzerland", "zip": "",
        "engine": "", "cert_date": "",
        "last_action": "", "expiration": "",
    }
    return render_template_string(OY_DETAIL_HTML, aircraft=aircraft)
if __name__ == "__main__":
    app.run(debug=True, port=8080)


@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML)

ABOUT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>About - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 24px; }
        .container { max-width: 760px; margin: 60px auto; padding: 0 20px; }
        h1 { font-size: 42px; font-weight: 700; margin-bottom: 16px; }
        h1 span { color: #ff6b35; }
        .lead { font-size: 18px; color: #aaa; line-height: 1.7; margin-bottom: 40px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 28px; margin-bottom: 20px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 16px; color: #ff6b35; margin-bottom: 12px; }
        .card p { color: #aaa; line-height: 1.7; font-size: 15px; }
        .contact { margin-top: 40px; color: #666; font-size: 14px; }
        .contact a { color: #ff6b35; text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav"><a href="/aircraft-for-sale" class="primary">Aircraft for sale</a>
            <a href="/parts" class="primary">Parts for sale</a><a href="/upload">+ List a part</a></div>
    </div>
    <div class="container">
        <h1>About <span>PanPanParts</span></h1>
        <p class="lead">A global marketplace for verified aviation parts — built by a pilot, for the aviation community.</p>
        <div class="card"><h3>Why PanPanParts?</h3><p>Finding quality aviation parts has always been fragmented — scattered across forums, emails, and phone calls. PanPanParts brings it all together in one verified marketplace, making it faster and safer to buy and sell aircraft parts anywhere in the world.</p></div>
        <div class="card"><h3>AI-verified documentation</h3><p>Every part listed on PanPanParts goes through AI-powered document verification. Upload a photo of the part and its airworthiness certificate — our system checks it automatically and flags anything that needs a closer look.</p></div>
        <div class="card"><h3>Aircraft registry</h3><p>Search across 346,000+ registered aircraft from the USA, Denmark, Norway, Switzerland and Australia. More registries are being added continuously.</p></div>
        <div class="card"><h3>Pan Pan</h3><p>In aviation, Pan Pan is an urgency call — the step before Mayday. We chose the name because finding the right part quickly can be exactly that urgent.</p></div>
        <div class="contact">Questions: <a href="mailto:hello@panpanparts.com">hello@panpanparts.com</a></div>
    </div>
</body>
</html>
"""

@app.route('/robots.txt')
def robots():
    return open('robots.txt').read(), 200, {'Content-Type': 'text/plain'}

@app.route('/tos')
def tos():
    return open('tos.html').read()

ABOUT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>About - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 24px; }
        .container { max-width: 760px; margin: 60px auto; padding: 0 20px; }
        h1 { font-size: 42px; font-weight: 700; margin-bottom: 16px; }
        h1 span { color: #ff6b35; }
        .lead { font-size: 18px; color: #aaa; line-height: 1.7; margin-bottom: 40px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 28px; margin-bottom: 20px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 16px; color: #ff6b35; margin-bottom: 12px; }
        .card p { color: #aaa; line-height: 1.7; font-size: 15px; }
        .contact { margin-top: 40px; color: #666; font-size: 14px; }
        .contact a { color: #ff6b35; text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav"><a href="/parts">Parts for sale</a><a href="/upload">+ List a part</a></div>
    </div>
    <div class="container">
        <h1>About <span>PanPanParts</span></h1>
        <p class="lead">A global marketplace for verified aviation parts — built by a pilot, for the aviation community.</p>
        <div class="card"><h3>Why PanPanParts?</h3><p>Finding quality aviation parts has always been fragmented — scattered across forums, emails, and phone calls. PanPanParts brings it all together in one verified marketplace, making it faster and safer to buy and sell aircraft parts anywhere in the world.</p></div>
        <div class="card"><h3>AI-verified documentation</h3><p>Every part listed on PanPanParts goes through AI-powered document verification. Upload a photo of the part and its airworthiness certificate — our system checks it automatically and flags anything that needs a closer look.</p></div>
        <div class="card"><h3>Aircraft registry</h3><p>Search across 346,000+ registered aircraft from the USA, Denmark, Norway, Switzerland and Australia. More registries are being added continuously.</p></div>
        <div class="card"><h3>Pan Pan</h3><p>In aviation, Pan Pan is an urgency call — the step before Mayday. We chose the name because finding the right part quickly can be exactly that urgent.</p></div>
        <div class="contact">Questions: <a href="mailto:hello@panpanparts.com">hello@panpanparts.com</a></div>
    </div>
</body>
</html>
"""

LOGIN_HTML = '''<!DOCTYPE html>
<html>
<head>
    <title>Login - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; min-height: 100vh; }
        .header { padding: 20px 40px; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .container { max-width: 420px; margin: 60px auto; padding: 0 20px; }
        h1 { font-size: 32px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 15px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 32px; border: 1px solid #2a2a3e; }
        input { width: 100%; padding: 13px 16px; border: 1px solid #333; border-radius: 8px; font-size: 15px; margin-bottom: 14px; background: #0d0d1a; color: white; }
        .btn { background: #ff6b35; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; }
        .link { text-align: center; margin-top: 20px; color: #666; font-size: 14px; }
        .link a { color: #ff6b35; text-decoration: none; }
        .error { background: rgba(255,100,100,0.1); border: 1px solid rgba(255,100,100,0.3); border-radius: 8px; padding: 12px; margin-bottom: 16px; color: #ff6b6b; font-size: 14px; }
        label { font-size: 13px; color: #aaa; display: block; margin-bottom: 6px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <h1>Welcome <span>back</span></h1>
        <p class="sub">Log in to list parts or contact sellers</p>
        <div class="card">
            {% if error %}<div class="error">{{ error }}</div>{% endif %}
            <form method="POST">
                <label>Email</label>
                <input type="email" name="email" placeholder="your@email.com" required>
                <label>Password</label>
                <input type="password" name="password" placeholder="Your password" required>
                <button class="btn" type="submit">Log in</button>
            </form>
        </div>
        <div class="link">No account? <a href="/register">Sign up free</a></div>
    </div>
</body>
</html>'''

REGISTER_HTML = '''<!DOCTYPE html>
<html>
<head>
    <title>Sign Up - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; min-height: 100vh; }
        .header { padding: 20px 40px; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .container { max-width: 420px; margin: 60px auto; padding: 0 20px; }
        h1 { font-size: 32px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 15px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 32px; border: 1px solid #2a2a3e; }
        input, select { width: 100%; padding: 13px 16px; border: 1px solid #333; border-radius: 8px; font-size: 15px; margin-bottom: 14px; background: #0d0d1a; color: white; }
        .btn { background: #ff6b35; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; }
        .link { text-align: center; margin-top: 20px; color: #666; font-size: 14px; }
        .link a { color: #ff6b35; text-decoration: none; }
        .error { background: rgba(255,100,100,0.1); border: 1px solid rgba(255,100,100,0.3); border-radius: 8px; padding: 12px; margin-bottom: 16px; color: #ff6b6b; font-size: 14px; }
        label { font-size: 13px; color: #aaa; display: block; margin-bottom: 6px; }
        .terms { font-size: 12px; color: #555; margin-top: 16px; text-align: center; }
        .terms a { color: #ff6b35; text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <h1>Join <span>PanPanParts</span></h1>
        <p class="sub">Free account — list parts, contact sellers, claim your aircraft</p>
        <div class="card">
            {% if error %}<div class="error">{{ error }}</div>{% endif %}
            <form method="POST">
                <label>Full name</label>
                <input type="text" name="name" placeholder="Your name" required>
                <label>Email</label>
                <input type="email" name="email" placeholder="your@email.com" required>
                <label>Password</label>
                <input type="password" name="password" placeholder="Min. 8 characters" required>
                <label>Country</label>
                <select name="country">
                    <option>Denmark</option><option>Norway</option><option>Sweden</option>
                    <option>Finland</option><option>United Kingdom</option><option>Germany</option>
                    <option>France</option><option>Netherlands</option><option>Belgium</option>
                    <option>Switzerland</option><option>Austria</option><option>United States</option>
                    <option>Canada</option><option>Australia</option><option>Other</option>
                </select>
                <button class="btn" type="submit">Create free account</button>
            </form>
            <p class="terms">By signing up you agree to our <a href="/tos">Terms of Service</a></p>
        </div>
        <div class="link">Already have an account? <a href="/login">Log in</a></div>
    </div>
</body>
</html>'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    error = None
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        with app.app_context():
            user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect('/')
        error = 'Invalid email or password'
    return render_template_string(LOGIN_HTML, error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        country = request.form.get('country', '')
        if len(password) < 8:
            error = 'Password must be at least 8 characters'
        else:
            with app.app_context():
                existing = User.query.filter_by(email=email).first()
                if existing:
                    error = 'An account with this email already exists'
                else:
                    user = User(name=name, email=email, country=country)
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect('/')
    return render_template_string(REGISTER_HTML, error=error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/claim/<tail>')
def claim(tail):
    if not current_user.is_authenticated:
        return redirect('/register?next=/claim/' + tail)
    import json
    user = User.query.get(current_user.id)
    claimed = json.loads(user.claimed_aircraft or '[]')
    if tail.upper() not in claimed:
        claimed.append(tail.upper())
        user.claimed_aircraft = json.dumps(claimed)
        db.session.commit()
    return redirect('/aircraft/' + tail + '?claimed=1')

@app.route('/my-aircraft')
@login_required
def my_aircraft():
    import json
    claimed = json.loads(current_user.claimed_aircraft or '[]')
    aircraft_list = []
    for tail in claimed:
        r = get_aircraft(tail)
        if not r:
            r = get_aircraft('N' + tail)
        if r:
            def s(val):
                v = str(val).strip() if val else ""
                return "" if v in ["nan", "None"] else v
            aircraft_list.append({
                "tail": s(r["registration"]),
                "model": s(r["model"]),
                "manufacturer": s(r["manufacturer"]),
                "year": s(r["year"]).split(".")[0],
                "country": s(r["country"]),
            })
        else:
            aircraft_list.append({"tail": tail, "model": "", "manufacturer": "", "year": "", "country": ""})
    return render_template_string(MY_AIRCRAFT_HTML, aircraft=aircraft_list)

MY_AIRCRAFT_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>My Aircraft - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        h1 { font-size: 32px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 15px; }
        .aircraft-card { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-bottom: 12px; border: 1px solid #2a2a3e; display: flex; justify-content: space-between; align-items: center; text-decoration: none; color: white; }
        .aircraft-card:hover { border-color: #ff6b35; }
        .tail { font-size: 28px; font-weight: 700; color: #ff6b35; font-family: monospace; }
        .model { font-size: 16px; margin: 4px 0; }
        .meta { color: #666; font-size: 13px; }
        .btn { background: #ff6b35; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-size: 14px; cursor: pointer; text-decoration: none; }
        .empty { text-align: center; padding: 60px 0; color: #666; }
        .empty a { color: #ff6b35; text-decoration: none; }
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
            <a href="/parts">Parts for sale</a>
            <div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} &#9660;</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div>
        </div>
    </div>
    <div class="container">
        <h1>My <span>Aircraft</span></h1>
        <p class="sub">Aircraft you have claimed on PanPanParts</p>
        {% if aircraft %}
            {% for a in aircraft %}
            <a class="aircraft-card" href="/aircraft/{{ a.tail }}">
                <div>
                    <div class="tail">{{ a.tail }}</div>
                    <div class="model">{{ a.manufacturer }} {{ a.model }}</div>
                    <div class="meta">{{ a.year }} · {{ a.country }}</div>
                </div>
                <div>
                    <a href="/upload" class="btn">+ List a part</a>
                </div>
            </a>
            {% endfor %}
        {% else %}
            <div class="empty">
                <p>No aircraft claimed yet</p>
                <p style="margin-top:12px"><a href="/">Search for your aircraft</a> and click Claim</p>
            </div>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/my-listings')
@login_required
def my_listings():
    with app.app_context():
        parts = Part.query.filter_by(contact_email=current_user.email).order_by(Part.created_at.desc()).all()
    return render_template_string(MY_LISTINGS_HTML, parts=parts)

MY_LISTINGS_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>My Listings - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        h1 { font-size: 32px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 15px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-bottom: 12px; border: 1px solid #2a2a3e; display: flex; justify-content: space-between; align-items: center; }
        .part-number { font-size: 18px; font-weight: 600; margin-bottom: 4px; }
        .meta { color: #666; font-size: 13px; }
        .price { font-size: 24px; font-weight: 700; color: #ff6b35; }
        .badge { background: rgba(45,122,58,0.2); color: #4caf50; padding: 4px 10px; border-radius: 20px; font-size: 12px; margin-top: 6px; display: inline-block; }
        .empty { text-align: center; padding: 60px 0; color: #666; }
        .empty a { color: #ff6b35; text-decoration: none; }
        .btn { background: #ff6b35; color: white; text-decoration: none; padding: 10px 20px; border-radius: 8px; font-size: 14px; }
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
            <a href="/upload" class="btn">+ List a part</a>
            <div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} &#9660;</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div>
        </div>
    </div>
    <div class="container">
        <h1>My <span>Listings</span></h1>
        <p class="sub">Parts you have listed for sale</p>
        {% if parts %}
            {% for p in parts %}
            <div class="card">
                <div>
                    <div class="part-number">{{ p.part_number or 'Unknown part' }}</div>
                    <div class="meta">{{ p.location }} · {{ p.part_condition }}</div>
                    <span class="badge">{{ p.ai_recommendation }}</span>
                </div>
                <div style="text-align:right">
                    <div class="price">€{{ p.price }}</div>
                </div>
            </a>
            {% endfor %}
        {% else %}
            <div class="empty">
                <p>No listings yet</p>
                <p style="margin-top:12px"><a href="/upload">List your first part</a></p>
            </div>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/part/<int:part_id>')
def part_detail(part_id):
    with app.app_context():
        part = Part.query.get_or_404(part_id)
    return render_template_string(PART_DETAIL_HTML, part=part, logged_in=current_user.is_authenticated)

PART_DETAIL_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>{{ part.part_number or 'Part' }} - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }
        .back:hover { color: white; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 28px; margin-bottom: 16px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; color: #666; margin-bottom: 16px; }
        .part-title { font-size: 28px; font-weight: 700; margin-bottom: 8px; }
        .price { font-size: 36px; font-weight: 700; color: #ff6b35; margin-bottom: 8px; }
        .badge { background: rgba(45,122,58,0.2); color: #4caf50; padding: 6px 14px; border-radius: 20px; font-size: 13px; display: inline-block; border: 1px solid rgba(76,175,80,0.3); }
        .badge-warn { background: rgba(255,107,53,0.2); color: #ff6b35; border-color: rgba(255,107,53,0.3); }
        .field { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #2a2a3e; font-size: 14px; }
        .field:last-child { border-bottom: none; }
        .field-label { color: #666; }
        .contact-btn { display: block; background: #ff6b35; color: white; text-align: center; padding: 16px; border-radius: 10px; font-size: 16px; font-weight: 600; text-decoration: none; margin-top: 8px; }
        .contact-btn:hover { background: #e55a25; }
        .login-prompt { background: #1a1a2e; border-radius: 12px; padding: 28px; text-align: center; border: 1px solid #2a2a3e; }
        .login-prompt p { color: #666; margin-bottom: 16px; }
        .login-prompt a { color: #ff6b35; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            {% if logged_in %}
            <a href="/my-listings">My listings</a>
            <a href="/logout">Log out</a>
            {% else %}
            <a href="/login">Log in</a>
            <a href="/register">Sign up</a>
            {% endif %}
        </div>
    </div>
    <div class="container">
        <a href="/parts" class="back">← Back to listings</a>
        <div class="card">
            <div class="part-title">{{ part.part_number or 'Unknown part' }}</div>
            <div style="margin:12px 0">
                <span class="badge {% if part.ai_recommendation != 'Approved for listing' %}badge-warn{% endif %}">
                    ✓ {{ part.ai_recommendation }}
                </span>
            </div>
            <div class="price">€{{ part.price }}</div>
            <p style="color:#aaa;margin-top:12px">{{ part.description or '' }}</p>
        </div>

        <div class="card">
            <h3>Part details</h3>
            <div class="field"><span class="field-label">Part number</span><span>{{ part.part_number or '—' }}</span></div>
            <div class="field"><span class="field-label">Serial number</span><span>{{ part.serial_number or '—' }}</span></div>
            <div class="field"><span class="field-label">Condition</span><span>{{ part.part_condition or '—' }}</span></div>
            <div class="field"><span class="field-label">Issued by</span><span>{{ part.issued_by or '—' }}</span></div>
            <div class="field"><span class="field-label">Issue date</span><span>{{ part.issue_date or '—' }}</span></div>
            <div class="field"><span class="field-label">Location</span><span>{{ part.location or '—' }}</span></div>
        </div>

        {% if logged_in %}
        <div class="card">
            <h3>Contact seller</h3>
            <div class="field"><span class="field-label">Name</span><span>{{ part.contact_name }}</span></div>
            <div class="field"><span class="field-label">Location</span><span>{{ part.location or '—' }}</span></div>
            <a href="mailto:{{ part.contact_email }}?subject=Regarding your listing: {{ part.part_number }}" class="contact-btn">
                ✉ Contact seller
            </a>
        </div>
        {% else %}
        <div class="login-prompt">
            <p>Log in to see seller contact details</p>
            <a href="/login">Log in</a> or <a href="/register">create a free account</a>
        </div>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/sell-aircraft/<tail>', methods=['GET', 'POST'])
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
    return render_template_string(SELL_AIRCRAFT_HTML, aircraft=aircraft)

SELL_AIRCRAFT_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>List for Sale - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 600px; margin: 40px auto; padding: 0 20px; }
        h1 { font-size: 28px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; }
        .info-box { background: #1a1a2e; border-radius: 12px; padding: 20px; margin-bottom: 24px; border: 1px solid #2a2a3e; display: flex; justify-content: space-between; align-items: center; }
        .tail { font-size: 32px; font-weight: 700; color: #ff6b35; font-family: monospace; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-bottom: 16px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 13px; text-transform: uppercase; color: #666; margin-bottom: 16px; }
        label { font-size: 13px; color: #aaa; display: block; margin-bottom: 6px; }
        input, textarea { width: 100%; padding: 12px; border: 1px solid #333; border-radius: 8px; font-size: 15px; margin-bottom: 14px; background: #0d0d1a; color: white; }
        textarea { height: 100px; resize: vertical; }
        .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .btn { background: #ff6b35; color: white; border: none; padding: 16px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav"><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div>
    </div>
    <div class="container">
        <h1>List <span>{{ aircraft.tail }}</span> for sale</h1>
        <p class="sub">Fill in the details to list your aircraft</p>
        <div class="info-box">
            <div><div class="tail">{{ aircraft.tail }}</div><div style="color:#aaa;margin-top:4px">{{ aircraft.manufacturer }} {{ aircraft.model }}</div></div>
            <div style="color:#666">{{ aircraft.year }}</div>
        </div>
        <form method="POST">
            <div class="card">
                <h3>Price</h3>
                <label>Asking price (EUR)</label>
                <input type="number" name="price" placeholder="e.g. 45000" min="0" required>
            </div>
            <div class="card">
                <h3>Hours</h3>
                <div class="row">
                    <div><label>Total airframe hours</label><input type="number" name="hours_total" placeholder="e.g. 3200" min="0"></div>
                    <div><label>Engine hours SMOH</label><input type="number" name="hours_engine" placeholder="e.g. 450" min="0"></div>
                </div>
            </div>
            <div class="card">
                <h3>Description</h3>
                <textarea name="description" placeholder="Condition, avionics, recent maintenance, reason for selling..."></textarea>
                <label>Location</label>
                <input type="text" name="location" placeholder="e.g. Roskilde, Denmark">
            </div>
            <button class="btn" type="submit">Publish listing</button>
        </form>
    </div>
</body>
</html>"""

@app.route('/aircraft-for-sale')
def aircraft_for_sale():
    listings = AircraftListing.query.order_by(AircraftListing.created_at.desc()).all()
    return render_template_string(AIRCRAFT_FOR_SALE_HTML, listings=listings)

AIRCRAFT_FOR_SALE_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Aircraft for Sale - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .nav a.primary { background: #ff6b35; color: white; padding: 10px 20px; border-radius: 8px; }
        .container { max-width: 900px; margin: 40px auto; padding: 0 20px; }
        h1 { font-size: 36px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; }
        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; text-decoration: none; color: white; display: block; }
        .card:hover { border-color: #ff6b35; }
        .tail { font-size: 24px; font-weight: 700; color: #ff6b35; font-family: monospace; }
        .model { font-size: 15px; margin: 6px 0 4px; }
        .meta { color: #666; font-size: 13px; }
        .price { font-size: 22px; font-weight: 700; color: white; margin-top: 12px; }
        .hours { color: #aaa; font-size: 13px; margin-top: 4px; }
        .empty { text-align: center; padding: 80px 0; color: #666; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/">Search registry</a>
            <a href="/parts">Parts for sale</a>
            {% if current_user.is_authenticated %}
            <a href="/my-aircraft" class="primary">My aircraft</a>
            {% else %}
            <a href="/register" class="primary">Sign up</a>
            {% endif %}
        </div>
    </div>
    <div class="container">
        <h1>Aircraft <span>for Sale</span></h1>
        <p class="sub">{{ listings|length }} aircraft listed</p>
        {% if listings %}
        <div class="grid">
            {% for l in listings %}
            <a class="card" href="/aircraft-listing/{{ l.id }}">
                <div class="tail">{{ l.tail }}</div>
                <div class="model">{{ l.manufacturer }} {{ l.model }}</div>
                <div class="meta">{{ l.year }} · {{ l.location }}</div>
                <div class="price">€{{ "{:,.0f}".format(l.price) }}</div>
                <div class="hours">
                    {% if l.hours_total %}{{ l.hours_total|int }} hrs TT{% endif %}
                    {% if l.hours_engine %} · {{ l.hours_engine|int }} SMOH{% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty">
            <p>No aircraft listed yet</p>
            <p style="margin-top:12px;color:#ff6b35">Be the first to list your aircraft</p>
        </div>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/type/<query>')
def aircraft_type(query):
    search = query.replace("-", " ")
    
    # AI beskrivelse
    try:
        import anthropic as ac
        client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=200,
            messages=[{"role": "user", "content": f"Give a brief 2 sentence description of the {search} aircraft. Be concise and factual."}]
        )
        ai_description = response.content[0].text
    except Exception as e:
        print("AI fejl:", e)
        ai_description = None
    
    # Fly til salg
    listings = AircraftListing.query.filter(
        db.or_(
            AircraftListing.model.ilike(f'%{search}%'),
            AircraftListing.manufacturer.ilike(f'%{search}%')
        )
    ).all()
    
    # Dele til salg
    parts = Part.query.filter(
        db.or_(
            Part.part_number.ilike(f'%{search}%'),
            Part.description.ilike(f'%{search}%'),
            Part.condition_notes.ilike(f'%{search}%')
        )
    ).filter(Part.price != None).all()
    
    return render_template_string(TYPE_PAGE_HTML, 
        search=search,
        listings=listings,
        parts=parts,
        ai_description=ai_description)

TYPE_PAGE_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>{{ search }} - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .nav a.primary { background: #ff6b35; color: white; padding: 10px 20px; border-radius: 8px; }
        .container { max-width: 900px; margin: 40px auto; padding: 0 20px; }
        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }
        h1 { font-size: 40px; font-weight: 700; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 40px; }
        h2 { font-size: 20px; margin-bottom: 16px; margin-top: 40px; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 12px; margin-bottom: 16px; }
        .stat-card { background: #1a1a2e; border-radius: 10px; padding: 16px; border: 1px solid #2a2a3e; text-align: center; }
        .stat-value { font-size: 24px; font-weight: 700; color: #ff6b35; }
        .stat-label { font-size: 12px; color: #666; margin-top: 4px; }
        .aircraft-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
        .aircraft-card { background: #1a1a2e; border-radius: 12px; padding: 20px; border: 1px solid #2a2a3e; text-decoration: none; color: white; }
        .aircraft-card:hover { border-color: #ff6b35; }
        .tail { font-size: 22px; font-weight: 700; color: #ff6b35; font-family: monospace; }
        .price { font-size: 20px; font-weight: 700; margin-top: 10px; }
        .meta { color: #666; font-size: 13px; margin-top: 4px; }
        .part-card { background: #1a1a2e; border-radius: 12px; padding: 20px; border: 1px solid #2a2a3e; text-decoration: none; color: white; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .part-card:hover { border-color: #ff6b35; }
        .empty { color: #555; font-size: 14px; padding: 20px 0; }
        .total-badge { background: rgba(255,107,53,0.15); border: 1px solid rgba(255,107,53,0.3); border-radius: 20px; padding: 6px 16px; font-size: 14px; color: #ff6b35; display: inline-block; margin-bottom: 32px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/aircraft-for-sale">Aircraft for sale</a>
            <a href="/parts">Parts for sale</a>
            {% if current_user.is_authenticated %}
            <a href="/my-aircraft" class="primary">My aircraft</a>
            {% else %}
            <a href="/register" class="primary">Sign up</a>
            {% endif %}
        </div>
    </div>
    <div class="container">
        <a href="/" class="back">← Search</a>
        <h1>{{ search }}</h1>
        {% if ai_description %}
        <p style="color:#aaa;font-size:15px;line-height:1.7;margin:16px 0 32px;max-width:680px">{{ ai_description }}</p>
        {% endif %}

        <h2>Aircraft for sale</h2>
        {% if listings %}
        <div class="aircraft-grid">
            {% for l in listings %}
            <a class="aircraft-card" href="/aircraft-listing/{{ l.id }}">
                <div class="tail">{{ l.tail }}</div>
                <div class="meta">{{ l.manufacturer }} {{ l.model }}</div>
                <div class="meta">{{ l.year }} · {{ l.location }}</div>
                {% if l.arc_verified %}
                <div style="color:#4caf50;font-size:12px;margin-top:6px">✓ ARC verified</div>
                {% endif %}
                <div class="price">€{{ "{:,.0f}".format(l.price) }}</div>
            </a>
            {% endfor %}
        </div>
        {% else %}
        <p class="empty">No {{ search }} listed for sale yet. <a href="/" style="color:#ff6b35">Own one? List it free.</a></p>
        {% endif %}

        <h2>Parts for sale</h2>
        {% if parts %}
            {% for p in parts %}
            <a class="part-card" href="/part/{{ p.id }}">
                <div>
                    <div style="font-weight:600">{{ p.part_number or "Unknown part" }}</div>
                    <div class="meta">{{ p.location }} · {{ p.part_condition }}</div>
                </div>
                <div style="font-weight:700;color:#ff6b35">€{{ p.price }}</div>
            </a>
            {% endfor %}
        {% else %}
        <p class="empty">No parts for {{ search }} listed yet. <a href="/upload" style="color:#ff6b35">List a part free.</a></p>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/register-aircraft', methods=['GET', 'POST'])
@login_required
def register_aircraft():
    if request.method == 'POST':
        tail = request.form.get('tail', '').strip().upper()
        manufacturer = request.form.get('manufacturer', '').strip()
        model = request.form.get('model', '').strip()
        year = request.form.get('year', '').strip()
        country = request.form.get('country', '').strip()
        
        if tail:
            conn_r = sql.connect(DB)
            existing = conn_r.execute("SELECT registration FROM aircraft WHERE registration = ?", (tail,)).fetchone()
            if not existing:
                conn_r.execute("INSERT INTO aircraft (registration, manufacturer, model, year, serial, country, owner, city, state, source) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (tail, manufacturer, model, year, '', country, current_user.name, '', country, 'User registered'))
                conn_r.commit()
            conn_r.close()
            return redirect('/claim/' + tail)
    
    return render_template_string(REGISTER_AIRCRAFT_HTML)

REGISTER_AIRCRAFT_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Register Aircraft - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 500px; margin: 40px auto; padding: 0 20px; }
        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }
        h1 { font-size: 28px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 15px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 28px; border: 1px solid #2a2a3e; }
        label { font-size: 13px; color: #aaa; display: block; margin-bottom: 6px; }
        input, select { width: 100%; padding: 12px; border: 1px solid #333; border-radius: 8px; font-size: 15px; margin-bottom: 16px; background: #0d0d1a; color: white; }
        .btn { background: #ff6b35; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; }
        .note { color: #555; font-size: 13px; margin-top: 16px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav"><a href="/">← Search</a></div>
    </div>
    <div class="container">
        <h1>Register your <span>aircraft</span></h1>
        <p class="sub">Can't find your aircraft in our registry? Add it manually.</p>
        <div class="card">
            <form method="POST">
                <label>Registration / Tail number *</label>
                <input type="text" name="tail" placeholder="e.g. OY-ABC or N12345" required>
                <label>Manufacturer *</label>
                <input type="text" name="manufacturer" placeholder="e.g. Cessna" required>
                <label>Model *</label>
                <input type="text" name="model" placeholder="e.g. 172S Skyhawk" required>
                <label>Year built</label>
                <input type="number" name="year" placeholder="e.g. 1998" min="1900" max="2030">
                <label>Country of registration</label>
                <select name="country">
                    <option>Denmark</option>
                    <option>Norway</option>
                    <option>Sweden</option>
                    <option>United Kingdom</option>
                    <option>Germany</option>
                    <option>France</option>
                    <option>Netherlands</option>
                    <option>Switzerland</option>
                    <option>Austria</option>
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Australia</option>
                    <option>Other</option>
                </select>
                <button class="btn" type="submit">Register and claim aircraft</button>
            </form>
            <p class="note">Your aircraft will be added to the PanPanParts registry and automatically claimed to your account.</p>
        </div>
    </div>
</body>
</html>"""

@app.route('/upload-arc/<tail>', methods=['GET', 'POST'])
@login_required
def upload_arc(tail):
    return render_template_string(UPLOAD_ARC_HTML, tail=tail)

@app.route('/verify-arc', methods=['POST'])
@login_required
def verify_arc():
    import anthropic as ac, json, base64
    data = request.get_json()
    tail = data.get('tail', '')
    image = data.get('image', '')
    
    client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image}},
            {"type": "text", "text": f"""You are an aviation document expert. Analyze this document.
Is this an Airworthiness Review Certificate (ARC) or Annual Inspection record for aircraft {tail}?

Respond ONLY with JSON:
{{
  "is_arc": true or false,
  "tail_number": "registration found in document or null",
  "tail_matches": true or false,
  "valid_until": "expiry date in YYYY-MM-DD format or null",
  "issued_by": "organization name or null",
  "issue_date": "issue date in YYYY-MM-DD format or null",
  "confidence": "high / medium / low",
  "notes": "any important observations"
}}"""}
        ]}]
    )
    
    text = response.content[0].text
    clean = text.replace("```json","").replace("```","").strip()
    result = json.loads(clean)
    
    if result.get('is_arc') and result.get('tail_matches'):
        # Gem i databasen
        existing = ClaimedAircraft.query.filter_by(tail=tail.upper()).first()
        if existing:
            existing.arc_valid_until = result.get('valid_until')
            existing.arc_verified = True
            existing.arc_document = image[:500]
            existing.arc_checked_at = datetime.utcnow()
        else:
            claimed = ClaimedAircraft(
                user_id=current_user.id,
                tail=tail.upper(),
                arc_valid_until=result.get('valid_until'),
                arc_verified=True,
                arc_document=image[:500],
                arc_checked_at=datetime.utcnow()
            )
            db.session.add(claimed)
        db.session.commit()
    
    return json.dumps(result)

UPLOAD_ARC_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Upload ARC - {{ tail }} - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .container { max-width: 560px; margin: 40px auto; padding: 0 20px; }
        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }
        h1 { font-size: 28px; margin-bottom: 8px; }
        h1 span { color: #ff6b35; }
        .sub { color: #666; margin-bottom: 32px; font-size: 15px; line-height: 1.6; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 28px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .card h3 { font-size: 13px; text-transform: uppercase; color: #666; margin-bottom: 16px; letter-spacing: 0.5px; }
        .upload-box { border: 2px dashed #333; border-radius: 10px; padding: 40px 20px; text-align: center; cursor: pointer; }
        .upload-box:hover { border-color: #ff6b35; }
        .upload-box img { width: 100%; max-height: 300px; object-fit: contain; border-radius: 8px; display: none; }
        .upload-icon { font-size: 40px; margin-bottom: 12px; }
        .upload-text { color: #666; font-size: 14px; }
        input[type=file] { display: none; }
        .btn { background: #ff6b35; color: white; border: none; padding: 16px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; margin-top: 16px; }
        .btn:disabled { background: #333; cursor: not-allowed; }
        .result { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-top: 16px; display: none; border: 1px solid #2a2a3e; }
        .result.success { border-color: #4caf50; }
        .result.error { border-color: #ff4444; }
        .result h3 { margin-bottom: 12px; }
        .field { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #2a2a3e; font-size: 14px; }
        .field:last-child { border-bottom: none; }
        .field-label { color: #666; }
        .badge-ok { color: #4caf50; }
        .badge-warn { color: #ff6b35; }
        .continue-btn { display: block; background: #4caf50; color: white; text-align: center; padding: 14px; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 16px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <a href="/aircraft/{{ tail }}" class="back">← Back to {{ tail }}</a>
        <h1>Verify <span>{{ tail }}</span></h1>
        <p class="sub">Upload your Airworthiness Review Certificate (ARC) or Annual Inspection record. AI will verify the document and confirm your aircraft is airworthy.</p>

        <div class="card">
            <h3>Upload ARC document</h3>
            <div class="upload-box" onclick="document.getElementById('arc-input').click()">
                <img id="arc-preview">
                <div id="upload-content">
                    <div class="upload-icon">📋</div>
                    <div class="upload-text">Click to upload ARC or Annual Inspection<br><small style="color:#444">Photo or scan of the document</small></div>
                </div>
                <input type="file" id="arc-input" accept="image/*" onchange="loadImage(this)">
            </div>
            <button class="btn" id="verify-btn" onclick="verify()" disabled>Verify with AI</button>
        </div>

        <div class="result" id="result">
            <h3 id="result-title"></h3>
            <div id="result-fields"></div>
            <a href="/my-aircraft" class="continue-btn" id="continue-btn" style="display:none">✓ Continue to My Aircraft</a>
        </div>
    </div>

    <script>
        var imageData = null;
        var tail = "{{ tail }}";

        function loadImage(input) {
            var file = input.files[0];
            if (!file) return;
            var img = new Image();
            var url = URL.createObjectURL(file);
            img.onload = function() {
                var canvas = document.createElement('canvas');
                var max = 1600;
                var w = img.width, h = img.height;
                if (w > max) { h = h*max/w; w = max; }
                canvas.width = w; canvas.height = h;
                canvas.getContext('2d').drawImage(img, 0, 0, w, h);
                var jpeg = canvas.toDataURL('image/jpeg', 0.85);
                var preview = document.getElementById('arc-preview');
                preview.src = jpeg;
                preview.style.display = 'block';
                document.getElementById('upload-content').style.display = 'none';
                imageData = jpeg.split(',')[1];
                document.getElementById('verify-btn').disabled = false;
                URL.revokeObjectURL(url);
            };
            img.src = url;
        }

        function verify() {
            document.getElementById('verify-btn').disabled = true;
            document.getElementById('verify-btn').textContent = 'Analyzing...';
            
            fetch('/verify-arc', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({tail: tail, image: imageData})
            })
            .then(r => r.json())
            .then(data => {
                var result = document.getElementById('result');
                var fields = '';
                
                if (data.is_arc && data.tail_matches) {
                    result.className = 'result success';
                    document.getElementById('result-title').innerHTML = '✓ ARC Verified';
                    fields += '<div class="field"><span class="field-label">Aircraft</span><span class="badge-ok">' + (data.tail_number || tail) + '</span></div>';
                    fields += '<div class="field"><span class="field-label">Valid until</span><span class="badge-ok">' + (data.valid_until || 'See document') + '</span></div>';
                    fields += '<div class="field"><span class="field-label">Issued by</span><span>' + (data.issued_by || '—') + '</span></div>';
                    fields += '<div class="field"><span class="field-label">Confidence</span><span>' + data.confidence + '</span></div>';
                    document.getElementById('continue-btn').style.display = 'block';
                } else {
                    result.className = 'result error';
                    document.getElementById('result-title').innerHTML = '✗ Verification failed';
                    if (!data.is_arc) fields += '<div class="field"><span class="field-label">Issue</span><span class="badge-warn">Document does not appear to be an ARC</span></div>';
                    if (!data.tail_matches) fields += '<div class="field"><span class="field-label">Issue</span><span class="badge-warn">Tail number does not match ' + tail + '</span></div>';
                    if (data.notes) fields += '<div class="field"><span class="field-label">Notes</span><span>' + data.notes + '</span></div>';
                }
                
                document.getElementById('result-fields').innerHTML = fields;
                result.style.display = 'block';
                document.getElementById('verify-btn').textContent = 'Verify with AI';
                document.getElementById('verify-btn').disabled = false;
            })
            .catch(e => {
                document.getElementById('verify-btn').textContent = 'Verify with AI';
                document.getElementById('verify-btn').disabled = false;
                alert('Error: ' + e.message);
            });
        }
    </script>
</body>
</html>"""

@app.route('/aircraft-listing/<int:listing_id>')
def aircraft_listing_detail(listing_id):
    listing = AircraftListing.query.get_or_404(listing_id)
    return render_template_string(AIRCRAFT_LISTING_DETAIL_HTML, 
        listing=listing, 
        logged_in=current_user.is_authenticated)

AIRCRAFT_LISTING_DETAIL_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>{{ listing.tail }} for Sale - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }
        .hero { background: #1a1a2e; border-radius: 16px; padding: 36px; margin-bottom: 20px; border: 1px solid #2a2a3e; }
        .tail { font-size: 52px; font-weight: 700; color: #ff6b35; font-family: monospace; }
        .model { font-size: 22px; margin: 8px 0 4px; }
        .meta { color: #666; font-size: 15px; }
        .price { font-size: 42px; font-weight: 700; margin-top: 16px; }
        .badges { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
        .badge { padding: 6px 14px; border-radius: 20px; font-size: 13px; }
        .badge-green { background: rgba(76,175,80,0.2); color: #4caf50; border: 1px solid rgba(76,175,80,0.3); }
        .badge-blue { background: rgba(74,158,255,0.2); color: #4a9eff; border: 1px solid rgba(74,158,255,0.3); }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; margin-bottom: 16px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 13px; text-transform: uppercase; color: #666; margin-bottom: 16px; letter-spacing: 0.5px; }
        .field { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #2a2a3e; font-size: 14px; }
        .field:last-child { border-bottom: none; }
        .field-label { color: #666; }
        .description { color: #aaa; line-height: 1.7; font-size: 15px; }
        .contact-btn { display: block; background: #ff6b35; color: white; text-align: center; padding: 16px; border-radius: 10px; font-size: 16px; font-weight: 600; text-decoration: none; }
        .contact-btn:hover { background: #e55a25; }
        .login-prompt { background: #1a1a2e; border-radius: 12px; padding: 28px; text-align: center; border: 1px solid #2a2a3e; }
        .login-prompt p { color: #666; margin-bottom: 16px; }
        .login-prompt a { color: #ff6b35; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/aircraft-for-sale">All aircraft</a>
            {% if logged_in %}
            <a href="/my-listings">My listings</a>
            {% else %}
            <a href="/register">Sign up</a>
            {% endif %}
        </div>
    </div>
    <div class="container">
        <a href="/aircraft-for-sale" class="back">← All aircraft for sale</a>
        
        <div class="hero">
            <div class="tail">{{ listing.tail }}</div>
            <div class="model">{{ listing.manufacturer }} {{ listing.model }}</div>
            <div class="meta">{{ listing.year }} · {{ listing.location }}</div>
            <div class="price">€{{ "{:,.0f}".format(listing.price) }}</div>
            <div class="badges">
                {% if listing.arc_verified %}
                <span class="badge badge-green">✓ ARC Verified</span>
                {% endif %}
                {% if listing.hours_total %}
                <span class="badge badge-blue">{{ listing.hours_total|int }} hrs TT</span>
                {% endif %}
                {% if listing.hours_engine %}
                <span class="badge badge-blue">{{ listing.hours_engine|int }} hrs SMOH</span>
                {% endif %}
            </div>
        </div>

        {% if listing.description %}
        <div class="card">
            <h3>Description</h3>
            <p class="description">{{ listing.description }}</p>
        </div>
        {% endif %}

        <div class="card">
            <h3>Details</h3>
            <div class="field"><span class="field-label">Registration</span><span>{{ listing.tail }}</span></div>
            <div class="field"><span class="field-label">Manufacturer</span><span>{{ listing.manufacturer }}</span></div>
            <div class="field"><span class="field-label">Model</span><span>{{ listing.model }}</span></div>
            <div class="field"><span class="field-label">Year</span><span>{{ listing.year }}</span></div>
            {% if listing.hours_total %}
            <div class="field"><span class="field-label">Total hours</span><span>{{ listing.hours_total|int }} hrs</span></div>
            {% endif %}
            {% if listing.hours_engine %}
            <div class="field"><span class="field-label">Engine SMOH</span><span>{{ listing.hours_engine|int }} hrs</span></div>
            {% endif %}
            <div class="field"><span class="field-label">Location</span><span>{{ listing.location }}</span></div>
            {% if listing.arc_verified and listing.arc_valid_until %}
            <div class="field"><span class="field-label">ARC valid until</span><span style="color:#4caf50">{{ listing.arc_valid_until }}</span></div>
            {% endif %}
        </div>

        {% if logged_in %}
        <div class="card">
            <h3>Contact seller</h3>
            <div class="field"><span class="field-label">Name</span><span>{{ listing.contact_name }}</span></div>
            <div class="field"><span class="field-label">Location</span><span>{{ listing.location }}</span></div>
            <a href="mailto:{{ listing.contact_email }}?subject=Regarding {{ listing.tail }} for sale" class="contact-btn" style="margin-top:16px">
                ✉ Contact seller
            </a>
        </div>
        {% else %}
        <div class="login-prompt">
            <p>Log in to see seller contact details</p>
            <a href="/login">Log in</a> or <a href="/register">create a free account</a>
        </div>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/sitemap.xml')
def sitemap():
    return render_template_string("""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap><loc>https://panpanparts.com/sitemap-pages.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-1.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-2.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-3.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-4.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-5.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-6.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-7.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-8.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-9.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-10.xml</loc></sitemap>
    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-11.xml</loc></sitemap>
</sitemapindex>"""), 200, {'Content-Type': 'application/xml'}

@app.route('/sitemap-pages.xml')
def sitemap_pages():
    return render_template_string("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://panpanparts.com/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>
    <url><loc>https://panpanparts.com/parts</loc><changefreq>daily</changefreq><priority>0.9</priority></url>
    <url><loc>https://panpanparts.com/aircraft-for-sale</loc><changefreq>daily</changefreq><priority>0.9</priority></url>
    <url><loc>https://panpanparts.com/about</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>
    <url><loc>https://panpanparts.com/tos</loc><changefreq>monthly</changefreq><priority>0.3</priority></url>
</urlset>"""), 200, {'Content-Type': 'application/xml'}

@app.route('/sitemap-aircraft-<int:page>.xml')
def sitemap_aircraft(page):
    limit = 50000
    offset = (page - 1) * limit
    conn_s = sql.connect(DB)
    rows = conn_s.execute(
        "SELECT registration FROM aircraft LIMIT ? OFFSET ?", 
        (limit, offset)
    ).fetchall()
    conn_s.close()
    
    urls = []
    for row in rows:
        reg = row[0]
        urls.append(f"<url><loc>https://panpanparts.com/aircraft/{reg}</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>")
    
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(urls) + """
</urlset>"""
    return xml, 200, {'Content-Type': 'application/xml'}

# Daglig backup scheduler
from apscheduler.schedulers.background import BackgroundScheduler
import boto3
import gzip
import psycopg2 as pg

def run_daily_backup():
    try:
        database_url = os.environ.get('DATABASE_URL')
        aws_key = os.environ.get('AWS_ACCESS_KEY_ID')
        aws_secret = os.environ.get('AWS_SECRET_ACCESS_KEY')
        bucket = os.environ.get('AWS_S3_BUCKET', 'panpanparts-backup')
        region = os.environ.get('AWS_REGION', 'eu-north-1')

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
        filename = f'/tmp/backup_{timestamp}.sql.gz'

        conn = pg.connect(database_url)
        cur = conn.cursor()
        tables = ['user', 'claimed_aircraft', 'aircraft_listing', 'part']

        with gzip.open(filename, 'wt') as f:
            for table in tables:
                cur.execute(f'SELECT * FROM "{table}"')
                rows = cur.fetchall()
                cols = [d[0] for d in cur.description]
                f.write(f'-- {table}: {len(rows)} rækker\n')
                f.write(f'-- Kolonner: {cols}\n')
                for row in rows:
                    f.write(str(row) + '\n')
                f.write('\n')

        cur.close()
        conn.close()

        s3 = boto3.client('s3', aws_access_key_id=aws_key, aws_secret_access_key=aws_secret, region_name=region)
        s3.upload_file(filename, bucket, f'backups/{filename.split("/")[-1]}')
        os.remove(filename)
        print(f'Backup fuldført: {filename}')
    except Exception as e:
        print(f'Backup fejl: {e}')

scheduler = BackgroundScheduler()
scheduler.add_job(run_daily_backup, 'cron', hour=2, minute=0)
scheduler.start()
