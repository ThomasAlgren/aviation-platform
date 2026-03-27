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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/parts">Parts</a>
            <div class="user-menu">
                <button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} ▾</button>
                <div class="dropdown">
                    <a href="/my-aircraft">My aircraft</a>
                    <a href="/my-profile">My profile</a>
                    <a href="/my-logbook">My logbook</a>
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

        <!-- Ret flydata -->
        <div class="card">
            <h3>Correct aircraft data
                <button class="edit-btn" onclick="document.getElementById('correct-form').classList.toggle('hidden')">Edit</button>
            </h3>
            <div class="date-item">
                <span class="date-label">Manufacturer</span>
                <span class="date-value">{{ aircraft.manufacturer or '—' }}</span>
            </div>
            <div class="date-item">
                <span class="date-label">Model</span>
                <span class="date-value">{{ aircraft.model or '—' }}</span>
            </div>
            <div class="date-item">
                <span class="date-label">Year</span>
                <span class="date-value">{{ aircraft.year or '—' }}</span>
            </div>
            <div id="correct-form" class="hidden" style="margin-top:16px">
                <p style="color:#666;font-size:13px;margin-bottom:12px">As the owner, you can correct incorrect data in our registry.</p>
                <form method="POST" action="/correct-aircraft/{{ aircraft.tail }}">
                    <input type="text" name="manufacturer" placeholder="Manufacturer (e.g. Cessna)" value="{{ aircraft.manufacturer or '' }}">
                    <input type="text" name="model" placeholder="Model (e.g. 172S Skyhawk)" value="{{ aircraft.model or '' }}">
                    <input type="text" name="year" placeholder="Year built" value="{{ aircraft.year or '' }}">
                    <button type="submit" class="save-btn">Save corrections</button>
                </form>
            </div>
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
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
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
    license_number = db.Column(db.String(100))
    license_type = db.Column(db.String(50))
    license_valid_until = db.Column(db.String(50))
    medical_class = db.Column(db.String(20))
    medical_valid_until = db.Column(db.String(50))
    total_flight_hours = db.Column(db.Float)
    ratings = db.Column(db.Text)
    license_document = db.Column(db.Text)
    medical_document = db.Column(db.Text)
    email_verified = db.Column(db.Boolean, default=False)
    verification_token = db.Column(db.String(100))
    reset_token = db.Column(db.String(100))
    reset_token_expires = db.Column(db.DateTime)
    
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
    coa_valid_until = db.Column(db.String(50))
    coa_document = db.Column(db.Text)
    registration_document = db.Column(db.Text)
    noise_document = db.Column(db.Text)
    radio_document = db.Column(db.Text)
    insurance_valid_until = db.Column(db.String(50))
    insurance_document = db.Column(db.Text)
    total_hours = db.Column(db.Float)
    engine_hours = db.Column(db.Float)
    last_service_date = db.Column(db.String(50))
    next_service_date = db.Column(db.String(50))
    notes = db.Column(db.Text)
    disputed = db.Column(db.Boolean, default=False)

class LogbookEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    flight_date = db.Column(db.String(20))
    dep_place = db.Column(db.String(10))
    arr_place = db.Column(db.String(10))
    off_block = db.Column(db.String(10))
    on_block = db.Column(db.String(10))
    aircraft_type = db.Column(db.String(100))
    registration = db.Column(db.String(20))
    pilot_in_command = db.Column(db.String(100))
    total_time = db.Column(db.String(10))
    night_time = db.Column(db.String(10))
    sep_vfr = db.Column(db.String(10))
    sep_ifr = db.Column(db.String(10))
    dual = db.Column(db.String(10))
    landings_day = db.Column(db.Integer)
    landings_night = db.Column(db.Integer)
    remarks = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PilotCertificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    cert_type = db.Column(db.String(100))
    cert_number = db.Column(db.String(100))
    issued_by = db.Column(db.String(200))
    issued_date = db.Column(db.String(50))
    valid_until = db.Column(db.String(50))
    document = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ClaimProtest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tail = db.Column(db.String(20))
    protester_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    protester_email = db.Column(db.String(200))
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
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
    fits_manufacturer = db.Column(db.String(200))
    fits_model = db.Column(db.String(200))
    fits_aircraft = db.Column(db.Text)

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
print("Connecting to PostgreSQL...")
import psycopg2
import psycopg2.extras

def get_pg_conn():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def search_aircraft(query, limit=50):
    conn = get_pg_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""
        SELECT * FROM aircraft 
        WHERE registration ILIKE %s 
        OR manufacturer ILIKE %s 
        OR model ILIKE %s
        LIMIT %s
    """, (f"%{query}%", f"%{query}%", f"%{query}%", limit))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_aircraft(registration):
    conn = get_pg_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM aircraft WHERE registration = %s", (registration,))
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
                    {% if p.fits_manufacturer %}<p style="color:#ff6b35;font-size:13px">Fits: {{ p.fits_manufacturer }} {{ p.fits_model }}</p>{% endif %}
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
        .verify-banner { background: rgba(255,193,7,0.15); border-bottom: 1px solid rgba(255,193,7,0.3); padding: 12px 40px; text-align: center; font-size: 14px; color: #ffc107; }
        .verify-banner a { color: #ff6b35; text-decoration: none; font-weight: 600; }
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
            <div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} ▾</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-logbook">My logbook</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div>
            {% else %}
            <a href="/login" class="primary">Log in</a>
            <a href="/register" class="primary">Sign up</a>
            {% endif %}
        </div>
    </div>
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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



        <div class="card">
            <h3>Own this aircraft?</h3>
            <p style="color:#666; font-size:14px; margin-bottom:16px">Claim your aircraft profile to add photos, flight hours, avionics and maintenance history.</p>
            <a href="/claim/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;margin-bottom:10px">Claim {{ aircraft.tail }} — it's free</a>
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
    welcome = request.args.get("welcome")
    if welcome and current_user.is_authenticated and not current_user.email_verified:
        flash("Welcome! Please check your email and verify your account.", "info")
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
        import psycopg2.extras
        conn = get_pg_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM aircraft WHERE 1=1"
        params = []
        if tail:
            t = tail.upper()
            query += " AND registration ILIKE %s"
            params.append(f'%{t}%')
        if model:
            query += " AND model ILIKE %s"
            params.append(f'%{model}%')
        if state:
            query += " AND state = %s"
            params.append(state)
        if year_from:
            query += " AND CAST(year AS INTEGER) >= %s"
            params.append(int(year_from))
        if year_to:
            query += " AND CAST(year AS INTEGER) <= %s"
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
        conn2 = get_pg_conn()
        cur2 = conn2.cursor()
        cur2.execute("SELECT COUNT(*) FROM aircraft")
        registry_count = cur2.fetchone()[0]
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
    model_query = aircraft["model"] if aircraft["model"] else ""
    if model_query:
        conn_stat = get_pg_conn()
        cur_stat = conn_stat.cursor()
        model_clean = model_query.replace("-", "")
        cur_stat.execute("SELECT COUNT(*) FROM aircraft WHERE REPLACE(model, '-', '') ILIKE %s", (model_clean,))
        total = cur_stat.fetchone()[0]
        cur_stat.execute("SELECT COUNT(*) FROM aircraft WHERE REPLACE(model, '-', '') ILIKE %s AND country = %s", (model_clean, "DK"))
        in_country = cur_stat.fetchone()[0]
        conn_stat.close()
    else:
        total = 0
        in_country = 0
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
        <div class="link" style="margin-top:10px"><a href="/forgot-password" style="color:#666;font-size:13px">Forgot password?</a></div>
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
                    import secrets
                    token = secrets.token_urlsafe(32)
                    user = User(name=name, email=email, country=country)
                    user.set_password(password)
                    user.verification_token = token
                    user.email_verified = False
                    db.session.add(user)
                    db.session.commit()
                    try:
                        from emails import send_verification_email
                        send_verification_email(email, name, token)
                    except Exception as e:
                        print("Email fejl:", e)
                    login_user(user)
                    return redirect('/?welcome=1')
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
    
    # Opret ClaimedAircraft record hvis den ikke findes
    existing = ClaimedAircraft.query.filter_by(tail=tail.upper()).first()
    if not existing:
        ca = ClaimedAircraft(
            user_id=current_user.id,
            tail=tail.upper()
        )
        db.session.add(ca)
        db.session.commit()
    
    return redirect('/my-aircraft/' + tail.upper())

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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/parts">Parts for sale</a>
            <div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} &#9660;</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-logbook">My logbook</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div>
        </div>
    </div>
    <div class="container">
        <h1>My <span>Aircraft</span></h1>
        <p class="sub">Aircraft you have claimed on PanPanParts</p>
        {% if aircraft %}
            {% for a in aircraft %}
            <a class="aircraft-card" href="/my-aircraft/{{ a.tail }}">
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/upload" class="btn">+ List a part</a>
            <div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} &#9660;</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-logbook">My logbook</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div>
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
        .search-bar { display: flex; gap: 10px; margin-bottom: 32px; }
        .search-bar input { flex: 1; padding: 14px 16px; border: 1px solid #333; border-radius: 10px; font-size: 16px; background: #1a1a2e; color: white; }
        .search-bar button { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: 600; }
        .ai-box { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.6; }
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
            {% if part.fits_manufacturer %}<div class="field"><span class="field-label">Fits aircraft</span><span style="color:#ff6b35">{{ part.fits_manufacturer }} {{ part.fits_model }}</span></div>{% endif %}
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav"><div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} ▾</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-logbook">My logbook</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div></div>
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
        .search-bar { display: flex; gap: 10px; margin-bottom: 32px; }
        .search-bar input { flex: 1; padding: 14px 16px; border: 1px solid #333; border-radius: 10px; font-size: 16px; background: #1a1a2e; color: white; }
        .search-bar button { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: 600; }
        .ai-box { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.6; }
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
        <form action="/" method="GET" class="search-bar">
            <input type="text" name="tail" placeholder="Search aircraft type, tail number..." value="{{ search }}">
            <button type="submit">Search</button>
        </form>
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
            conn_r = get_pg_conn()
            cur_r = conn_r.cursor()
            cur_r.execute("SELECT registration FROM aircraft WHERE registration = %s", (tail,))
            existing = cur_r.fetchone()
            if not existing:
                cur_r.execute("INSERT INTO aircraft (registration, manufacturer, model, year, serial, country, owner, city, state, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
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
        .search-bar { display: flex; gap: 10px; margin-bottom: 32px; }
        .search-bar input { flex: 1; padding: 14px 16px; border: 1px solid #333; border-radius: 10px; font-size: 16px; background: #1a1a2e; color: white; }
        .search-bar button { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: 600; }
        .ai-box { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.6; }
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
        .search-bar { display: flex; gap: 10px; margin-bottom: 32px; }
        .search-bar input { flex: 1; padding: 14px 16px; border: 1px solid #333; border-radius: 10px; font-size: 16px; background: #1a1a2e; color: white; }
        .search-bar button { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: 600; }
        .ai-box { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.6; }
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
        .search-bar { display: flex; gap: 10px; margin-bottom: 32px; }
        .search-bar input { flex: 1; padding: 14px 16px; border: 1px solid #333; border-radius: 10px; font-size: 16px; background: #1a1a2e; color: white; }
        .search-bar button { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: 600; }
        .ai-box { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.6; }
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
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
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
    conn_s = get_pg_conn()
    cur_s = conn_s.cursor()
    cur_s.execute("SELECT registration FROM aircraft LIMIT %s OFFSET %s", (limit, offset))
    rows = cur_s.fetchall()
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

@app.route('/my-aircraft/<tail>')
@login_required
def aircraft_cockpit(tail):
    import json
    from datetime import datetime, date
    
    # Tjek ejerskab
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return redirect('/my-aircraft')
    
    # Hent fly data
    r = get_aircraft(tail)
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v in ["nan", "None"] else v
    
    if r:
        aircraft = {
            "tail": tail,
            "model": s(r["model"]),
            "manufacturer": s(r["manufacturer"]),
            "year": s(r["year"]).split(".")[0],
            "country": s(r["country"]),
        }
    else:
        aircraft = {"tail": tail, "model": "", "manufacturer": "", "year": "", "country": ""}
    
    # Hent claimed data
    claimed = ClaimedAircraft.query.filter_by(tail=tail).first()
    
    # Beregn dage til ARC udløb
    arc_days = None
    if claimed and claimed.arc_valid_until:
        try:
            arc_date = datetime.strptime(claimed.arc_valid_until, '%Y-%m-%d').date()
            arc_days = (arc_date - date.today()).days
        except:
            pass
    
    return render_template_string(AIRCRAFT_COCKPIT_HTML, 
        aircraft=aircraft, 
        claimed=claimed,
        arc_days=arc_days,
        current_user=current_user)

@app.route('/my-aircraft/<tail>/update', methods=['POST'])
@login_required
def aircraft_cockpit_update(tail):
    import json
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return redirect('/my-aircraft')
    
    claimed = ClaimedAircraft.query.filter_by(tail=tail).first()
    if not claimed:
        return redirect('/my-aircraft')
    
    # Opdater felter
    fields = ['arc_valid_until', 'coa_valid_until', 'insurance_valid_until', 
              'last_service_date', 'next_service_date', 'total_hours', 
              'engine_hours', 'notes']
    
    for field in fields:
        val = request.form.get(field)
        if val is not None and val != '':
            setattr(claimed, field, val)
    
    db.session.commit()
    return redirect(f'/my-aircraft/{tail}')

@app.route('/my-aircraft/<tail>/upload-doc', methods=['POST'])
@login_required
def aircraft_upload_doc(tail):
    import json
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return json.dumps({'ok': False})
    
    claimed = ClaimedAircraft.query.filter_by(tail=tail).first()
    if not claimed:
        return json.dumps({'ok': False})
    
    data = request.get_json()
    doc_type = data.get('doc_type')
    doc_data = data.get('data', '')[:5000]
    
    doc_map = {
        'arc': 'arc_document',
        'coa': 'coa_document',
        'registration': 'registration_document',
        'noise': 'noise_document',
        'radio': 'radio_document',
        'insurance': 'insurance_document',
    }
    
    if doc_type in doc_map:
        setattr(claimed, doc_map[doc_type], doc_data)
        db.session.commit()
        return json.dumps({'ok': True})
    
    return json.dumps({'ok': False})

@app.route('/my-profile', methods=['GET', 'POST'])
@login_required
def my_profile():
    from datetime import datetime, date
    
    if request.method == 'POST':
        fields = ['license_number', 'license_type', 'license_valid_until',
                  'medical_class', 'medical_valid_until', 'total_flight_hours', 'ratings']
        for field in fields:
            val = request.form.get(field)
            if val is not None:
                setattr(current_user, field, val)
        db.session.commit()
        return redirect('/my-profile')
    
    # Beregn dage til udløb
    medical_days = None
    if current_user.medical_valid_until:
        try:
            med_date = datetime.strptime(current_user.medical_valid_until, '%Y-%m-%d').date()
            medical_days = (med_date - date.today()).days
        except:
            pass

    license_days = None
    if current_user.license_valid_until:
        try:
            lic_date = datetime.strptime(current_user.license_valid_until, '%Y-%m-%d').date()
            license_days = (lic_date - date.today()).days
        except:
            pass

    # Hent certifikater med dage til udløb
    from datetime import date
    raw_certs = PilotCertificate.query.filter_by(user_id=current_user.id).order_by(PilotCertificate.created_at).all()
    certificates = []
    for cert in raw_certs:
        days_left = None
        if cert.valid_until:
            try:
                exp = datetime.strptime(cert.valid_until, '%Y-%m-%d').date()
                days_left = (exp - date.today()).days
            except:
                pass
        certificates.append({
            'id': cert.id,
            'cert_type': cert.cert_type,
            'cert_number': cert.cert_number,
            'issued_by': cert.issued_by,
            'valid_until': cert.valid_until,
            'days_left': days_left
        })

    return render_template_string(MY_PROFILE_HTML,
        current_user=current_user,
        medical_days=medical_days,
        license_days=license_days,
        certificates=certificates)

MY_PROFILE_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>My Profile - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 700px; margin: 40px auto; padding: 0 20px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }
        .hero { background: linear-gradient(135deg, #1a1a2e, #16213e); border-radius: 16px; padding: 32px; margin-bottom: 24px; border: 1px solid #2a2a3e; }
        .hero-name { font-size: 36px; font-weight: 700; }
        .hero-sub { color: #666; margin-top: 6px; font-size: 15px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .date-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #2a2a3e; }
        .date-item:last-child { border-bottom: none; }
        .date-label { color: #aaa; font-size: 14px; }
        .date-value { font-size: 14px; font-weight: 600; }
        .date-ok { color: #4caf50; }
        .date-warn { color: #ffc107; }
        .date-alert { color: #ff6b35; }
        .date-missing { color: #444; font-style: italic; font-weight: 400; }
        .status-badge { padding: 8px 20px; border-radius: 20px; font-size: 14px; font-weight: 600; float: right; }
        .status-ok { background: rgba(76,175,80,0.2); color: #4caf50; border: 1px solid rgba(76,175,80,0.3); }
        .status-warn { background: rgba(255,193,7,0.2); color: #ffc107; border: 1px solid rgba(255,193,7,0.3); }
        .status-alert { background: rgba(255,107,53,0.2); color: #ff6b35; border: 1px solid rgba(255,107,53,0.3); }
        .edit-btn { background: transparent; border: 1px solid #333; color: #aaa; padding: 6px 14px; border-radius: 6px; font-size: 12px; cursor: pointer; float: right; margin-top: -4px; }
        .edit-btn:hover { border-color: #ff6b35; color: #ff6b35; }
        .hidden { display: none; }
        input[type=text], input[type=date], input[type=number], select { width: 100%; padding: 10px 12px; border: 1px solid #333; border-radius: 8px; font-size: 14px; margin-bottom: 10px; background: #0d0d1a; color: white; }
        .save-btn { background: #ff6b35; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 14px; cursor: pointer; font-weight: 600; width: 100%; margin-top: 4px; }
        .hours-value { font-size: 48px; font-weight: 700; color: #ff6b35; }
        .hours-label { font-size: 13px; color: #666; margin-top: 4px; }
        .user-menu { position: relative; margin-left: 8px; }
        .user-btn { background: #1a1a2e; color: #aaa; border: 1px solid #333; padding: 8px 16px; border-radius: 8px; font-size: 14px; cursor: pointer; }
        .dropdown { display: none; position: absolute; right: 0; top: 44px; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 8px; min-width: 140px; z-index: 100; }
        .dropdown a { display: block; padding: 12px 16px; color: #aaa; text-decoration: none; font-size: 14px; }
        .dropdown a:hover { color: white; background: #2a2a3e; }
        .dropdown.open { display: block; }
        label { font-size: 12px; color: #666; margin-bottom: 4px; display: block; }
    </style>
</head>
<body>
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/parts">Parts</a>
            <div class="user-menu">
                <button class="user-btn" onclick="this.nextElementSibling.classList.toggle('open')">{{ current_user.name }} ▾</button>
                <div class="dropdown">
                    <a href="/my-aircraft">My aircraft</a>
                    <a href="/my-profile">My profile</a>
                    <a href="/my-logbook">My logbook</a>
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
                <div class="hero-name">{{ current_user.name }}</div>
                <div class="hero-sub">
                    {{ current_user.license_type or 'Pilot' }}
                    {% if current_user.license_number %} · {{ current_user.license_number }}{% endif %}
                    {% if current_user.country %} · {{ current_user.country }}{% endif %}
                </div>
            </div>
        </div>

        <!-- Kritiske datoer -->
        <div class="card">
            <h3>Critical dates
                <button class="edit-btn" onclick="document.getElementById('dates-form').classList.toggle('hidden')">Edit</button>
            </h3>

            <div class="date-item">
                <span class="date-label">Medical valid until</span>
                <span class="date-value {% if medical_days is not none %}{% if medical_days < 0 %}date-alert{% elif medical_days < 60 %}date-warn{% else %}date-ok{% endif %}{% else %}date-missing{% endif %}">
                    {% if current_user.medical_valid_until %}
                        {{ current_user.medical_valid_until }}
                        {% if medical_days is not none %}
                            {% if medical_days < 0 %} — EXPIRED{% elif medical_days < 60 %} — {{ medical_days }} days left{% endif %}
                        {% endif %}
                    {% else %}
                        Not registered
                    {% endif %}
                </span>
            </div>

            <div class="date-item">
                <span class="date-label">Medical class</span>
                <span class="date-value {% if current_user.medical_class %}date-ok{% else %}date-missing{% endif %}">
                    {{ current_user.medical_class or 'Not registered' }}
                </span>
            </div>

            <div class="date-item">
                <span class="date-label">License valid until</span>
                <span class="date-value {% if license_days is not none %}{% if license_days < 0 %}date-alert{% elif license_days < 60 %}date-warn{% else %}date-ok{% endif %}{% else %}date-missing{% endif %}">
                    {% if current_user.license_valid_until %}
                        {{ current_user.license_valid_until }}
                        {% if license_days is not none %}
                            {% if license_days < 0 %} — EXPIRED{% elif license_days < 60 %} — {{ license_days }} days left{% endif %}
                        {% endif %}
                    {% else %}
                        Not registered
                    {% endif %}
                </span>
            </div>

            <div class="date-item">
                <span class="date-label">Ratings</span>
                <span class="date-value {% if current_user.ratings %}date-ok{% else %}date-missing{% endif %}">
                    {{ current_user.ratings or 'Not registered' }}
                </span>
            </div>

            <!-- Edit form -->
            <div id="dates-form" class="hidden" style="margin-top:16px">
                <form method="POST" action="/my-profile">
                    <label>License type</label>
                    <select name="license_type">
                        <option value="">Select...</option>
                        <option value="PPL" {% if current_user.license_type == 'PPL' %}selected{% endif %}>PPL — Private Pilot License</option>
                        <option value="CPL" {% if current_user.license_type == 'CPL' %}selected{% endif %}>CPL — Commercial Pilot License</option>
                        <option value="ATPL" {% if current_user.license_type == 'ATPL' %}selected{% endif %}>ATPL — Airline Transport Pilot License</option>
                        <option value="SPL" {% if current_user.license_type == 'SPL' %}selected{% endif %}>SPL — Student Pilot License</option>
                    </select>
                    <label>License number</label>
                    <input type="text" name="license_number" placeholder="e.g. DK.FCL.2026.PPL.12345" value="{{ current_user.license_number or '' }}">
                    <label>License valid until</label>
                    <input type="text" name="license_valid_until" placeholder="YYYY-MM-DD" value="{{ current_user.license_valid_until or '' }}">
                    <label>Medical class</label>
                    <select name="medical_class">
                        <option value="">Select...</option>
                        <option value="Class 1" {% if current_user.medical_class == 'Class 1' %}selected{% endif %}>Class 1 — Commercial</option>
                        <option value="Class 2" {% if current_user.medical_class == 'Class 2' %}selected{% endif %}>Class 2 — Private</option>
                        <option value="LAPL" {% if current_user.medical_class == 'LAPL' %}selected{% endif %}>LAPL Medical</option>
                    </select>
                    <label>Medical valid until</label>
                    <input type="text" name="medical_valid_until" placeholder="YYYY-MM-DD" value="{{ current_user.medical_valid_until or '' }}">
                    <label>Ratings (e.g. IR, Night, MEP, SEP)</label>
                    <input type="text" name="ratings" placeholder="e.g. SEP, Night" value="{{ current_user.ratings or '' }}">
                    <button type="submit" class="save-btn">Save profile</button>
                </form>
            </div>
        </div>

        <!-- Flyvetimer -->
        <div class="card">
            <h3>Flight hours
                <button class="edit-btn" onclick="document.getElementById('hours-form').classList.toggle('hidden')">Edit</button>
            </h3>
            <div class="hours-value">{{ current_user.total_flight_hours or '0' }}</div>
            <div class="hours-label">Total flight hours</div>

            <div id="hours-form" class="hidden" style="margin-top:16px">
                <form method="POST" action="/my-profile">
                    <label>Total flight hours</label>
                    <input type="number" name="total_flight_hours" placeholder="Total hours in logbook" value="{{ current_user.total_flight_hours or '' }}" step="0.1">
                    <button type="submit" class="save-btn">Save hours</button>
                </form>
            </div>
        <!-- Certifikater -->
        <div class="card">
            <h3>Certificates & Ratings</h3>
            {% if certificates %}
            {% for cert in certificates %}
            <div class="date-item" onclick="showCert({{ cert.id }})" style="cursor:pointer">
                <div>
                    <div style="font-size:14px;font-weight:600">{{ cert.cert_type }}</div>
                    {% if cert.cert_number %}<div style="font-size:12px;color:#666">{{ cert.cert_number }}</div>{% endif %}
                    {% if cert.issued_by %}<div style="font-size:12px;color:#666">{{ cert.issued_by }}</div>{% endif %}
                </div>
                <div style="text-align:right">
                    {% if cert.valid_until %}
                    <div class="date-value {% if cert.days_left is not none %}{% if cert.days_left < 0 %}date-alert{% elif cert.days_left < 60 %}date-warn{% else %}date-ok{% endif %}{% endif %}">
                        {{ cert.valid_until }}
                        {% if cert.days_left is not none and cert.days_left < 60 %}
                            {% if cert.days_left < 0 %} — EXPIRED{% else %} — {{ cert.days_left }} days{% endif %}
                        {% endif %}
                    </div>
                    {% else %}
                    <div style="color:#444;font-size:13px">No expiry</div>
                    {% endif %}
                    <a href="/delete-certificate/{{ cert.id }}" style="color:#444;font-size:11px;text-decoration:none" onclick="return confirm('Delete this certificate?')">remove</a>
                </div>
            </div>
            {% endfor %}
            {% else %}
            <p style="color:#444;font-size:14px;padding:12px 0">No certificates added yet.</p>
            {% endif %}

            <div style="margin-top:16px;border-top:1px solid #2a2a3e;padding-top:16px">
                <button class="edit-btn" style="float:none;margin:0 0 12px 0" onclick="document.getElementById('cert-form').classList.toggle('hidden')">+ Add certificate</button>
                <div id="cert-form" class="hidden">
                    <form method="POST" action="/add-certificate">
                        <label>Certificate type</label>
                        <select name="cert_type">
                            <option value="">Select type...</option>
                            <optgroup label="Licences">
                            <option>LAPL(A) — Light Aircraft Pilot Licence</option>
                            <option>PPL(A) — Private Pilot Licence</option>
                            <option>CPL(A) — Commercial Pilot Licence</option>
                            <option>ATPL(A) — Airline Transport Pilot Licence</option>
                            <option>MPL — Multi-crew Pilot Licence</option>
                            <option>PPL(H) — Helicopter Pilot Licence</option>
                            <option>SPL — Sailplane Pilot Licence</option>
                            <option>BPL — Balloon Pilot Licence</option>
                            <option>FAA PPL</option>
                            <option>FAA CPL</option>
                            <option>FAA ATPL</option>
                            </optgroup>
                            <optgroup label="Theory Exams">
                            <option>PPL Theory — Passed</option>
                            <option>ATPL Theory — Passed (Frozen)</option>
                            </optgroup>
                            <optgroup label="Ratings">
                            <option>IR(A) — Instrument Rating</option>
                            <option>EIR — En-route Instrument Rating</option>
                            <option>Night Rating</option>
                            <option>SEP(land) — Single Engine Piston</option>
                            <option>MEP(land) — Multi Engine Piston</option>
                            <option>TMG — Touring Motor Glider</option>
                            <option>HPA — High Performance Aircraft</option>
                            <option>Tailwheel Endorsement</option>
                            </optgroup>
                            <optgroup label="Medical">
                            <option>Medical Class 1</option>
                            <option>Medical Class 2</option>
                            <option>LAPL Medical</option>
                            </optgroup>
                            <optgroup label="Radio">
                            <option>Radio Certificate — National</option>
                            <option>Radio Certificate — ICAO/International (English)</option>
                            <option>ICAO English Language Proficiency</option>
                            </optgroup>
                            <optgroup label="Instructor">
                            <option>FI(A) — Flight Instructor</option>
                            <option>IRI(A) — Instrument Rating Instructor</option>
                            <option>CRI — Class Rating Instructor</option>
                            </optgroup>
                            <option>Other</option>
                        </select>
                        <label>Certificate number (optional)</label>
                        <input type="text" name="cert_number" placeholder="e.g. DK.FCL.2026.PPL.12345">
                        <label>Issued by (optional)</label>
                        <input type="text" name="issued_by" placeholder="e.g. Trafikstyrelsen, FAA, CAA">
                        <label>Issue date (optional)</label>
                        <input type="text" name="issued_date" placeholder="YYYY-MM-DD">
                        <label>Valid until (leave blank if no expiry)</label>
                        <input type="text" name="valid_until" placeholder="YYYY-MM-DD">
                        <label>Upload certificate photo (optional — AI will read dates automatically)</label>
                        <input type="file" id="cert-photo" accept="image/*" capture="environment" onchange="loadCertPhoto(this)" style="margin-bottom:10px">
                        <input type="hidden" name="document" id="cert-doc-data">
                        <img id="cert-preview" style="max-width:100%;border-radius:8px;margin-bottom:10px;display:none">
                        <button type="submit" class="save-btn">Add certificate</button>
                    </form>
                    <script>
                    function loadCertPhoto(input) {
                        var file = input.files[0];
                        if (!file) return;
                        var reader = new FileReader();
                        reader.onload = function(e) {
                            var img = new Image();
                            img.onload = function() {
                                var canvas = document.createElement("canvas");
                                var maxSize = 1200;
                                var w = img.width, h = img.height;
                                if (w > maxSize || h > maxSize) {
                                    if (w > h) { h = h * maxSize / w; w = maxSize; }
                                    else { w = w * maxSize / h; h = maxSize; }
                                }
                                canvas.width = w;
                                canvas.height = h;
                                canvas.getContext("2d").drawImage(img, 0, 0, w, h);
                                var compressed = canvas.toDataURL("image/jpeg", 0.7);
                                document.getElementById("cert-preview").src = compressed;
                                document.getElementById("cert-preview").style.display = "block";
                                document.getElementById("cert-doc-data").value = compressed.split(",")[1];
                            };
                            img.src = e.target.result;
                        };
                        reader.readAsDataURL(file);
                    }
                    </script>
                </div>
            </div>
        </div>
    <!-- Certificate modal -->
    <div id="cert-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:1000;overflow-y:auto">
        <div style="max-width:500px;margin:40px auto;background:#1a1a2e;border-radius:12px;padding:28px;position:relative">
            <button onclick="document.getElementById('cert-modal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;color:#aaa;font-size:20px;cursor:pointer">✕</button>
            <h3 id="modal-type" style="margin-bottom:16px;font-size:18px"></h3>
            <div id="modal-details" style="color:#aaa;font-size:14px;margin-bottom:16px"></div>
            <img id="modal-img" style="width:100%;border-radius:8px;display:none">
        </div>
    </div>

    <script>
    function showCert(id) {
        fetch('/certificate/' + id)
            .then(r => r.json())
            .then(cert => {
                document.getElementById('modal-type').textContent = cert.cert_type;
                var details = '';
                if (cert.cert_number) details += '<div>Number: ' + cert.cert_number + '</div>';
                if (cert.issued_by) details += '<div>Issued by: ' + cert.issued_by + '</div>';
                if (cert.issued_date) details += '<div>Issue date: ' + cert.issued_date + '</div>';
                if (cert.valid_until) details += '<div>Valid until: <strong style="color:#ff6b35">' + cert.valid_until + '</strong></div>';
                document.getElementById('modal-details').innerHTML = details;
                if (cert.document) {
                    document.getElementById('modal-img').src = 'data:image/jpeg;base64,' + cert.document;
                    document.getElementById('modal-img').style.display = 'block';
                } else {
                    document.getElementById('modal-img').style.display = 'none';
                }
                document.getElementById('cert-modal').style.display = 'block';
            });
    }
    </script>
    </div>
</body>
</html>"""

# Email verificering og password reset
import secrets
from emails import send_verification_email, send_password_reset_email

@app.route('/verify-email/<token>')
def verify_email(token):
    user = User.query.filter_by(verification_token=token).first()
    if not user:
        return render_template_string("""
        <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
        <h2 style='color:#ff6b35'>Invalid or expired link</h2>
        <a href='/' style='color:#4a9eff'>Go to PanPanParts</a>
        </body></html>""")
    user.email_verified = True
    user.verification_token = None
    db.session.commit()
    return render_template_string("""
    <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
    <h2 style='color:#4caf50'>✓ Email verified!</h2>
    <p style='color:#aaa;margin:16px 0'>Your account is now active.</p>
    <a href='/login' style='background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600'>Log in</a>
    </body></html>""")

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        user = User.query.filter_by(email=email).first()
        if user:
            token = secrets.token_urlsafe(32)
            user.reset_token = token
            user.reset_token_expires = datetime.utcnow().replace(microsecond=0)
            db.session.commit()
            try:
                send_password_reset_email(user.email, user.name, token)
            except Exception as e:
                print("Email fejl:", e)
        return render_template_string("""
        <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
        <h2>Check your email</h2>
        <p style='color:#aaa'>If an account exists, we sent a reset link.</p>
        <a href='/login' style='color:#ff6b35'>Back to login</a>
        </body></html>""")
    return render_template_string("""
    <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
    <h2>Forgot password</h2>
    <form method='POST' style='margin-top:24px'>
        <input type='email' name='email' placeholder='Your email address' required
            style='padding:12px 16px;border:1px solid #333;border-radius:8px;background:#1a1a2e;color:white;font-size:15px;width:300px'>
        <br><br>
        <button type='submit' style='background:#ff6b35;color:white;border:none;padding:14px 28px;border-radius:8px;font-size:16px;cursor:pointer;font-weight:600'>
            Send reset link
        </button>
    </form>
    <br><a href='/login' style='color:#aaa;font-size:14px'>Back to login</a>
    </body></html>""")

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()
    if not user:
        return render_template_string("""
        <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
        <h2 style='color:#ff6b35'>Invalid or expired link</h2>
        <a href='/forgot-password' style='color:#4a9eff'>Try again</a>
        </body></html>""")
    if request.method == 'POST':
        password = request.form.get('password', '')
        if len(password) < 8:
            flash('Password must be at least 8 characters')
            return redirect(f'/reset-password/{token}')
        user.set_password(password)
        user.reset_token = None
        user.reset_token_expires = None
        db.session.commit()
        return render_template_string("""
        <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
        <h2 style='color:#4caf50'>✓ Password updated!</h2>
        <a href='/login' style='background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600'>Log in</a>
        </body></html>""")
    return render_template_string("""
    <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
    <h2>Choose new password</h2>
    <form method='POST' style='margin-top:24px'>
        <input type='password' name='password' placeholder='New password (min 8 characters)' required
            style='padding:12px 16px;border:1px solid #333;border-radius:8px;background:#1a1a2e;color:white;font-size:15px;width:300px'>
        <br><br>
        <button type='submit' style='background:#ff6b35;color:white;border:none;padding:14px 28px;border-radius:8px;font-size:16px;cursor:pointer;font-weight:600'>
            Save new password
        </button>
    </form>
    </body></html>""")

@app.route('/resend-verification')
@login_required
def resend_verification():
    if current_user.email_verified:
        return redirect('/')
    import secrets
    token = secrets.token_urlsafe(32)
    current_user.verification_token = token
    db.session.commit()
    try:
        from emails import send_verification_email
        send_verification_email(current_user.email, current_user.name, token)
        flash("Verification email sent!", "info")
    except Exception as e:
        print("Email fejl:", e)
        flash("Could not send email. Please try again.", "error")
    return redirect('/')

@app.route('/protest-claim/<tail>', methods=['GET', 'POST'])
@login_required
def protest_claim(tail):
    claimed = ClaimedAircraft.query.filter_by(tail=tail).first()
    if not claimed:
        return redirect(f'/aircraft/{tail}')
    
    if request.method == 'POST':
        reason = request.form.get('reason', '').strip()
        if reason:
            protest = ClaimProtest(
                tail=tail,
                protester_id=current_user.id,
                protester_email=current_user.email,
                reason=reason
            )
            db.session.add(protest)
            claimed.disputed = True
            db.session.commit()
            
            # Send email til thomas
            try:
                import resend
                resend.api_key = os.environ.get("RESEND_API_KEY")
                resend.Emails.send({
                    "from": "PanPanParts <noreply@panpanparts.com>",
                    "to": "thomas@panpanparts.com",
                    "subject": f"Claim protest: {tail}",
                    "html": f"""
                    <h2>Claim protest received</h2>
                    <p><strong>Tail:</strong> {tail}</p>
                    <p><strong>Protester:</strong> {current_user.name} ({current_user.email})</p>
                    <p><strong>Reason:</strong> {reason}</p>
                    """
                })
            except Exception as e:
                print("Email fejl:", e)
            
            return render_template_string("""
            <html><body style='font-family:sans-serif;text-align:center;padding:80px;background:#0d0d1a;color:white'>
            <h2 style='color:#ffc107'>⚠ Protest received</h2>
            <p style='color:#aaa;margin:16px 0'>We have received your protest for {{ tail }}.<br>We will review it and contact you within 48 hours.</p>
            <a href='/' style='color:#ff6b35'>Back to PanPanParts</a>
            </body></html>""", tail=tail)
    
    return render_template_string("""
    <html><body style='font-family:sans-serif;background:#0d0d1a;color:white;padding:40px'>
    <div style='max-width:500px;margin:0 auto'>
        <h2>Protest claim for {{ tail }}</h2>
        <p style='color:#aaa;margin:16px 0'>If you believe this aircraft is incorrectly claimed, please explain why.</p>
        <form method='POST'>
            <textarea name='reason' required placeholder='Explain why you believe this claim is incorrect...'
                style='width:100%;height:120px;padding:12px;border:1px solid #333;border-radius:8px;background:#1a1a2e;color:white;font-size:14px;margin-bottom:16px'></textarea>
            <button type='submit' style='background:#ff6b35;color:white;border:none;padding:14px 28px;border-radius:8px;font-size:16px;cursor:pointer;font-weight:600;width:100%'>
                Submit protest
            </button>
        </form>
        <br><a href='/' style='color:#aaa;font-size:14px'>Cancel</a>
    </div>
    </body></html>""", tail=tail)

@app.route('/correct-aircraft/<tail>', methods=['POST'])
@login_required  
def correct_aircraft(tail):
    import json
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return redirect('/')
    
    manufacturer = request.form.get('manufacturer', '').strip()
    model = request.form.get('model', '').strip()
    year = request.form.get('year', '').strip()
    
    if any([manufacturer, model, year]):
        conn = get_pg_conn()
        cur = conn.cursor()
        if manufacturer:
            cur.execute("UPDATE aircraft SET manufacturer = %s WHERE registration = %s", (manufacturer, tail))
        if model:
            cur.execute("UPDATE aircraft SET model = %s WHERE registration = %s", (model, tail))
        if year:
            cur.execute("UPDATE aircraft SET year = %s WHERE registration = %s", (year, tail))
        conn.commit()
        conn.close()
    
    return redirect(f'/my-aircraft/{tail}')

@app.route('/add-certificate', methods=['POST'])
@login_required
def add_certificate():
    cert_type = request.form.get('cert_type', '').strip()
    if not cert_type:
        return redirect('/my-profile')
    
    cert_number = request.form.get('cert_number', '').strip() or None
    issued_by = request.form.get('issued_by', '').strip() or None
    issued_date = request.form.get('issued_date', '').strip() or None
    valid_until = request.form.get('valid_until', '').strip() or None
    document = request.form.get('document', '').strip() or None

    # AI analyse hvis foto uploaded
    if document and not valid_until:
        try:
            import anthropic as ac
            import json
            client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=300,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": document}},
                        {"type": "text", "text": """Analyze this pilot certificate/licence image. Extract:
Respond ONLY with JSON:
{
  "cert_number": "certificate number or null",
  "issued_by": "issuing authority or null",
  "issued_date": "YYYY-MM-DD or null",
  "valid_until": "YYYY-MM-DD or null"
}"""}
                    ]
                }]
            )
            text = response.content[0].text
            clean = text.replace("```json", "").replace("```", "").strip()
            result = json.loads(clean)
            cert_number = cert_number or result.get("cert_number")
            issued_by = issued_by or result.get("issued_by")
            issued_date = issued_date or result.get("issued_date")
            valid_until = valid_until or result.get("valid_until")
        except Exception as e:
            print("AI fejl:", e)

    cert = PilotCertificate(
        user_id=current_user.id,
        cert_type=cert_type,
        cert_number=cert_number,
        issued_by=issued_by,
        issued_date=issued_date,
        valid_until=valid_until,
        document=document[:500] if document else None,
    )
    db.session.add(cert)
    db.session.commit()
    return redirect('/my-profile')

@app.route('/delete-certificate/<int:cert_id>')
@login_required
def delete_certificate(cert_id):
    cert = PilotCertificate.query.get_or_404(cert_id)
    if cert.user_id == current_user.id:
        db.session.delete(cert)
        db.session.commit()
    return redirect('/my-profile')

@app.route('/certificate/<int:cert_id>')
@login_required
def get_certificate(cert_id):
    cert = PilotCertificate.query.get_or_404(cert_id)
    if cert.user_id != current_user.id:
        return json.dumps({'error': 'Not authorized'}), 403
    import json
    return json.dumps({
        'cert_type': cert.cert_type,
        'cert_number': cert.cert_number or '',
        'issued_by': cert.issued_by or '',
        'issued_date': cert.issued_date or '',
        'valid_until': cert.valid_until or '',
        'document': cert.document or ''
    })

@app.route('/my-logbook')
@login_required
def my_logbook():
    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.id.asc()).all()
    
    total_minutes = 0
    for e in entries:
        if e.total_time and e.total_time not in ['—', '-', '']:
            try:
                parts = e.total_time.replace(":", " ").replace(".", " ").split()
                if len(parts) == 2:
                    total_minutes += int(parts[0]) * 60 + int(parts[1])
            except:
                pass
    total_hours = total_minutes // 60
    total_mins = total_minutes % 60
    total_str = f"{total_hours}:{total_mins:02d}" if total_minutes > 0 else "0:00"
    
    return render_template_string(LOGBOOK_HTML, entries=entries, current_user=current_user, total_time=total_str, total_flights=len(entries))

@app.route('/logbook-scan', methods=['POST'])
@login_required
def logbook_scan():
    import anthropic as ac
    import json
    data = request.get_json()
    left_page = data.get('left_page')
    right_page = data.get('right_page')
    
    # Hent brugerens tidligere registreringer som kontekst
    prev_entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.created_at.desc()).limit(20).all()
    known_regs = list(set([e.registration for e in prev_entries if e.registration]))
    known_types = list(set([e.aircraft_type for e in prev_entries if e.aircraft_type]))
    
    content_parts = []
    if left_page:
        content_parts.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": left_page}})
    if right_page:
        content_parts.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": right_page}})
    
    context_hint = ""
    if known_regs:
        context_hint = f"\n\nThis pilot has previously flown: {', '.join(known_regs)}. Use these as reference when unsure about a registration."

    content_parts.append({"type": "text", "text": f"""These are pages from a pilot logbook. Extract all flight entries carefully.

IMPORTANT:
- Dates are ALWAYS in DD/MM/YY format (European). Day first, then month, then 2-digit year.
- Examples: 02/10/25 = 02/10/2025, 20/01/26 = 20/01/2026, 04/03/26 = 04/03/2026.
- NEVER interpret dates as MM/DD/YY — this is a European logbook.
- Aircraft registrations: OY-XXX (Denmark), LN-XXX (Norway), N12345 (USA). 
- Danish registrations are always OY- followed by 3 letters. Read each letter carefully.
- Times are H:MM format. A space between digits means colon e.g. "1 55" = 1:55.
- Only extract rows with actual flight data — skip empty rows.
- CRITICAL: Preserve the EXACT order of rows as they appear on the page. Do NOT sort or reorder entries.
- Read rows strictly from top to bottom. Row 1 in the logbook must be row 1 in your output.
- Each row belongs to a specific line — do not mix data between rows.
- At the bottom of the page there are totals: "Total This Page", "Total Previous Pages", "Total".
- Read these totals and include them in a "page_totals" field in your response.
- Calculate your own total of all flight times and compare with "Total This Page".
- If they differ, add a "validation_warning" field explaining the discrepancy.{context_hint}

Respond ONLY with a JSON object:
{{
  "flights": [{{
  "flight_date": "DD/MM/YYYY",
  "dep_place": "ICAO code",
  "arr_place": "ICAO code",
  "off_block": "HH:MM or null",
  "on_block": "HH:MM or null",
  "aircraft_type": "type as written",
  "registration": "e.g. OY-BJM",
  "pilot_in_command": "name or null",
  "total_time": "H:MM",
  "night_time": "H:MM or null",
  "sep_vfr": "H:MM or null",
  "dual": "H:MM or null",
  "landings_day": number or null,
  "landings_night": number or null,
  "remarks": "any remarks or null"
}}]"""})

    client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": content_parts}]
    )
    
    text = response.content[0].text
    clean = text.replace("```json", "").replace("```", "").strip()
    parsed = json.loads(clean)
    
    # Håndter både gammelt array format og nyt objekt format
    if isinstance(parsed, list):
        flights = parsed
        validation_warning = None
        page_totals = None
    else:
        flights = parsed.get("flights", [])
        validation_warning = parsed.get("validation_warning")
        page_totals = parsed.get("page_totals")
    
    # Gem flyvninger
    saved = 0
    for f in flights:
        entry = LogbookEntry(
            user_id=current_user.id,
            flight_date=f.get('flight_date'),
            dep_place=f.get('dep_place'),
            arr_place=f.get('arr_place'),
            off_block=f.get('off_block'),
            on_block=f.get('on_block'),
            aircraft_type=f.get('aircraft_type'),
            registration=f.get('registration'),
            pilot_in_command=f.get('pilot_in_command'),
            total_time=f.get('total_time'),
            night_time=f.get('night_time'),
            sep_vfr=f.get('sep_vfr'),
            dual=f.get('dual'),
            landings_day=f.get('landings_day'),
            landings_night=f.get('landings_night'),
            remarks=f.get('remarks'),
        )
        db.session.add(entry)
        saved += 1
    
    db.session.commit()
    return json.dumps({'ok': True, 'saved': saved, 'flights': flights, 'validation_warning': validation_warning, 'page_totals': page_totals})

@app.route('/delete-logbook-entry/<int:entry_id>')
@login_required
def delete_logbook_entry(entry_id):
    entry = LogbookEntry.query.get_or_404(entry_id)
    if entry.user_id == current_user.id:
        db.session.delete(entry)
        db.session.commit()
    return redirect('/my-logbook')

LOGBOOK_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>My Logbook - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 16px; }
        .container { max-width: 1000px; margin: 40px auto; padding: 0 20px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .upload-row { display: flex; gap: 12px; margin-bottom: 16px; }
        .upload-box { flex: 1; border: 2px dashed #333; border-radius: 8px; padding: 20px; text-align: center; cursor: pointer; color: #666; font-size: 13px; position: relative; }
        .upload-box:hover { border-color: #ff6b35; color: #ff6b35; }
        .upload-box img { width: 100%; height: 120px; object-fit: cover; border-radius: 6px; display: none; }
        input[type=file] { display: none; }
        .scan-btn { background: #ff6b35; color: white; border: none; padding: 14px 28px; border-radius: 8px; font-size: 15px; cursor: pointer; font-weight: 600; width: 100%; }
        .scan-btn:disabled { background: #444; cursor: not-allowed; }
        .status { background: #0d0d1a; border-radius: 8px; padding: 16px; margin-top: 12px; color: #aaa; font-size: 14px; display: none; border: 1px solid #2a2a3e; }
        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        @media (max-width: 600px) {
            table { font-size: 11px; }
            th, td { padding: 6px 4px; }
            .container { padding: 0 10px; }
            .header { padding: 16px 20px; }
            th:nth-child(4), td:nth-child(4) { display: none; }
            th:nth-child(7), td:nth-child(7) { display: none; }
        }
        th { text-align: left; padding: 10px 8px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; }
        td { padding: 10px 8px; border-bottom: 1px solid #1a1a2e; }
        tr:hover td { background: #1a1a2e; }
        .total-row { color: #ff6b35; font-weight: 600; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }
        .delete-btn:hover { color: #ff6b35; }
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
                    <a href="/my-logbook">My logbook</a>
                    <a href="/my-listings">My listings</a>
                    <a href="/logout">Log out</a>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <a href="/my-profile" class="back">← My profile</a>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px">
            <h1 style="font-size:32px">My <span style="color:#ff6b35">Logbook</span></h1>
            <div style="text-align:right">
                <div style="font-size:36px;font-weight:700;color:#ff6b35;font-family:monospace">{{ total_time }}</div>
                <div style="font-size:12px;color:#666">Total flight hours</div>
                <div style="font-size:12px;color:#444">{{ total_flights }} flights</div>
            </div>
        </div>

        <!-- Scan side -->
        <div class="card">
            <h3>Scan logbook pages with AI</h3>
            <p style="color:#666;font-size:14px;margin-bottom:16px">Upload photos of left and right page — AI reads all flights automatically</p>
            <div class="upload-row">
                <div class="upload-box" onclick="document.getElementById('left-page').click()">
                    <img id="left-preview">
                    <span id="left-label">📷 Left page</span>
                    <input type="file" id="left-page" accept="image/*" onchange="loadPage(this,'left')">
                </div>
                <div class="upload-box" onclick="document.getElementById('right-page').click()">
                    <img id="right-preview">
                    <span id="right-label">📷 Right page</span>
                    <input type="file" id="right-page" accept="image/*" onchange="loadPage(this,'right')">
                </div>
            </div>
            <button class="scan-btn" id="scan-btn" onclick="scanPages()" disabled>Scan with AI</button>
            <div class="status" id="status"></div>
        </div>

        <!-- Logbog entries -->
        <div class="card">
            <h3>Flight entries ({{ entries|length }} total)</h3>
            {% if entries %}
            <table>
                <tr>
                    <th>Date</th>
                    <th>From</th>
                    <th>To</th>
                    <th>Aircraft</th>
                    <th>Reg</th>
                    <th>Total</th>
                    <th>Dual</th>
                    <th>Ldg</th>
                    <th></th>
                </tr>
                {% for e in entries %}
                <tr onclick="editEntry({{ e.id }}, '{{ e.flight_date or '' }}', '{{ e.dep_place or '' }}', '{{ e.arr_place or '' }}', '{{ e.aircraft_type or '' }}', '{{ e.registration or '' }}', '{{ e.total_time or '' }}', '{{ e.dual or '' }}', '{{ e.landings_day or '' }}')" style="cursor:pointer">
                    <td>{{ e.flight_date or '—' }}</td>
                    <td>{{ e.dep_place or '—' }}</td>
                    <td>{{ e.arr_place or '—' }}</td>
                    <td>{{ e.aircraft_type or '—' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or '—' }}</td>
                    <td>{{ e.total_time or '—' }}</td>
                    <td>{{ e.dual or '—' }}</td>
                    <td>{{ e.landings_day or '—' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="event.stopPropagation();return confirm('Delete?')">✕</a></td>
                </tr>
                {% endfor %}
            </table>
            {% else %}
            <p style="color:#444;font-size:14px;padding:16px 0">No flights yet — scan your logbook pages above!</p>
            {% endif %}
        </div>
    </div>

    <!-- Edit modal -->
    <div id="edit-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:1000;overflow-y:auto">
        <div style="max-width:500px;margin:40px auto;background:#1a1a2e;border-radius:12px;padding:28px;position:relative">
            <button onclick="document.getElementById('edit-modal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;color:#aaa;font-size:20px;cursor:pointer">✕</button>
            <h3 style="margin-bottom:16px">Edit flight entry</h3>
            <form id="edit-form" method="POST">
                <label style="font-size:12px;color:#666">Date (DD/MM/YYYY)</label>
                <input type="text" name="flight_date" id="edit-date" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white;margin-bottom:10px">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
                    <div>
                        <label style="font-size:12px;color:#666">From</label>
                        <input type="text" name="dep_place" id="edit-dep" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">To</label>
                        <input type="text" name="arr_place" id="edit-arr" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px">
                    <div>
                        <label style="font-size:12px;color:#666">Aircraft type</label>
                        <input type="text" name="aircraft_type" id="edit-type" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">Registration</label>
                        <input type="text" name="registration" id="edit-reg" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:10px">
                    <div>
                        <label style="font-size:12px;color:#666">Total time</label>
                        <input type="text" name="total_time" id="edit-total" placeholder="H:MM" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">Dual</label>
                        <input type="text" name="dual" id="edit-dual" placeholder="H:MM" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">Landings</label>
                        <input type="number" name="landings_day" id="edit-ldg" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                </div>
                <div style="margin-top:10px">
                    <label style="font-size:12px;color:#666">Remarks</label>
                    <input type="text" name="remarks" id="edit-remarks" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                </div>
                <button type="submit" style="background:#ff6b35;color:white;border:none;padding:14px;border-radius:8px;font-size:15px;cursor:pointer;font-weight:600;width:100%;margin-top:16px">Save changes</button>
            </form>
        </div>
    </div>

    <script>
        var pages = {left: null, right: null};

        function loadPage(input, side) {
            var file = input.files[0];
            if (!file) return;
            var reader = new FileReader();
            reader.onload = function(e) {
                var img = new Image();
                img.onload = function() {
                    var canvas = document.createElement("canvas");
                    var maxSize = 1600;
                    var w = img.width, h = img.height;
                    if (w > maxSize || h > maxSize) {
                        if (w > h) { h = h * maxSize / w; w = maxSize; }
                        else { w = w * maxSize / h; h = maxSize; }
                    }
                    canvas.width = w; canvas.height = h;
                    canvas.getContext("2d").drawImage(img, 0, 0, w, h);
                    var compressed = canvas.toDataURL("image/jpeg", 0.8);
                    pages[side] = compressed.split(",")[1];
                    document.getElementById(side+"-preview").src = compressed;
                    document.getElementById(side+"-preview").style.display = "block";
                    document.getElementById(side+"-label").style.display = "none";
                    if (pages.left || pages.right) {
                        document.getElementById("scan-btn").disabled = false;
                    }
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }

        function editEntry(id, date, dep, arr, type, reg, total, dual, ldg) {
            document.getElementById('edit-form').action = '/edit-logbook-entry/' + id;
            document.getElementById('edit-date').value = date;
            document.getElementById('edit-dep').value = dep;
            document.getElementById('edit-arr').value = arr;
            document.getElementById('edit-type').value = type;
            document.getElementById('edit-reg').value = reg;
            document.getElementById('edit-total').value = total;
            document.getElementById('edit-dual').value = dual;
            document.getElementById('edit-ldg').value = ldg;
            document.getElementById('edit-modal').style.display = 'block';
        }

        function scanPages() {
            var btn = document.getElementById("scan-btn");
            var status = document.getElementById("status");
            btn.disabled = true;
            btn.textContent = "Scanning...";
            status.style.display = "block";
            status.textContent = "AI is reading your logbook pages...";

            fetch("/logbook-scan", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({left_page: pages.left, right_page: pages.right})
            })
            .then(r => r.json())
            .then(result => {
                if (result.ok) {
                    var msg = "✓ " + result.saved + " flights saved!";
                    if (result.validation_warning) {
                        msg += "\n⚠ " + result.validation_warning;
                        status.style.color = "#ffc107";
                    }
                    if (result.page_totals) {
                        msg += "\nPage totals: " + JSON.stringify(result.page_totals);
                    }
                    status.textContent = msg;
                    setTimeout(() => location.reload(), 3000);
                } else {
                    status.textContent = "Error: " + (result.error || "Something went wrong");
                    btn.disabled = false;
                    btn.textContent = "Scan with AI";
                }
            })
            .catch(err => {
                status.textContent = "Error: " + err;
                btn.disabled = false;
                btn.textContent = "Scan with AI";
            });
        }
    </script>
</body>
</html>"""

@app.route('/edit-logbook-entry/<int:entry_id>', methods=['POST'])
@login_required
def edit_logbook_entry(entry_id):
    entry = LogbookEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        return redirect('/my-logbook')
    
    entry.flight_date = request.form.get('flight_date', '').strip() or None
    entry.dep_place = request.form.get('dep_place', '').strip() or None
    entry.arr_place = request.form.get('arr_place', '').strip() or None
    entry.aircraft_type = request.form.get('aircraft_type', '').strip() or None
    entry.registration = request.form.get('registration', '').strip() or None
    entry.total_time = request.form.get('total_time', '').strip() or None
    entry.dual = request.form.get('dual', '').strip() or None
    entry.landings_day = int(request.form.get('landings_day', 0) or 0) or None
    entry.remarks = request.form.get('remarks', '').strip() or None
    db.session.commit()
    return redirect('/my-logbook')
