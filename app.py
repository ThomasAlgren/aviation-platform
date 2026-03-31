AIRCRAFT_COCKPIT_HTML = """<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
                        <input type="text" name="arc_valid_until" type="date" value="{{ claimed.arc_valid_until or '' }}">
                        <input type="text" name="coa_valid_until" type="date" value="{{ claimed.coa_valid_until or '' }}">
                        <input type="text" name="insurance_valid_until" type="date" value="{{ claimed.insurance_valid_until or '' }}">
                        <input type="text" name="last_service_date" type="date" value="{{ claimed.last_service_date or '' }}">
                        <input type="text" name="next_service_date" type="date" value="{{ claimed.next_service_date or '' }}">
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
            <a href="/my-aircraft/{{ aircraft.tail }}/maintenance" class="action-btn">✦ Maintenance log <span>→</span></a>
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

@app.template_filter('from_json_first')
def from_json_first(s):
    try:
        import json
        arr = json.loads(s)
        return arr[0] if arr else ''
    except:
        return ''
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(DB_PATH, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(DB_PATH, 'panpanparts.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

def normalize_date(value):
    """Konverter alle datoformater til YYYY-MM-DD"""
    if not value:
        return None
    value = str(value).strip()
    from datetime import datetime
    for fmt in ['%Y-%m-%d', '%Y%m%d', '%d/%m/%Y', '%d/%m/%y', '%m/%d/%Y']:
        try:
            d = datetime.strptime(value, fmt)
            return d.strftime('%Y-%m-%d')
        except:
            pass
    return value

@app.template_filter('format_date')
def format_date(value):
    if not value:
        return 'Not registered'
    try:
        from datetime import datetime
        for fmt in ['%Y-%m-%d', '%Y%m%d', '%d/%m/%Y']:
            try:
                d = datetime.strptime(str(value), fmt)
                return d.strftime('%d %b %Y')
            except:
                pass
    except:
        pass
    return value
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
    preferred_aircraft = db.Column(db.Text)  # JSON liste af foretrukne tail#
    
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

class AircraftMaintenanceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tail = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    entry_date = db.Column(db.String(20))
    entry_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    performed_by = db.Column(db.String(200))
    approved_by = db.Column(db.String(200))
    hours_at_entry = db.Column(db.Float)
    document = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    mep_vfr = db.Column(db.String(10))
    mep_ifr = db.Column(db.String(10))
    pic_time = db.Column(db.String(10))
    copilot_time = db.Column(db.String(10))
    instructor_time = db.Column(db.String(10))
    multipilot_time = db.Column(db.String(10))
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
    ai_description = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    hours_engine_tbo = db.Column(db.Float)
    hours_prop = db.Column(db.Float)
    hours_prop_tbo = db.Column(db.Float)
    has_autopilot = db.Column(db.Boolean, default=False)
    has_adsb = db.Column(db.Boolean, default=False)
    is_hangared = db.Column(db.Boolean, default=False)
    engine_overhauls = db.Column(db.Integer, default=0)
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
    source = db.Column(db.String(50))
    source_url = db.Column(db.Text)
    title = db.Column(db.String(300))

class MaintenanceOrg(db.Model):
    __tablename__ = 'maintenance_org'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    approval_number = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(300))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    website = db.Column(db.String(200))
    source = db.Column(db.String(100))
    source_url = db.Column(db.Text)
    source_date = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
            conn.execute(db.text("ALTER TABLE aircraft_listing ADD COLUMN ai_description TEXT"))
            conn.execute(db.text("ALTER TABLE aircraft_listing ADD COLUMN source_url TEXT"))
            conn.execute(db.text("ALTER TABLE aircraft_listing ADD COLUMN source TEXT"))
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
                    <h3>{{ p.title or p.part_number or 'Unknown part' }}</h3>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
    <title>PanPanParts — Aircraft for Sale, Aviation Parts & Pilot Logbook</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Buy and sell aircraft and aviation parts. Browse 700+ aircraft for sale including Cessna, Piper, Cirrus and Diamond. Digital pilot logbook, EASA certified workshops directory.">
    <meta property="og:title" content="PanPanParts — Aircraft for Sale & Aviation Marketplace">
    <meta property="og:description" content="Buy and sell aircraft and aviation parts. 700+ aircraft for sale, EASA certified workshops, digital pilot logbook.">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://panpanparts.com/">
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
        .features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 1100px; margin: 0 auto 80px; padding: 0 20px; }
        .feature { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; }
        .feature-icon { font-size: 28px; margin-bottom: 12px; }
        .feature h3 { font-size: 15px; margin-bottom: 8px; }
        .feature p { font-size: 13px; color: #666; line-height: 1.6; }
        .cta-row { display: flex; gap: 16px; justify-content: center; margin: 24px 0; flex-wrap: wrap; }
        .cta-primary { background: #ff6b35; color: white; padding: 16px 32px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 16px; }
        .cta-primary:hover { background: #e55a25; }
        .cta-secondary { background: transparent; color: #ff6b35; padding: 16px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 16px; border: 2px solid #ff6b35; }
        .cta-secondary:hover { background: rgba(255,107,53,0.1); }
        .three-cards { display: flex; gap: 20px; margin-top: 32px; flex-wrap: wrap; }
        .tcard { flex: 1; min-width: 220px; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 12px; padding: 24px; }
        .tcard-icon { font-size: 32px; margin-bottom: 12px; }
        .tcard h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
        .tcard p { color: #666; font-size: 14px; line-height: 1.5; margin-bottom: 16px; }
        .tcard-link { color: #ff6b35; text-decoration: none; font-size: 14px; font-weight: 600; }
        .tcard-link:hover { text-decoration: underline; }
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
        <h1>The aviation platform<br>for <span>pilots and owners</span></h1>
        <p>Sell parts, manage your aircraft, track your logbook — all in one place</p>

        <div class="cta-row">
            <a href="/upload" class="cta-primary">+ List a part — free</a>
            <a href="/register" class="cta-secondary">Create pilot account</a>
        </div>

        <div class="stats">
            <div class="stat"><div class="stat-value">{{ "{:,.0f}".format(registry_count) }}</div><div class="stat-label">Aircraft registered</div></div>
            {% if part_count > 0 %}<div class="stat"><div class="stat-value">{{ part_count }}</div><div class="stat-label">Parts for sale</div></div>{% endif %}
            {% if aircraft_count > 0 %}<div class="stat"><div class="stat-value">{{ aircraft_count }}</div><div class="stat-label">Aircraft for sale</div></div>{% endif %}
            <div class="stat"><div class="stat-value">AI</div><div class="stat-label">Verified</div></div>
        </div>

        <div id="search" style="margin:0 auto 32px;max-width:640px;padding:0 20px">
            <form method="GET">
                <div class="search-box">
                    <input name="tail" placeholder="Find your aircraft — e.g. OY-RYY or N12345..." value="{{ tail }}">
                    <button type="submit">Search</button>
                </div>
            </form>
        </div>

        <div class="carousel-section" style="margin:0 auto 48px;max-width:1100px;padding:0 20px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">
                <span style="font-size:13px;text-transform:uppercase;letter-spacing:2px;color:#ff6b35">Featured Aircraft</span>
                <a href="/aircraft-for-sale" style="color:#666;font-size:13px;text-decoration:none">View all {{ aircraft_count }} →</a>
            </div>
            <div class="carousel-track" id="carouselTrack">
                {% for f in featured_aircraft %}
                <a class="carousel-card" href="/aircraft-listing/{{ f.id }}">
                    <div class="carousel-img" style="background-image:url('{{ f.hero_image }}')"></div>
                    <div class="carousel-body">
                        <div style="font-size:11px;color:#ff6b35;font-family:monospace">{{ f.tail }}</div>
                        <div style="font-size:14px;font-weight:600;margin:2px 0">{{ f.manufacturer }} {{ f.model }}</div>
                        <div style="font-size:12px;color:#666">{{ f.year }}{% if f.location %} · {{ f.location[:20] }}{% endif %}</div>
                        <div style="font-size:13px;color:#ff6b35;font-weight:600;margin-top:6px">{% if f.price %}EUR {{ "{:,.0f}".format(f.price) }}{% else %}Price on request{% endif %}</div>
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>
        <style>
        .carousel-section { overflow: hidden; }
        .carousel-track { display: flex; gap: 16px; transition: transform 0.5s ease; }
        .carousel-card { flex: 0 0 220px; background: #1a1a2e; border-radius: 12px; border: 1px solid #2a2a3e; text-decoration: none; color: inherit; overflow: hidden; transition: border-color 0.2s; }
        .carousel-card:hover { border-color: #ff6b35; }
        .carousel-img { height: 130px; background-size: cover; background-position: center; background-color: #2a2a3e; }
        .carousel-body { padding: 12px; }
        </style>
        <script>
        (function() {
            var track = document.getElementById('carouselTrack');
            if (!track) return;
            var cards = track.children.length;
            var cardWidth = 236;
            var current = 0;
            setInterval(function() {
                current = (current + 1) % cards;
                track.style.transform = 'translateX(-' + (current * cardWidth) + 'px)';
                // Reset smoothly when near end
                if (current === cards - 1) {
                    setTimeout(function() {
                        track.style.transition = 'none';
                        current = 0;
                        track.style.transform = 'translateX(0)';
                        setTimeout(function() { track.style.transition = 'transform 0.5s ease'; }, 50);
                    }, 500);
                }
            }, 4000);
        })();
        </script>

        <div class="three-cards">
            <div class="tcard">
                <div class="tcard-icon">💰</div>
                <h3>Sell your parts</h3>
                <p>Got spare parts collecting dust? List in 2 minutes — AI writes the description and checks documentation automatically.</p>
                <a href="/upload" class="tcard-link">List a part →</a>
            </div>
            <div class="tcard">
                <div class="tcard-icon">✈️</div>
                <h3>Pilot cockpit</h3>
                <p>Digital logbook, flight currency, certificates, medical — everything a pilot needs in one place.</p>
                <a href="/register" class="tcard-link">Get started →</a>
            </div>
            <div class="tcard">
                <div class="tcard-icon">🔍</div>
                <h3>Aircraft registry</h3>
                <p>Search {{ "{:,.0f}".format(registry_count) }} registered aircraft from USA, EU, UK, Australia, Canada and Switzerland.</p>
                <a href="#search" class="tcard-link">Search registry →</a>
            </div>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
            <a href="/sell-aircraft/{{ aircraft.tail }}" class="sell-btn" style="display:block;text-align:center;text-decoration:none;background:#2a2a3e">List {{ aircraft.tail }} for sale</a>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    if tail and not any(tail.upper().startswith(p) for p in ["OY", "LN", "HB", "VH", "SE", "PH", "OO", "EI", "CS", "EC", "I-", "D-", "F-", "G-", "OE", "C-", "N", "ZK", "ZS"]):
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
    # Hent 16 featured fly til karussel
    import json as _json2
    conn3 = get_pg_conn()
    cur3 = conn3.cursor()
    cur3.execute("SELECT id, tail, manufacturer, model, year, price, location, images FROM aircraft_listing WHERE status='active' AND images != '[]' AND price > 0 ORDER BY RANDOM()")
    featured_rows = cur3.fetchall()
    conn3.close()
    featured_aircraft = []
    for fr in featured_rows:
        imgs = _json2.loads(fr[7]) if isinstance(fr[7], str) else fr[7]
        featured_aircraft.append({'id': fr[0], 'tail': fr[1], 'manufacturer': fr[2], 'model': fr[3], 'year': fr[4], 'price': fr[5], 'location': fr[6], 'hero_image': imgs[0] if imgs else ''})

    return render_template_string(SEARCH_HTML, tail=tail, model=model, state=state,
        year_from=year_from, year_to=year_to, states=states,
        results=results, result_count=result_count, part_count=part_count, aircraft_count=aircraft_count, registry_count=registry_count, featured_aircraft=featured_aircraft)

@app.route("/aircraft/<tail>")
def aircraft_detail(tail):
    r = get_aircraft('N' + tail.upper())
    if not r:
        r = get_aircraft(tail.upper())
    if not r:
        return render_template_string("""<!DOCTYPE html>
<html><head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script><meta charset="utf-8"><style>
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
<html><head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script><meta charset="utf-8"><style>
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
<html><head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script><meta charset="utf-8"><style>
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
<html><head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script><meta charset="utf-8"><style>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
        <div class="card"><h3>Aircraft registry</h3><p>Search across 525,000+ registered aircraft from USA, EU, UK, Australia, Canada and Switzerland. More registries added continuously.</p></div>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
        <div class="card"><h3>Aircraft registry</h3><p>Search across 525,000+ registered aircraft from USA, EU, UK, Australia, Canada and Switzerland. More registries added continuously.</p></div>
        <div class="card"><h3>Pan Pan</h3><p>In aviation, Pan Pan is an urgency call — the step before Mayday. We chose the name because finding the right part quickly can be exactly that urgent.</p></div>
        <div class="contact">Questions: <a href="mailto:hello@panpanparts.com">hello@panpanparts.com</a></div>
    </div>
</body>
</html>
"""

LOGIN_HTML = '''<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
                    <div class="part-number">{{ p.title or p.part_number or 'Unknown part' }}</div>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
    <title>{{ part.title or part.part_number or 'Part' }} - PanPanParts</title>
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
            <div class="part-title">{{ part.title or part.part_number or 'Unknown part' }}</div>
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

@app.route('/upload-image', methods=['POST'])
@login_required
def upload_image():
    import boto3, base64, uuid, json as _json
    data = request.get_json()
    image_data = data.get('image', '')
    
    # Fjern data URL prefix
    if ',' in image_data:
        image_data = image_data.split(',')[1]
    
    try:
        image_bytes = base64.b64decode(image_data)
        filename = f"listings/{current_user.id}/{uuid.uuid4().hex}.jpg"
        
        s3 = boto3.client('s3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('AWS_REGION', 'eu-north-1')
        )
        bucket = os.environ.get('AWS_S3_BUCKET', 'panpanparts-backup')
        
        s3.put_object(
            Bucket=bucket,
            Key=filename,
            Body=image_bytes,
            ContentType='image/jpeg'
        )
        
        url = f"https://{bucket}.s3.{os.environ.get('AWS_REGION', 'eu-north-1')}.amazonaws.com/{filename}"
        return _json.dumps({'ok': True, 'url': url})
    except Exception as e:
        return _json.dumps({'ok': False, 'error': str(e)})

@app.route('/sell-aircraft/ai-analyze', methods=['POST'])
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

Clean the description first — remove any photo captions, image references, navigation elements, or metadata (like "Exterior (6)", "Posted: X ago", "Views: XXXX", "Make", "Model" labels etc). Keep only the actual descriptive text about the aircraft.

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

        def _f(name):
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
            ai_description=request.form.get('ai_description', ''),
        )
        db.session.add(listing)
        db.session.commit()
        return redirect(f"/aircraft-listing/{listing.id}")
    return render_template_string(SELL_AIRCRAFT_HTML, aircraft=aircraft, error=None)

SELL_AIRCRAFT_HTML = """<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
                <h3>Hours &amp; technical</h3>
                <div class="row2">
                    <div><label>Airframe total time (TT)</label>
                    <input type="number" name="hours_total" placeholder="e.g. 456" min="0"></div>
                    <div><label>Engine SMOH</label>
                    <input type="number" name="hours_engine" placeholder="e.g. 450" min="0"></div>
                </div>
                <div class="row2">
                    <div><label>Engine TBO (hours)</label>
                    <input type="number" name="hours_engine_tbo" placeholder="e.g. 2000" min="0"></div>
                    <div><label>Engine overhauls (count)</label>
                    <input type="number" name="engine_overhauls" placeholder="e.g. 1" min="0"></div>
                </div>
                <div class="row2">
                    <div><label>Propeller hours</label>
                    <input type="number" name="hours_prop" placeholder="e.g. 456" min="0"></div>
                    <div><label>Propeller OH interval (hours)</label>
                    <input type="number" name="hours_prop_tbo" placeholder="e.g. 1300" min="0"></div>
                </div>
                <label style="margin-top:12px;display:block">Equipment</label>
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
            </div>

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
                        var maxSize = 1200;
                        var w = img.width, h = img.height;
                        if (w > maxSize || h > maxSize) {
                            if (w > h) { h = h * maxSize / w; w = maxSize; }
                            else { w = w * maxSize / h; h = maxSize; }
                        }
                        canvas.width = w; canvas.height = h;
                        canvas.getContext('2d').drawImage(img, 0, 0, w, h);
                        var compressed = canvas.toDataURL('image/jpeg', 0.75);
                        
                        // Upload til S3
                        var thumbEl = addPendingThumb();
                        fetch('/upload-image', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({image: compressed})
                        })
                        .then(r => r.json())
                        .then(result => {
                            if (result.ok) {
                                uploadedImages.push(result.url);
                                document.getElementById('images_data').value = uploadedImages.join('|||');
                                thumbEl.src = result.url;
                                thumbEl.style.opacity = '1';
                            } else {
                                thumbEl.remove();
                                alert('Upload fejlede: ' + result.error);
                            }
                        })
                        .catch(function(e) {
                            thumbEl.remove();
                            alert('Upload fejlede — prøv igen');
                        });
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

        function addPendingThumb() {
            var grid = document.getElementById('img-grid');
            var img = document.createElement('img');
            img.className = 'img-thumb';
            img.style.opacity = '0.3';
            img.src = 'data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=';
            img.style.background = '#2a2a3e';
            grid.appendChild(img);
            return img;
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


@app.route('/aircraft-for-sale')
def aircraft_for_sale():
    try:
        import json as _json
        listings = AircraftListing.query.order_by(AircraftListing.created_at.desc()).limit(800).all()
        listings_data = []
        for l in listings:
            listings_data.append({'id': l.id, 'tail': l.tail, 'manufacturer': l.manufacturer, 'model': l.model, 'year': l.year, 'price': l.price or 0, 'hours_total': l.hours_total, 'location': l.location, 'hero_image': l.hero_image, 'condition': l.condition, 'seller_type': l.seller_type, 'ai_highlights': l.ai_highlights, 'description': l.description, 'images': l.images})
        conn_f = get_pg_conn()
        cur_f = conn_f.cursor()
        cur_f.execute("SELECT id, tail, manufacturer, model, year, price, location, images FROM aircraft_listing WHERE status='active' AND images != '[]' ORDER BY RANDOM() LIMIT 16")
        featured_rows = cur_f.fetchall()
        conn_f.close()
        featured_aircraft = []
        for fr in featured_rows:
            imgs = _json.loads(fr[7]) if isinstance(fr[7], str) else fr[7]
            featured_aircraft.append({'id': fr[0], 'tail': fr[1], 'manufacturer': fr[2], 'model': fr[3], 'year': fr[4], 'price': fr[5], 'location': fr[6], 'hero_image': imgs[0] if imgs else ''})
        conn_m = get_pg_conn()
        cur_m = conn_m.cursor()
        cur_m.execute("SELECT DISTINCT manufacturer FROM aircraft_listing WHERE manufacturer IS NOT NULL AND status='active' ORDER BY manufacturer")
        manufacturers = [r[0] for r in cur_m.fetchall() if r[0]]
        conn_m.close()
        return render_template_string(AIRCRAFT_FOR_SALE_HTML, listings=listings, listings_json=_json.dumps(listings_data), current_user=current_user, featured_aircraft=featured_aircraft, manufacturers=manufacturers)
    except Exception as e:
        return f'FEJL: {str(e)}', 500

    import json as _json
    import anthropic as ac
    data = request.get_json()
    queries = data.get('queries', [])
    listings = data.get('listings', [])

    if not queries:
        return _json.dumps({'matches': listings, 'suggestion': None})

    combined_query = ' AND '.join(queries)

    # Step 1: Ask AI to extract search filters (fast, no listings sent)
    client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"""Extract search filters from this aircraft search query. Return ONLY JSON, no markdown.

Query: {combined_query}

Return:
{{
  "keywords": ["list", "of", "keywords", "to", "search", "in", "description", "and", "model"],
  "max_price": null or number,
  "min_price": null or number,
  "manufacturer": null or string,
  "has_autopilot": null or true,
  "has_adsb": null or true,
  "suggestion": null or "helpful tip"
}}

Examples:
- "glass cockpit" -> keywords: ["G1000", "Avidyne", "glass", "Garmin", "GTN", "GNS"]
- "under 100k" -> max_price: 100000
- "Cessna" -> manufacturer: "Cessna"
- "with autopilot" -> has_autopilot: true
- "newer than 2010" -> year_from: 2010
- "older than 1990" -> year_to: 1990
- "between 2005 and 2015" -> year_from: 2005, year_to: 2015

Also add to JSON:
  "year_from": null or number,
  "year_to": null or number,"""
        }]
    )

    try:
        filters = _json.loads(response.content[0].text.replace("```json","").replace("```","").strip())
    except:
        filters = {"keywords": queries}

    # Step 2: Filter in database using SQL
    conn = get_pg_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    conditions = ["status = 'active'"]
    params = []

    if filters.get('max_price'):
        conditions.append("price <= %s")
        params.append(filters['max_price'])
    if filters.get('min_price'):
        conditions.append("price >= %s")
        params.append(filters['min_price'])
    if filters.get('manufacturer'):
        conditions.append("manufacturer ILIKE %s")
        params.append(f"%{filters['manufacturer']}%")
    if filters.get('has_autopilot'):
        conditions.append("has_autopilot = true")
    if filters.get('has_adsb'):
        conditions.append("has_adsb = true")
    if filters.get('year_from'):
        conditions.append("CAST(year AS INTEGER) >= %s")
        params.append(int(filters['year_from']))
    if filters.get('year_to'):
        conditions.append("CAST(year AS INTEGER) <= %s")
        params.append(int(filters['year_to']))

    keywords = filters.get('keywords', [])
    if keywords:
        kw_conditions = []
        for kw in keywords[:5]:
            kw_conditions.append("(description ILIKE %s OR model ILIKE %s OR manufacturer ILIKE %s)")
            params.extend([f"%{kw}%", f"%{kw}%", f"%{kw}%"])
        conditions.append("(" + " OR ".join(kw_conditions) + ")")

    where = " AND ".join(conditions)
    cur.execute(f"SELECT * FROM aircraft_listing WHERE {where} ORDER BY CASE WHEN price IS NULL OR price = 0 THEN 1 ELSE 0 END, price ASC LIMIT 50", params)
    rows = cur.fetchall()
    conn.close()

    matches = []
    for r in rows:
        row = dict(r)
        try: row['images'] = _json.loads(row['images']) if isinstance(row['images'], str) else row['images']
        except: row['images'] = []
        matches.append(row)

    return _json.dumps({'matches': matches, 'suggestion': filters.get('suggestion')})


AIRCRAFT_FOR_SALE_HTML = """<!DOCTYPE html>
<html>
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-K3PJMNF1JE');</script>
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
        .page { display: flex; max-width: 1400px; margin: 0 auto; padding: 32px 20px; gap: 32px; }
        
        /* FILTER PANEL */
        .filter-panel { width: 260px; flex-shrink: 0; }
        .filter-panel h2 { font-size: 13px; font-weight: 700; color: #666; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 20px; }
        .filter-group { margin-bottom: 24px; border-bottom: 1px solid #1a1a2e; padding-bottom: 24px; }
        .filter-group label { display: block; font-size: 12px; color: #666; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
        .filter-group select, .filter-group input[type=number] { width: 100%; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 8px; color: white; padding: 10px 12px; font-size: 14px; }
        .filter-group select:focus, .filter-group input:focus { outline: none; border-color: #ff6b35; }
        .filter-row { display: flex; gap: 8px; }
        .filter-row input { width: 50%; }
        .filter-toggle { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; cursor: pointer; }
        .filter-toggle input[type=checkbox] { width: 18px; height: 18px; accent-color: #ff6b35; cursor: pointer; }
        .filter-toggle span { font-size: 14px; color: #ccc; }
        .btn-reset { width: 100%; background: transparent; border: 1px solid #2a2a3e; color: #666; padding: 10px; border-radius: 8px; cursor: pointer; font-size: 13px; margin-top: 8px; }
        .btn-reset:hover { border-color: #ff6b35; color: #ff6b35; }
        
        /* MAIN CONTENT */
        .main { flex: 1; min-width: 0; }
        .search-box { display: flex; gap: 12px; margin-bottom: 24px; }
        .search-input { flex: 1; padding: 14px 18px; border: 2px solid #2a2a3e; border-radius: 12px; font-size: 15px; background: #1a1a2e; color: white; }
        .search-input:focus { outline: none; border-color: #ff6b35; }
        .search-btn { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 12px; font-size: 15px; cursor: pointer; font-weight: 700; }
        .results-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .results-count { font-size: 14px; color: #666; }
        .listings-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
        .listing-card { background: #1a1a2e; border-radius: 16px; overflow: hidden; border: 1px solid #2a2a3e; text-decoration: none; color: white; display: block; transition: transform 0.2s, border-color 0.2s; }
        .listing-card:hover { transform: translateY(-2px); border-color: #ff6b35; }
        .card-img { width: 100%; height: 180px; object-fit: cover; display: block; }
        .card-img-placeholder { width: 100%; height: 180px; background: linear-gradient(135deg, #1a1a2e, #2a1a3e); display: flex; align-items: center; justify-content: center; font-size: 48px; }
        .card-body { padding: 16px; }
        .card-tail { font-size: 12px; color: #666; font-family: monospace; letter-spacing: 1px; margin-bottom: 4px; }
        .card-title { font-size: 16px; font-weight: 700; margin-bottom: 4px; }
        .card-meta { font-size: 13px; color: #666; margin-bottom: 10px; }
        .card-price { font-size: 22px; font-weight: 800; color: #ff6b35; font-family: monospace; }
        .card-hours { font-size: 12px; color: #666; margin-top: 4px; }
        .card-tags { margin-top: 8px; display: flex; gap: 6px; flex-wrap: wrap; }
        .tag { font-size: 11px; background: #0a0a14; border: 1px solid #2a2a3e; border-radius: 4px; padding: 2px 8px; color: #aaa; }
        .tag.green { border-color: #2a5a2a; color: #4caf50; }
        .spinner { display: inline-block; width: 20px; height: 20px; border: 3px solid #333; border-top-color: #ff6b35; border-radius: 50%; animation: spin 0.8s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .ai-suggestion { background: #1a1a2e; border-radius: 10px; padding: 12px 16px; margin-bottom: 16px; font-size: 13px; color: #aaa; display: none; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">
            <a href="/parts">Parts for sale</a>
            {% if current_user.is_authenticated %}<a href="/my-listings" class="primary">+ List aircraft</a>
            {% else %}<a href="/register" class="primary">+ List aircraft</a>{% endif %}
        </div>
    </div>

    <div class="page">
        <!-- FILTER PANEL -->
        <div class="filter-panel">
            <h2>Filters</h2>
            
            <div class="filter-group">
                <label>Manufacturer</label>
                <select id="f-manufacturer" onchange="applyFilters()">
                    <option value="">All manufacturers</option>
                    {% for m in manufacturers %}<option>{{ m }}</option>{% endfor %}
                </select>
            </div>

            <div class="filter-group">
                <label>Price (EUR)</label>
                <div class="filter-row">
                    <input type="number" id="f-price-min" placeholder="Min" onchange="applyFilters()">
                    <input type="number" id="f-price-max" placeholder="Max" onchange="applyFilters()">
                </div>
            </div>

            <div class="filter-group">
                <label>Year</label>
                <div class="filter-row">
                    <input type="number" id="f-year-min" placeholder="From" max="2025" onchange="applyFilters()">
                    <input type="number" id="f-year-max" placeholder="To" max="2025" onchange="applyFilters()">
                </div>
            </div>

            <div class="filter-group">
                <label>Total hours (max)</label>
                <input type="number" id="f-hours-max" placeholder="e.g. 2000" onchange="applyFilters()">
            </div>

            <div class="filter-group">
                <label>Equipment</label>
                <label class="filter-toggle">
                    <input type="checkbox" id="f-autopilot" onchange="applyFilters()">
                    <span>Autopilot</span>
                </label>
                <label class="filter-toggle">
                    <input type="checkbox" id="f-adsb" onchange="applyFilters()">
                    <span>ADS-B</span>
                </label>
                <label class="filter-toggle">
                    <input type="checkbox" id="f-hangared" onchange="applyFilters()">
                    <span>Hangared</span>
                </label>
            </div>

            <button class="btn-reset" onclick="resetFilters()">Reset filters</button>
        </div>

        <!-- MAIN CONTENT -->
        <div class="main">
            <div class="search-box">
                <input type="text" class="search-input" id="search-input" 
                    placeholder="Search — e.g. Garmin G1000, fresh annual, IFR equipped..."
                    onkeydown="if(event.key==='Enter') doSearch()">
                <button class="search-btn" onclick="doSearch()">Search →</button>
            </div>
            
            <div class="ai-suggestion" id="ai-suggestion"></div>

            <div class="results-header">
                <div class="results-count" id="results-count">{{ listings|length }} aircraft listed</div>
                <div id="loading-indicator"></div>
            </div>

            <div class="listings-grid" id="listings-grid">
                {% for l in listings %}
                {% set imgs = l.images|from_json_first if l.images else '' %}
                {% set hero = l.hero_image or imgs %}
                <a href="/aircraft-listing/{{ l.id }}" class="listing-card">
                    {% if hero %}
                    <img class="card-img" src="{{ hero }}" alt="{{ l.manufacturer }} {{ l.model }}" loading="lazy">
                    {% else %}
                    <div class="card-img-placeholder">✈️</div>
                    {% endif %}
                    <div class="card-body">
                        <div class="card-tail">{{ l.tail }}</div>
                        <div class="card-title">{{ l.manufacturer }} {{ l.model }}</div>
                        <div class="card-meta">{{ l.year }}{% if l.location %} · {{ l.location[:30] }}{% endif %}</div>
                        <div class="card-price">{% if l.price and l.price > 0 %}EUR {{ "{:,.0f}".format(l.price) }}{% else %}Price on request{% endif %}</div>
                        <div class="card-hours">{% if l.hours_total %}{{ l.hours_total|int }}h TT{% endif %}</div>
                        <div class="card-tags">
                            {% if l.has_autopilot %}<span class="tag green">Autopilot</span>{% endif %}
                            {% if l.has_adsb %}<span class="tag green">ADS-B</span>{% endif %}
                            {% if l.is_hangared %}<span class="tag green">Hangared</span>{% endif %}
                        </div>
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>
    </div>

<script>
const ALL_LISTINGS = {{ listings_json|safe }};
let currentListings = [...ALL_LISTINGS];

function renderListings(listings) {
    const grid = document.getElementById('listings-grid');
    document.getElementById('results-count').textContent = listings.length + ' aircraft listed';
    if (listings.length === 0) {
        grid.innerHTML = '<div style="grid-column:1/-1;text-align:center;padding:80px 0;color:#666"><div style="font-size:48px;margin-bottom:16px">✈️</div><div>No aircraft found</div></div>';
        return;
    }
    grid.innerHTML = listings.map(l => {
        let imgs = [];
        try { imgs = typeof l.images === 'string' ? JSON.parse(l.images) : (l.images || []); } catch(e) {}
        const hero = l.hero_image || (imgs.length > 0 ? imgs[0] : '');
        const price = l.price > 0 ? 'EUR ' + l.price.toLocaleString('en', {maximumFractionDigits:0}) : 'Price on request';
        const tags = [
            l.has_autopilot ? '<span class="tag green">Autopilot</span>' : '',
            l.has_adsb ? '<span class="tag green">ADS-B</span>' : '',
            l.is_hangared ? '<span class="tag green">Hangared</span>' : ''
        ].join('');
        return `<a href="/aircraft-listing/${l.id}" class="listing-card">
            ${hero ? `<img class="card-img" src="${hero}" alt="${l.manufacturer} ${l.model}" loading="lazy">` : '<div class="card-img-placeholder">✈️</div>'}
            <div class="card-body">
                <div class="card-tail">${l.tail || ''}</div>
                <div class="card-title">${l.manufacturer || ''} ${l.model || ''}</div>
                <div class="card-meta">${l.year || ''}${l.location ? ' · ' + l.location.substring(0,30) : ''}</div>
                <div class="card-price">${price}</div>
                <div class="card-hours">${l.hours_total ? Math.round(l.hours_total) + 'h TT' : ''}</div>
                <div class="card-tags">${tags}</div>
            </div>
        </a>`;
    }).join('');
}

function applyFilters() {
    const manufacturer = document.getElementById('f-manufacturer').value.toLowerCase();
    const priceMin = parseFloat(document.getElementById('f-price-min').value) || 0;
    const priceMax = parseFloat(document.getElementById('f-price-max').value) || Infinity;
    const yearMin = parseInt(document.getElementById('f-year-min').value) || 0;
    const yearMax = parseInt(document.getElementById('f-year-max').value) || 9999;
    const hoursMax = parseFloat(document.getElementById('f-hours-max').value) || Infinity;
    const needAutopilot = document.getElementById('f-autopilot').checked;
    const needAdsb = document.getElementById('f-adsb').checked;
    const needHangared = document.getElementById('f-hangared').checked;

    let filtered = ALL_LISTINGS.filter(l => {
        if (manufacturer && !(l.manufacturer || '').toLowerCase().includes(manufacturer)) return false;
        if (priceMin > 0 && l.price < priceMin) return false;
        if (priceMax < Infinity && l.price > priceMax) return false;
        if (yearMin > 0 && parseInt(l.year) < yearMin) return false;
        if (yearMax < 9999 && parseInt(l.year) > yearMax) return false;
        if (hoursMax < Infinity && l.hours_total > hoursMax) return false;
        if (needAutopilot && !l.has_autopilot) return false;
        if (needAdsb && !l.has_adsb) return false;
        if (needHangared && !l.is_hangared) return false;
        return true;
    });
    currentListings = filtered;
    renderListings(filtered);
}

function resetFilters() {
    document.getElementById('f-manufacturer').value = '';
    document.getElementById('f-price-min').value = '';
    document.getElementById('f-price-max').value = '';
    document.getElementById('f-year-min').value = '';
    document.getElementById('f-year-max').value = '';
    document.getElementById('f-hours-max').value = '';
    document.getElementById('f-autopilot').checked = false;
    document.getElementById('f-adsb').checked = false;
    document.getElementById('f-hangared').checked = false;
    document.getElementById('search-input').value = '';
    document.getElementById('ai-suggestion').style.display = 'none';
    currentListings = [...ALL_LISTINGS];
    renderListings(ALL_LISTINGS);
}

async function doSearch() {
    const query = document.getElementById('search-input').value.trim();
    if (!query) { applyFilters(); return; }
    
    document.getElementById('loading-indicator').innerHTML = '<div class="spinner"></div>';
    
    try {
        const resp = await fetch('/api/aircraft-search', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({queries: [query], listings: currentListings})
        });
        const data = await resp.json();
        renderListings(data.matches || []);
        if (data.suggestion) {
            const s = document.getElementById('ai-suggestion');
            s.textContent = '💡 ' + data.suggestion;
            s.style.display = 'block';
        }
    } catch(e) {
        console.error(e);
    }
    document.getElementById('loading-indicator').innerHTML = '';
}
</script>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
                    <div style="font-weight:600">{{ p.title or p.part_number or "Unknown part" }}</div>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
    import json as _json
    listing = AircraftListing.query.get_or_404(listing_id)
    listing.views = (listing.views or 0) + 1
    db.session.commit()
    images = []
    if listing.images:
        try: images = _json.loads(listing.images)
        except: images = []
    highlights = []
    if listing.ai_highlights:
        try: highlights = _json.loads(listing.ai_highlights)
        except: highlights = []
    specs = {}
    if listing.ai_specs:
        try: specs = _json.loads(listing.ai_specs)
        except: specs = {}
    return render_template_string(AIRCRAFT_LISTING_HTML, listing=listing, images=images, highlights=highlights, specs=specs, current_user=current_user)

def aircraft_listing_detail_OLD(listing_id):
    listing = AircraftListing.query.get_or_404(listing_id)
    return render_template_string(AIRCRAFT_LISTING_DETAIL_HTML, 
        listing=listing, 
        logged_in=current_user.is_authenticated)


AIRCRAFT_LISTING_HTML = """<!DOCTYPE html>
<html>
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-K3PJMNF1JE');</script>
    <title>{{ listing.tail }} — {{ listing.manufacturer }} {{ listing.model }} for Sale | PanPanParts</title>
    <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{{ listing.manufacturer }} {{ listing.model }}{% if listing.year %} ({{ listing.year }}){% endif %}{% if listing.price and listing.price > 0 %} for sale at EUR {{ "{:,.0f}".format(listing.price) }}{% else %} for sale{% endif %}{% if listing.location %} — {{ listing.location }}{% endif %}. Listed on PanPanParts.">
    {% if images %}<meta property="og:image" content="{{ images[0] }}">{% endif %}
    <link rel="canonical" href="https://panpanparts.com/aircraft-listing/{{ listing.id }}">
    <style>
        *{margin:0;padding:0;box-sizing:border-box;}
        body{font-family:-apple-system,sans-serif;background:#0a0a14;color:white;}
        .header{padding:16px 40px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #1a1a2e;position:sticky;top:0;background:rgba(10,10,20,0.97);backdrop-filter:blur(10px);z-index:100;}
        .logo{font-size:20px;font-weight:700;}.logo span{color:#ff6b35;}
        .nav a{color:#aaa;text-decoration:none;font-size:14px;margin-left:16px;}
        .nav a.primary{background:#ff6b35;color:white;padding:8px 16px;border-radius:8px;}

        /* HERO */
        .hero-wrap{position:relative;background:#000;}
        .hero-img{width:100%;height:65vh;min-height:400px;object-fit:cover;display:block;cursor:pointer;}
        .hero-placeholder{width:100%;height:40vh;background:linear-gradient(135deg,#1a1a2e,#2a1a3e);display:flex;align-items:center;justify-content:center;font-size:80px;}
        .hero-nav{position:absolute;top:50%;transform:translateY(-50%);background:rgba(0,0,0,0.5);color:white;border:none;font-size:24px;width:48px;height:48px;border-radius:50%;cursor:pointer;z-index:10;}
        .hero-nav-left{left:16px;}.hero-nav-right{right:16px;}
        .hero-counter{position:absolute;bottom:16px;right:16px;background:rgba(0,0,0,0.6);color:white;font-size:12px;padding:4px 10px;border-radius:20px;}
        .thumb-strip{display:flex;gap:6px;padding:8px;background:#0d0d1a;overflow-x:auto;}
        .thumb{width:72px;height:52px;object-fit:cover;border-radius:6px;cursor:pointer;border:2px solid transparent;flex-shrink:0;opacity:0.6;transition:all 0.2s;}
        .thumb.active,.thumb:hover{border-color:#ff6b35;opacity:1;}

        /* INFO BAR */
        .info-bar{background:#0d0d1a;border-bottom:1px solid #1a1a2e;padding:16px 40px;display:flex;align-items:center;gap:32px;flex-wrap:wrap;}
        .info-bar-price{font-size:28px;font-weight:800;color:#ff6b35;font-family:monospace;}
        .info-bar-meta{font-size:13px;color:#666;}
        .info-bar-meta strong{color:#aaa;}
        .hbadge{display:inline-block;padding:4px 10px;border-radius:4px;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-right:6px;}
        .info-bar-gauge{padding:12px 16px;border-right:1px solid #1a2a1a;text-align:center;flex-shrink:0;}
        .info-bar-gauge-lbl{font-size:9px;color:#4a8a4a;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:4px;}
        .info-bar-gauge-val{font-size:12px;color:#ccc;font-weight:700;margin-top:4px;}
        .hbadge.yes{background:rgba(76,175,80,0.12);color:#4caf50;border:1px solid rgba(76,175,80,0.4);}
        .hbadge.orange{background:rgba(255,107,53,0.12);color:#ff6b35;border:1px solid rgba(255,107,53,0.4);}

        /* LAYOUT */
        .page{max-width:1100px;margin:0 auto;padding:32px 20px;display:grid;grid-template-columns:1fr 340px;gap:32px;}
        @media(max-width:800px){.page{grid-template-columns:1fr;}}
        
        /* SECTIONS */
        .section{background:#1a1a2e;border-radius:16px;padding:24px;margin-bottom:20px;border:1px solid #2a2a3e;}
        .section-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;}
        .section-title{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:#666;font-weight:700;}
        .section-badge{font-size:10px;color:#666;background:#0a0a14;border:1px solid #2a2a3e;padding:3px 8px;border-radius:4px;}
        
        /* AIRCRAFT HEADER */
        .back{color:#666;text-decoration:none;font-size:14px;display:inline-block;margin-bottom:16px;}
        .back:hover{color:#ff6b35;}
        .tail-reg{font-size:13px;color:#666;font-family:monospace;letter-spacing:2px;margin-bottom:4px;}
        .listing-title{font-size:34px;font-weight:800;line-height:1.1;margin-bottom:6px;}
        .listing-subtitle{font-size:15px;color:#aaa;margin-bottom:16px;}
        .badges{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px;}
        .badge{padding:4px 14px;border-radius:20px;font-size:12px;font-weight:600;}
        .badge-orange{background:rgba(255,107,53,0.15);color:#ff6b35;border:1px solid rgba(255,107,53,0.3);}
        .badge-gray{background:rgba(255,255,255,0.05);color:#aaa;border:1px solid #333;}
        .badge-green{background:rgba(76,175,80,0.15);color:#4caf50;border:1px solid rgba(76,175,80,0.3);}

        /* HIGHLIGHTS */
        .highlight-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid #2a2a3e;font-size:14px;color:#ccc;}
        .highlight-item:last-child{border-bottom:none;}
        .highlight-check{color:#4caf50;flex-shrink:0;}

        /* SPECS GRID */
        .specs-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:#2a2a3e;border-radius:10px;overflow:hidden;}
        .spec-item{background:#0d0d1a;padding:14px 16px;}
        .spec-label{font-size:10px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;}
        .spec-value{font-size:16px;font-weight:700;font-family:monospace;color:white;}

        /* DESCRIPTION */
        .desc-line{padding:8px 0;border-bottom:1px solid #2a2a3e;font-size:14px;color:#ccc;line-height:1.5;}
        .desc-line:last-child{border-bottom:none;}
        .desc-category{font-size:10px;color:#ff6b35;text-transform:uppercase;letter-spacing:1px;font-weight:700;margin-top:16px;margin-bottom:4px;}

        /* HISTORY SECTIONS — locked */
        .locked{text-align:center;padding:32px;color:#444;}
        .locked-icon{font-size:32px;margin-bottom:8px;}
        .locked-title{font-size:14px;color:#555;margin-bottom:8px;}
        .locked-cta{display:inline-block;background:#ff6b35;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:700;margin-top:8px;}

        /* SIDEBAR */
        .price-card{background:#1a1a2e;border-radius:16px;padding:24px;border:1px solid #2a2a3e;margin-bottom:16px;}
        .price-label{font-size:11px;color:#666;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}
        .price-amount{font-size:36px;font-weight:800;color:#ff6b35;font-family:monospace;line-height:1;}
        .price-note{font-size:12px;color:#666;margin-top:4px;}
        .hours-row{display:flex;gap:16px;margin-top:16px;padding-top:16px;border-top:1px solid #2a2a3e;}
        .hours-item{flex:1;}
        .hours-label{font-size:10px;color:#666;text-transform:uppercase;letter-spacing:1px;}
        .hours-value{font-size:20px;font-weight:700;font-family:monospace;margin-top:2px;}
        .location-row{margin-top:16px;padding-top:16px;border-top:1px solid #2a2a3e;font-size:13px;color:#666;}
        .location-row span{color:#aaa;}
        .contact-card{background:#1a1a2e;border-radius:16px;padding:24px;border:1px solid #2a2a3e;margin-bottom:16px;}
        .btn-contact{display:block;background:#ff6b35;color:white;text-align:center;padding:14px;border-radius:10px;text-decoration:none;font-weight:700;font-size:15px;margin-bottom:8px;}
        .btn-contact:hover{background:#e55a25;}
        .contact-name{font-size:15px;font-weight:600;margin-bottom:2px;}
        .contact-email{font-size:13px;color:#666;margin-bottom:16px;}
        .views-count{font-size:11px;color:#444;text-align:center;margin-top:8px;}
        .ai-btn{display:block;background:transparent;border:1px solid #ff6b35;color:#ff6b35;text-align:center;padding:12px;border-radius:10px;font-size:13px;cursor:pointer;width:100%;margin-top:8px;}
        .ai-btn:hover{background:#ff6b35;color:white;}
        .registry-card{background:#1a1a2e;border-radius:16px;padding:20px;border:1px solid #2a2a3e;}
        .reg-row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #2a2a3e;font-size:13px;}
        .reg-row:last-child{border-bottom:none;}
        .reg-label{color:#666;}
        .reg-value{color:#aaa;font-family:monospace;}
        .spinner{display:inline-block;width:16px;height:16px;border:2px solid #333;border-top-color:#ff6b35;border-radius:50%;animation:spin 0.8s linear infinite;}
        @keyframes spin{to{transform:rotate(360deg);}}
    </style>
</head>
<body>
<div class="header">
    <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    <div class="nav">
        <a href="/aircraft-for-sale">All listings</a>
        {% if current_user.is_authenticated %}<a href="/my-logbook">My logbook</a>
        {% else %}<a href="/login">Log in</a><a href="/register" class="primary">Sign up</a>{% endif %}
    </div>
</div>

<!-- HERO -->
<div class="hero-wrap">
    {% if images %}
    <img class="hero-img" id="hero-img" src="{{ images[0] }}" alt="{{ listing.tail }}">
    {% if images|length > 1 %}
    <button class="hero-nav hero-nav-left" onclick="navHero(-1)">&#8592;</button>
    <button class="hero-nav hero-nav-right" onclick="navHero(1)">&#8594;</button>
    <div class="hero-counter" id="hero-counter">1 / {{ images|length }}</div>
    {% endif %}
    {% else %}
    <div class="hero-placeholder">✈️</div>
    {% endif %}
</div>

<!-- INFO BAR -->
<div class="info-bar">
    {% if listing.hours_engine and listing.hours_engine_tbo %}
    {% set eng_pct = (listing.hours_engine / listing.hours_engine_tbo * 100)|int %}
    <div class="info-bar-gauge">
        <div class="info-bar-gauge-lbl">ENG · SMOH/TBO</div>
        <canvas class="gauge-canvas" width="110" height="68" data-pct="{{ eng_pct }}" data-cx="55" data-cy="62" data-r="44"></canvas>
        <div class="info-bar-gauge-val">{{ listing.hours_engine|int }}h / {{ listing.hours_engine_tbo|int }}h</div>
    </div>
    {% endif %}
    {% if listing.hours_total %}
    {% set af_pct = [listing.hours_total / 10000 * 100, 100]|min|int %}
    <div class="info-bar-gauge">
        <div class="info-bar-gauge-lbl">AIRFRAME · TT</div>
        <canvas class="gauge-canvas" width="110" height="68" data-pct="{{ af_pct }}" data-label="{{ listing.hours_total|int }}h" data-cx="55" data-cy="62" data-r="44"></canvas>
        <div class="info-bar-gauge-val">{{ listing.hours_total|int }}h TT</div>
    </div>
    {% endif %}
    {% if listing.hours_prop and listing.hours_prop_tbo %}
    {% set prop_pct = (listing.hours_prop / listing.hours_prop_tbo * 100)|int %}
    <div class="info-bar-gauge">
        <div class="info-bar-gauge-lbl">PROP · OH</div>
        <canvas class="gauge-canvas" width="110" height="68" data-pct="{{ prop_pct }}" data-cx="55" data-cy="62" data-r="44"></canvas>
        <div class="info-bar-gauge-val">{{ listing.hours_prop|int }}h / {{ listing.hours_prop_tbo|int }}h</div>
    </div>
    {% endif %}
    <div style="display:flex;align-items:center;gap:8px;flex-wrap:nowrap;">
        {% if listing.has_autopilot %}<span class="hbadge yes">✓ Autopilot</span>{% endif %}
        {% if listing.has_adsb %}<span class="hbadge yes">✓ ADS-B</span>{% endif %}
        {% if listing.is_hangared %}<span class="hbadge yes">✓ Hangared</span>{% endif %}
        {% if listing.arc_verified %}<span class="hbadge yes">✓ ARC</span>{% endif %}
    </div>
    {% if images|length > 1 %}
    <div style="display:flex;gap:6px;overflow-x:auto;flex:1;">
        {% for img in images %}
        <img class="thumb {% if loop.first %}active{% endif %}" src="{{ img }}" onclick="setHero({{ loop.index0 }})" style="width:64px;height:46px;object-fit:cover;border-radius:6px;cursor:pointer;border:2px solid transparent;flex-shrink:0;opacity:0.7;">
        {% endfor %}
    </div>
    {% endif %}
</div>

<!-- PAGE -->
<div class="page">
    <!-- LEFT COLUMN -->
    <div>
        <a href="/aircraft-for-sale" class="back">← Back to listings</a>
        
        <div class="tail-reg">{{ listing.tail }}</div>
        <h1 class="listing-title">{{ listing.manufacturer }} {{ listing.model }}</h1>
        <div class="listing-subtitle">{{ listing.year }}{% if listing.location %} · {{ listing.location }}{% endif %}</div>
        <div class="badges">
            {% if listing.condition %}<span class="badge badge-orange">{{ listing.condition|title }}</span>{% endif %}
            {% if listing.seller_type %}<span class="badge badge-gray">{{ listing.seller_type|title }}</span>{% endif %}
            {% if listing.arc_verified %}<span class="badge badge-green">✓ ARC Verified</span>{% endif %}
        </div>

        <!-- HIGHLIGHTS -->
        {% if highlights %}
        <div class="section">
            <div class="section-header">
                <div class="section-title">Highlights</div>
            </div>
            {% for h in highlights %}
            <div class="highlight-item"><span class="highlight-check">✓</span><span>{{ h }}</span></div>
            {% endfor %}
        </div>
        {% endif %}

        <!-- HOURS GAUGES -->
        {% if listing.hours_total or listing.hours_engine or listing.hours_prop %}
        <div class="section">
            <div class="section-header"><div class="section-title">Airframe & Engine</div></div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:16px;">
                {% if listing.hours_total %}
                <div style="background:#0d0d1a;border:1px solid #1a2a1a;border-radius:10px;padding:16px;text-align:center;">
                    <div style="font-size:10px;color:#4a8a4a;text-transform:uppercase;letter-spacing:2px;margin-bottom:8px;">Airframe TT</div>
                    <div style="font-size:28px;font-weight:800;font-family:monospace;color:white;">{{ listing.hours_total|int }}</div>
                    <div style="font-size:10px;color:#456;margin-top:4px;">hours</div>
                </div>
                {% endif %}
                {% if listing.hours_engine %}
                <div style="background:#0d0d1a;border:1px solid #1a2a1a;border-radius:10px;padding:16px;text-align:center;">
                    <div style="font-size:10px;color:#4a8a4a;text-transform:uppercase;letter-spacing:2px;margin-bottom:8px;">Engine SMOH</div>
                    <div style="font-size:28px;font-weight:800;font-family:monospace;color:white;">{{ listing.hours_engine|int }}</div>
                    <div style="font-size:10px;color:#456;margin-top:4px;">hours</div>
                </div>
                {% endif %}
                {% if listing.hours_prop %}
                <div style="background:#0d0d1a;border:1px solid #1a2a1a;border-radius:10px;padding:16px;text-align:center;">
                    <div style="font-size:10px;color:#4a8a4a;text-transform:uppercase;letter-spacing:2px;margin-bottom:8px;">Prop</div>
                    <div style="font-size:28px;font-weight:800;font-family:monospace;color:white;">{{ listing.hours_prop|int }}</div>
                    <div style="font-size:10px;color:#456;margin-top:4px;">hours</div>
                </div>
                {% endif %}
            </div>
        </div>
        {% endif %}

        <!-- SPECS -->
        {% if specs %}
        <div class="section">
            <div class="section-header"><div class="section-title">Specifications</div></div>
            <div class="specs-grid">
                {% if specs.engine %}<div class="spec-item"><div class="spec-label">Engine</div><div class="spec-value" style="font-size:13px">{{ specs.engine }}</div></div>{% endif %}
                {% if specs.avionics %}<div class="spec-item"><div class="spec-label">Avionics</div><div class="spec-value" style="font-size:13px">{{ specs.avionics }}</div></div>{% endif %}
                {% if specs.seats %}<div class="spec-item"><div class="spec-label">Seats</div><div class="spec-value">{{ specs.seats }}</div></div>{% endif %}
                {% if specs.cruise_kt %}<div class="spec-item"><div class="spec-label">Cruise</div><div class="spec-value">{{ specs.cruise_kt }} kt</div></div>{% endif %}
                {% if specs.range_nm %}<div class="spec-item"><div class="spec-label">Range</div><div class="spec-value">{{ specs.range_nm }} nm</div></div>{% endif %}
                {% if specs.useful_load_kg %}<div class="spec-item"><div class="spec-label">Useful load</div><div class="spec-value">{{ specs.useful_load_kg }} kg</div></div>{% endif %}
            </div>
        </div>
        {% endif %}

        <!-- AI DESCRIPTION -->
        {% if listing.ai_description %}
        <div class="section">
            <div class="section-header"><div class="section-title">About this aircraft</div><div class="section-badge">✦ AI Summary</div></div>
            <div style="color:#aaa;font-size:14px;line-height:1.8;">{{ listing.ai_description }}</div>
        </div>
        {% endif %}

        <!-- FULL DESCRIPTION -->
        {% if listing.description %}
        <div class="section">
            <div class="section-header"><div class="section-title">Full details</div></div>
            {%- set ns = namespace(category="") -%}
            {%- set lines = listing.description.split("
") -%}
            {%- for line in lines -%}
            {%- set stripped = line.strip() -%}
            {%- if stripped and not stripped.startswith("Highlights:") and not stripped.startswith("Engine:") -%}
            {%- if stripped == "Avionics:" %}
            <div class="desc-category">Avionics</div>
            {%- set ns.category = "avionics" -%}
            {%- elif stripped == "Additional Remarks:" or stripped.startswith("Additional Remarks:") %}
            <div class="desc-category">Additional remarks</div>
            {%- set ns.category = "remarks" -%}
            {%- if stripped|length > 19 -%}
            {%- for item in stripped[19:].split(";") -%}
            {%- if item.strip() %}<div class="desc-line">{{ item.strip() }}</div>{%- endif -%}
            {%- endfor -%}
            {%- endif -%}
            {%- elif stripped == "Maintenance:" or stripped.startswith("Maintenance:") %}
            <div class="desc-category">Maintenance</div>
            {%- set ns.category = "maintenance" -%}
            {%- if stripped|length > 12 -%}
            {%- for item in stripped[12:].split(";") -%}
            {%- if item.strip() %}<div class="desc-line">{{ item.strip() }}</div>{%- endif -%}
            {%- endfor -%}
            {%- endif -%}
            {%- elif ns.category == "avionics" -%}
            {%- for item in stripped.split(";") -%}
            {%- if item.strip() %}<div class="desc-line">{{ item.strip() }}</div>{%- endif -%}
            {%- endfor -%}
            {%- elif ns.category == "remarks" -%}
            {%- for item in stripped.split(";") -%}
            {%- if item.strip() %}<div class="desc-line">{{ item.strip() }}</div>{%- endif -%}
            {%- endfor -%}
            {%- elif ns.category == "maintenance" -%}
            {%- for item in stripped.split(";") -%}
            {%- if item.strip() %}<div class="desc-line">{{ item.strip() }}</div>{%- endif -%}
            {%- endfor -%}
            {%- else %}
            <div class="desc-line">{{ stripped }}</div>
            {%- endif %}
            {%- endif -%}
            {%- endfor -%}
        </div>
        {% endif %}

        <!-- MAINTENANCE HISTORY — locked -->
        <div class="section">
            <div class="section-header">
                <div class="section-title">Maintenance history</div>
                <div class="section-badge">Coming soon</div>
            </div>
            {% if listing.arc_verified %}
            <div style="padding:8px 0;font-size:14px;color:#4caf50;">✓ ARC verified by PanPanParts</div>
            {% if listing.arc_valid_until %}
            <div style="padding:8px 0;font-size:13px;color:#aaa;">Valid until: {{ listing.arc_valid_until }}</div>
            {% endif %}
            {% else %}
            <div class="locked">
                <div class="locked-icon">🔧</div>
                <div class="locked-title">No maintenance records yet</div>
                <div style="font-size:12px;color:#444;margin-bottom:8px;">Own this aircraft? Claim it to add service history, ARC documents and more.</div>
                <a href="/register" class="locked-cta">Claim this aircraft</a>
            </div>
            {% endif %}
        </div>

        <!-- DOCUMENTS — locked -->
        <div class="section">
            <div class="section-header">
                <div class="section-title">Documents</div>
                <div class="section-badge">Coming soon</div>
            </div>
            <div class="locked">
                <div class="locked-icon">📄</div>
                <div class="locked-title">No documents uploaded</div>
                <div style="font-size:12px;color:#444;margin-bottom:8px;">ARC, weight & balance, STC certificates and logbook scans will appear here.</div>
                <a href="/register" class="locked-cta">Claim this aircraft</a>
            </div>
        </div>

        <!-- AI ANALYSIS -->
        <div class="section" id="ai-insight-card">
            <div class="section-header">
                <div class="section-title">✦ AI Aircraft Analysis</div>
                <button class="ai-btn" id="btn-ai-insight" onclick="loadAIInsight()" style="width:auto;padding:6px 14px;">Analyze →</button>
            </div>
            <div id="ai-insight-loading" style="display:none;text-align:center;padding:24px;color:#666;">
                <div class="spinner"></div>
                <div style="margin-top:8px;font-size:13px;">AI is analyzing this aircraft...</div>
            </div>
            <div id="ai-insight-content" style="display:none;">
                <div id="insight-character" style="color:#ccc;font-size:14px;line-height:1.7;margin-bottom:16px;font-style:italic;"></div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
                    <div>
                        <div style="font-size:10px;text-transform:uppercase;letter-spacing:1px;color:#4caf50;margin-bottom:8px;">Strengths</div>
                        <div id="insight-strengths"></div>
                    </div>
                    <div>
                        <div style="font-size:10px;text-transform:uppercase;letter-spacing:1px;color:#f44336;margin-bottom:8px;">Considerations</div>
                        <div id="insight-weaknesses"></div>
                    </div>
                </div>
                <div id="insight-recommendation" style="border-top:1px solid #2a2a3e;padding-top:16px;font-size:13px;color:#ff6b35;line-height:1.6;"></div>
            </div>
        </div>
    </div>

    <!-- RIGHT SIDEBAR -->
    <div>
        <!-- PRICE CARD -->
        <div class="price-card">
            <div class="price-label">Asking price</div>
            <div class="price-amount">
                {% if listing.price and listing.price > 0 %}EUR {{ "{:,.0f}".format(listing.price) }}
                {% else %}Price on request{% endif %}
            </div>
            {% if listing.hours_total or listing.hours_engine %}
            <div class="hours-row">
                {% if listing.hours_total %}<div class="hours-item"><div class="hours-label">Airframe TT</div><div class="hours-value">{{ listing.hours_total|int }}h</div></div>{% endif %}
                {% if listing.hours_engine %}<div class="hours-item"><div class="hours-label">Engine SMOH</div><div class="hours-value">{{ listing.hours_engine|int }}h</div></div>{% endif %}
            </div>
            {% endif %}
            {% if listing.location %}
            <div class="location-row">📍 <span>{{ listing.location }}</span></div>
            {% endif %}
        </div>

        <!-- CONTACT -->
        <div class="contact-card">
            <div class="section-title" style="margin-bottom:16px;">Listed by</div>
            <div class="contact-name">{{ listing.contact_name or 'Seller' }}</div>
            <div class="contact-email">{{ listing.contact_email or '' }}</div>
            {% if listing.source_url %}
            <a href="{{ listing.source_url }}" target="_blank" class="btn-contact">View original listing →</a>
            {% else %}
            <a href="mailto:{{ listing.contact_email }}" class="btn-contact">✉ Send message</a>
            {% endif %}
            <div class="views-count">{{ listing.views or 0 }} views</div>
        </div>

        <!-- REGISTRY INFO -->
        <div class="registry-card">
            <div class="section-title" style="margin-bottom:16px;">Registry</div>
            <div class="reg-row"><span class="reg-label">Registration</span><span class="reg-value">{{ listing.tail }}</span></div>
            <div class="reg-row"><span class="reg-label">Year</span><span class="reg-value">{{ listing.year or '—' }}</span></div>
            <div class="reg-row"><span class="reg-label">Condition</span><span class="reg-value">{{ listing.condition|title if listing.condition else '—' }}</span></div>
            <div class="reg-row"><span class="reg-label">Seller type</span><span class="reg-value">{{ listing.seller_type|title if listing.seller_type else '—' }}</span></div>
            {% if listing.source %}
            <div class="reg-row"><span class="reg-label">Source</span><span class="reg-value">{{ listing.source|title }}</span></div>
            {% endif %}
        </div>
    </div>
</div>

<script>
var allImages = [{% for img in images %}'{{ img }}'{% if not loop.last %},{% endif %}{% endfor %}];
var currentIdx = 0;
function setHero(idx) {
    currentIdx = idx;
    document.getElementById('hero-img').src = allImages[idx];
    document.querySelectorAll('.thumb').forEach((t,i) => t.classList.toggle('active', i===idx));
    var ctr = document.getElementById('hero-counter');
    if(ctr) ctr.textContent = (idx+1) + ' / ' + allImages.length;
}
function navHero(dir) {
    var next = (currentIdx + dir + allImages.length) % allImages.length;
    setHero(next);
}

document.querySelectorAll('.gauge-canvas').forEach(function(canvas) {
    var pct = parseInt(canvas.dataset.pct) || 0;
    var label = canvas.dataset.label || (pct + '%');
    var ctx = canvas.getContext('2d');
    var cx = parseInt(canvas.dataset.cx) || Math.round(canvas.width/2);
    var cy = parseInt(canvas.dataset.cy) || Math.round(canvas.height*0.88);
    var r = parseInt(canvas.dataset.r) || Math.round(canvas.width*0.40);
    var startAngle = Math.PI;
    var endAngle = 2 * Math.PI;
    var color = pct < 50 ? '#4caf50' : (pct < 75 ? '#ffc107' : '#f44336');
    ctx.beginPath(); ctx.arc(cx, cy, r, startAngle, endAngle);
    ctx.strokeStyle = '#1a2a1a'; ctx.lineWidth = 12; ctx.lineCap = 'butt'; ctx.stroke();
    var grad = ctx.createLinearGradient(14, 0, 116, 0);
    grad.addColorStop(0, '#4caf50'); grad.addColorStop(0.55, '#ffc107'); grad.addColorStop(1, '#f44336');
    ctx.beginPath(); ctx.arc(cx, cy, r, startAngle, endAngle);
    ctx.strokeStyle = grad; ctx.globalAlpha = 0.8; ctx.stroke(); ctx.globalAlpha = 1;
    var angle = Math.PI + (pct / 100) * Math.PI;
    var nx = cx + r * Math.cos(angle);
    var ny = cy + r * Math.sin(angle);
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(nx, ny);
    ctx.strokeStyle = '#000'; ctx.lineWidth = 4; ctx.lineCap = 'round';
    ctx.globalAlpha = 0.4; ctx.stroke(); ctx.globalAlpha = 1;
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(nx, ny);
    ctx.strokeStyle = '#fff'; ctx.lineWidth = 2.5; ctx.stroke();
    ctx.beginPath(); ctx.arc(cx, cy, 5, 0, 2*Math.PI);
    ctx.fillStyle = '#0d0d1a'; ctx.fill();
    ctx.strokeStyle = color; ctx.lineWidth = 1.5; ctx.stroke();
    ctx.beginPath(); ctx.arc(cx, cy, 2, 0, 2*Math.PI);
    ctx.fillStyle = color; ctx.fill();
    ctx.fillStyle = color; ctx.font = 'bold 12px monospace';
    ctx.textAlign = 'center'; ctx.fillText(label || pct + '%', cx, 62);
});

async function loadAIInsight() {
    document.getElementById('btn-ai-insight').style.display = 'none';
    document.getElementById('ai-insight-loading').style.display = 'block';
    try {
        const resp = await fetch('/aircraft-listing/{{ listing.id }}/ai-insight', {method:'POST', headers:{'Content-Type':'application/json'}});
        const data = await resp.json();
        document.getElementById('ai-insight-loading').style.display = 'none';
        document.getElementById('ai-insight-content').style.display = 'block';
        document.getElementById('insight-character').textContent = data.character || '';
        const str = document.getElementById('insight-strengths');
        (data.strengths||[]).forEach(s => { const d=document.createElement('div'); d.style.cssText='font-size:13px;color:#ccc;padding:4px 0;border-bottom:1px solid #2a2a3e;'; d.textContent='✓ '+s; str.appendChild(d); });
        const weak = document.getElementById('insight-weaknesses');
        (data.weaknesses||[]).forEach(w => { const d=document.createElement('div'); d.style.cssText='font-size:13px;color:#ccc;padding:4px 0;border-bottom:1px solid #2a2a3e;'; d.textContent='• '+w; weak.appendChild(d); });
        document.getElementById('insight-recommendation').textContent = data.recommendation || '';
    } catch(e) {
        document.getElementById('ai-insight-loading').innerHTML = '<div style="color:#f44336;font-size:13px;">Analysis failed. Please try again.</div>';
    }
}
</script>
</body>
</html>"""


@app.route('/aircraft-listing/<int:listing_id>/ai-insight', methods=['POST'])
def aircraft_listing_ai_insight(listing_id):
    import json as _json
    listing = AircraftListing.query.get_or_404(listing_id)
    data = request.get_json() or {}
    user_hours = data.get('user_hours')
    user_license = data.get('user_license')

    aircraft_info = f"""
Aircraft: {listing.manufacturer} {listing.model} ({listing.year})
Registration: {listing.tail}
Total time: {listing.hours_total or 'unknown'} hours
Engine SMOH: {listing.hours_engine or 'unknown'} hours
Engine TBO: {listing.hours_engine_tbo or 'unknown'} hours
Price: EUR {listing.price or 'unknown'}
Location: {listing.location or 'unknown'}
Condition: {listing.condition or 'unknown'}
Has autopilot: {listing.has_autopilot}
Has ADS-B: {listing.has_adsb}
Is hangared: {listing.is_hangared}
Description: {listing.description or ''}
"""

    buyer_info = ""
    if user_hours and user_license:
        buyer_info = f"""
Potential buyer profile:
- Total flight hours: {user_hours}
- License type: {user_license}
"""

    try:
        import anthropic as _anthropic
        client = _anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"""You are an expert aviation advisor. Analyze this aircraft listing and provide insights for a potential buyer.

{aircraft_info}
{buyer_info}

Return ONLY a JSON object with these fields:
{{
  "character": "2-3 sentence description of this aircraft type's flying characteristics, personality and typical use",
  "strengths": ["3-4 key strengths as short strings"],
  "weaknesses": ["2-3 honest weaknesses or considerations as short strings"],
  "economy": {{
    "fuel_burn_lph": estimated fuel burn in liters per hour as number or null,
    "cruise_speed_kt": cruise speed in knots as number or null,
    "range_nm": range in nautical miles as number or null,
    "cost_per_hour_eur": estimated total operating cost per hour in EUR as number or null,
    "note": "brief note on operating economics"
  }},
  "buyer_match": {{"score": "great/good/caution/mismatch", "reason": "1-2 sentences why this aircraft does or does not match the buyer profile"}} or null if no buyer profile,
  "recommendation": "1-2 sentence honest recommendation — who is this aircraft ideal for?"
}}

Be honest, specific and helpful. Use aviation expertise."""
            }]
        )
        text = response.content[0].text
        clean = text.replace("```json", "").replace("```", "").strip()
        result = _json.loads(clean)
        return _json.dumps({"ok": True, "data": result})
    except Exception as e:
        return _json.dumps({"ok": False, "error": str(e)})


@app.route('/admin/status')
def admin_status():
    conn = get_pg_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM aircraft_listing")
    total = cur.fetchone()[0]
    cur.execute("SELECT source, COUNT(*) FROM aircraft_listing GROUP BY source")
    sources = cur.fetchall()
    cur.execute("SELECT id, tail, manufacturer, model FROM aircraft_listing WHERE source='winglist' LIMIT 5")
    winglist = cur.fetchall()
    conn.close()
    result = f"Total: {total}<br><br>Sources:<br>"
    for s in sources:
        result += f"  {s[0]}: {s[1]}<br>"
    result += "<br>Winglist sample:<br>"
    for w in winglist:
        result += f"  {w}<br>"
    return result

@app.route('/admin/migrate')
def admin_migrate():
    conn = get_pg_conn()
    cur = conn.cursor()
    results = []
    for col, typ in [('source_url','TEXT'),('source','TEXT'),('ai_description','TEXT'),('status','TEXT')]:
        try:
            cur.execute('ALTER TABLE part ADD COLUMN source TEXT')
            cur.execute('ALTER TABLE part ADD COLUMN source_url TEXT')
            cur.execute('ALTER TABLE part ADD COLUMN title TEXT')
            conn.commit()
        except: conn.rollback()
        try:
            cur.execute(f"ALTER TABLE aircraft_listing ADD COLUMN {col} {typ}")
            conn.commit()
            results.append(f"Added {col}")
        except Exception as e:
            conn.rollback()
            results.append(f"{col}: {str(e)[:50]}")
    for col in ['source','source_url','title']:
        try:
            cur.execute(f"ALTER TABLE part ADD COLUMN {col} TEXT")
            conn.commit()
            results.append(f"part.{col} added")
        except Exception as e:
            conn.rollback()
            results.append(f"part.{col}: {str(e)[:40]}")
    conn.close()
    return "<br>".join(results)

@app.route('/admin/test-barnstormers')
def admin_test_barnstormers():
    import requests as _req
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.com',
        }
        resp = _req.get('https://www.barnstormers.com/classified_cats.php?cat=Parts', headers=headers, timeout=15)
        return f"Status: {resp.status_code}, Bytes: {len(resp.text)}, First 500 chars: {resp.text[:500]}"
    except Exception as e:
        return f"FEJL: {e}"

@app.route('/admin/test-scrape')
def admin_test_scrape():
    import requests as _req
    try:
        resp = _req.get('https://www.winglist.aero/', timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        return f"Status: {resp.status_code}, Bytes: {len(resp.text)}"
    except Exception as e:
        return f"FEJL: {e}"


@app.route('/admin/import-barnstormers-parts')
def admin_import_barnstormers_parts():
    import requests as _req, time as _time, re as _re
    from bs4 import BeautifulSoup as _BS
    BASE = 'https://www.barnstormers.com'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://www.barnstormers.com/'}
    conn = get_pg_conn()
    cur = conn.cursor()
    imported = skipped = errors = 0
    err_msgs = []
    for page in range(1, 6):
        try:
            resp = _req.get(BASE + '/listing.php?cat=Parts&page=' + str(page), headers=HEADERS, timeout=15)
            soup = _BS(resp.text, 'html.parser')
            ads = soup.find_all('div', class_='classified_single')
            if not ads: break
            for ad in ads:
                try:
                    adid = ad.get('data-adid', '')
                    title_tag = ad.find('a', class_='listing_header')
                    title = title_tag.get_text(strip=True) if title_tag else ''
                    href = title_tag['href'] if title_tag else ''
                    if not href.startswith('http'): href = BASE + href
                    cur.execute('SELECT id FROM part WHERE source_url = %s', (href,))
                    if cur.fetchone():
                        skipped += 1
                        continue
                    body_tag = ad.find('span', class_='body')
                    description = body_tag.get_text(strip=True) if body_tag else ''
                    contact_tag = ad.find('span', class_='contact')
                    contact_text = contact_tag.get_text(' ', strip=True) if contact_tag else ''
                    price = None
                    pm = _re.search(r'\$[\d,]+', title + ' ' + description)
                    if pm:
                        try: price = float(pm.group().replace('$','').replace(',',''))
                        except: pass
                    phone = ''
                    phone_m = _re.search(r'[\d]{3}[-.\s][\d]{3}[-.\s][\d]{4}', contact_text)
                    if phone_m: phone = phone_m.group()
                    img = BASE + '/listing_images.php?id=' + adid if adid else None
                    cur.execute('INSERT INTO part (title, description, price, contact_phone, source, source_url, part_image) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                        (title, description, price, phone, 'barnstormers', href, img))
                    imported += 1
                except Exception as e:
                    errors += 1
                    err_msgs.append(str(e)[:80])
            _time.sleep(0.5)
        except Exception as e:
            err_msgs.append('Side ' + str(page) + ': ' + str(e)[:80])
            break
    conn.commit()
    conn.close()
    return 'Done! Importeret: ' + str(imported) + ', Sprunget over: ' + str(skipped) + ', Fejl: ' + str(errors) + '<br>' + '<br>'.join(err_msgs[:5])


@app.route('/admin/import-workshops')
def admin_import_workshops():
    import json as _json, re as _re
    conn = get_pg_conn()
    cur = conn.cursor()
    
    # Opret tabel hvis den ikke findes
    cur.execute("""CREATE TABLE IF NOT EXISTS maintenance_org (
        id SERIAL PRIMARY KEY,
        name TEXT,
        approval_number TEXT UNIQUE,
        address TEXT,
        country TEXT,
        city TEXT,
        email TEXT,
        phone TEXT,
        website TEXT,
        source TEXT,
        source_url TEXT,
        source_date TEXT,
        created_at TIMESTAMP DEFAULT NOW()
    )""")
    conn.commit()
    
    # Data fra scrape
    data = [
        {'name': 'AeroInterior ApS', 'approval_number': 'DK.145.0108', 'address': '5270 Odense N', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'AEROSERVICE ApS', 'approval_number': 'DK.145.0109', 'address': '2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Alsie A/S Sønderborg Lufthavn', 'approval_number': 'DK.145.0050', 'address': '6400 Sønderborg', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Greenland A/S', 'approval_number': 'DK.145.0025', 'address': '', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Service International A/S', 'approval_number': 'DK.145.0007', 'address': '7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Service Vamdrup ApS', 'approval_number': 'DK.145.0027', 'address': '6580 Vamdrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Atlantic Airways, Faroe Islands, P/F Vagar Airport', 'approval_number': 'DK.145.0009', 'address': 'FO-380 Sørvágur', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Avia Radio A/S Hangar', 'approval_number': 'DK.145.0033', 'address': 'Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Bel Air Aviation A/S Vestre', 'approval_number': 'DK.145.0094', 'address': '6705 Esbjerg Ø', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Benair A/S Stauning Lufthavn', 'approval_number': 'DK.145.0019', 'address': '6900 Skjern', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Bornholm Air Service ApS Søndre', 'approval_number': 'DK.145.0079', 'address': '3700 Rønne', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Cat Flyservice A/S', 'approval_number': 'DK.145.0015', 'address': '4000 Roskilde', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'CCS Maintenance ApS Hangar', 'approval_number': 'DK.145.0097', 'address': 'Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'CHEP Aerospace Solutions ApS Copenhagen Airport South, Building', 'approval_number': 'DK.145.0104', 'address': '280 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Classic Trim ApS', 'approval_number': 'DK.145.0072', 'address': '5330 Munkebo', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'DanCopter A/S DanCopter Allé', 'approval_number': 'DK.145.0070', 'address': '6705 Esbjerg Ø page 3 of 50', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Danish Aerotech A/S', 'approval_number': 'DK.145.0073', 'address': 'Karup Airbase 7470 Karup J', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Danish Air Transport A/S', 'approval_number': 'DK.145.0083', 'address': '6580 Vamdrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'DAO Aviation A/S Hangarvej H', 'approval_number': 'DK.145.0020', 'address': 'Københavns Lufthavn Roskilde 4000 Roskilde', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'F.O. Flyservice ApS', 'approval_number': 'DK.145.0076', 'address': '7400 Herning', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'General Aviation Service ApS Hangarvej A', 'approval_number': 'DK.145.0098', 'address': '4000 Roskilde', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Jet Time A/S', 'approval_number': 'DK.145.0091', 'address': '2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Kalundborg Aviation v/ Thorkild', 'approval_number': 'DK.145.0031', 'address': 'Kristensen Kalundborg Flyveplads 4593 Eskebjerg', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Lite Flite ApS v/John C. Holstein', 'approval_number': 'DK.145.0039', 'address': 'Koldingegnens Lufthavn 6580 Vamdrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Nordic Aviation Capital A/S', 'approval_number': 'DK.145.0018', 'address': '7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Nordisk Svejse Kontrol A/S Hammeren', 'approval_number': 'DK.145.0081', 'address': '6715 Esbjerg N', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'North Flying A/S Aalborg Lufthavn', 'approval_number': 'DK.145.0022', 'address': '9400 Nørresundby', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Northern Aerotech ApS Københavns Lufthavn Syd Bygn.', 'approval_number': 'DK.145.0103', 'address': '2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Scanaviation of', 'approval_number': 'DK.145.0107', 'address': '2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Scandinavian Aircraft Technologies', 'approval_number': 'DK.145.0078', 'address': 'A/S 9870 Sindal', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Scandinavian Avionics A/S', 'approval_number': 'DK.145.0075', 'address': '7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Skyways Technics A/S', 'approval_number': 'DK.145.0105', 'address': '6400 Sønderborg', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'ST Aerospace Solutions (Europe) A/S Amager', 'approval_number': 'DK.145.0092', 'address': '2770 Kastrup page 4 of 50', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Star Air A/S Hangar', 'approval_number': 'DK.145.0087', 'address': 'Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Sun-Air of Scandinavia A/S', 'approval_number': 'DK.145.0002', 'address': '7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Thomas Cook Airlines Scandinavia Københavns Lufthavn Syd', 'approval_number': 'DK.145.0049', 'address': 'A/S 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Thrane & Thrane A/S', 'approval_number': 'DK.145.0060', 'address': '2800 Kgs. Lyngby', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Uni-Fly A/S', 'approval_number': 'DK.145.0099', 'address': 'H. C. Andersen Airport 5270 Odense N', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Viking Life-Saving Equipment A/S Sædding', 'approval_number': 'DK.145.0102', 'address': '6710 Esbjerg V. page 5 of 50', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'AeroInterior ApS Approval No:', 'approval_number': 'DK.145.0108', 'address': 'Lufthavnvej 131 5270 Odense N', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'AEROSERVICE ApS Approval No:', 'approval_number': 'DK.145.0109', 'address': 'Oliefabriksvej 118 2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Alsie A/S Approval No:', 'approval_number': 'DK.145.0050', 'address': 'Sønderborg Lufthavn 6400 Sønderborg', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Greenland A/S Approval No:', 'approval_number': 'DK.145.0025', 'address': '3900 Nuuk Other approved addresses:', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Service International A/S Approval No:', 'approval_number': 'DK.145.0007', 'address': 'Stratusvej 1 7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Air Service Vamdrup ApS Approval No:', 'approval_number': 'DK.145.0027', 'address': 'Lufthavnsvej 7A 6580 Vamdrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Atlantic Airways, Faroe Islands, P/F Approval No:', 'approval_number': 'DK.145.0009', 'address': 'Vagar Airport FO-380 Sørvágur', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Avia Radio A/S Approval No:', 'approval_number': 'DK.145.0033', 'address': 'Hangar 141 Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Bel Air Aviation A/S Approval No:', 'approval_number': 'DK.145.0094', 'address': 'Vestre Lufthavnsvej 54 6705 Esbjerg Ø', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Benair A/S Approval No:', 'approval_number': 'DK.145.0019', 'address': 'Stauning Lufthavn 6900 Skjern', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Bornholm Air Service ApS Approval No:', 'approval_number': 'DK.145.0079', 'address': 'Søndre Landevej 2 3700 Rønne', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Cat Flyservice A/S Approval No:', 'approval_number': 'DK.145.0015', 'address': 'Lufthavnsvej 34 4000 Roskilde', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'CCS Maintenance ApS Approval No:', 'approval_number': 'DK.145.0097', 'address': 'Hangar 253 Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'CHEP Aerospace Solutions ApS Approval No:', 'approval_number': 'DK.145.0104', 'address': 'Copenhagen Airport South, Building 280 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Classic Trim ApS Approval No:', 'approval_number': 'DK.145.0072', 'address': 'Garbæksvej 10 5330 Munkebo', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'DanCopter A/S Approval No:', 'approval_number': 'DK.145.0070', 'address': 'DanCopter Allé 2 6705 Esbjerg Ø', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Danish Aerotech A/S Approval No:', 'approval_number': 'DK.145.0073', 'address': 'Herningvej 30 Karup Airbase 7470 Karup J', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Danish Air Transport A/S Approval No:', 'approval_number': 'DK.145.0083', 'address': 'Lufthavnsvej 7A 6580 Vamdrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'DAO Aviation A/S Approval No:', 'approval_number': 'DK.145.0020', 'address': 'Hangarvej H 1 Københavns Lufthavn Roskilde 4000 Roskilde', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'F.O. Flyservice ApS Approval No:', 'approval_number': 'DK.145.0076', 'address': 'Skinderholmvej 19 7400 Herning', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'General Aviation Service ApS Approval No:', 'approval_number': 'DK.145.0098', 'address': 'Hangarvej A 4 4000 Roskilde', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Jet Time A/S Approval No:', 'approval_number': 'DK.145.0091', 'address': 'Skøjtevej 27-31 2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Kalundborg Aviation v/ Thorkild Kristensen Approval No:', 'approval_number': 'DK.145.0031', 'address': 'Eskebjergvej 92 Kalundborg Flyveplads 4593 Eskebjerg', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Lite Flite ApS v/John C. Holstein Approval No:', 'approval_number': 'DK.145.0039', 'address': 'Lufthavnsvej 8A Koldingegnens Lufthavn 6580 Vamdrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Nordic Aviation Capital A/S Approval No:', 'approval_number': 'DK.145.0018', 'address': 'Stratusvej 12 7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Nordisk Svejse Kontrol A/S Approval No:', 'approval_number': 'DK.145.0081', 'address': 'Hammeren 5 6715 Esbjerg N', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'North Flying A/S Approval No:', 'approval_number': 'DK.145.0022', 'address': 'Aalborg Lufthavn 9400 Nørresundby', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Northern Aerotech ApS Approval No:', 'approval_number': 'DK.145.0103', 'address': 'Københavns Lufthavn Syd Bygn. 273 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Scanaviation of', 'approval_number': 'DK.145.0107', 'address': 'Amager Landevej 147 B 2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Scandinavian Aircraft Technologies A/S Approval No:', 'approval_number': 'DK.145.0078', 'address': 'Taagholtvej 178 9870 Sindal', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Scandinavian Avionics A/S Approval No:', 'approval_number': 'DK.145.0075', 'address': 'Stratusvej 9 7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Skyways Technics A/S Approval No:', 'approval_number': 'DK.145.0105', 'address': 'Lufthavnsvej 1B 6400 Sønderborg', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'ST Aerospace Solutions (Europe) A/S Approval No:', 'approval_number': 'DK.145.0092', 'address': 'Amager Strandvej 392 2770 Kastrup', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Star Air A/S Approval No:', 'approval_number': 'DK.145.0087', 'address': 'Hangar 243 Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Sun-Air of Scandinavia A/S Approval No:', 'approval_number': 'DK.145.0002', 'address': 'Cumulusvej 10 7190 Billund', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Thomas Cook Airlines Scandinavia A/S Approval No:', 'approval_number': 'DK.145.0049', 'address': 'Københavns Lufthavn Syd 2791 Dragør', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Thrane & Thrane A/S Approval No:', 'approval_number': 'DK.145.0060', 'address': 'Lundtoftegårdsvej 93D 2800 Kgs. Lyngby', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Uni-Fly A/S Approval No:', 'approval_number': 'DK.145.0099', 'address': 'Lufthavnsvej 131 H. C. Andersen Airport 5270 Odense N', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'},
        {'name': 'Viking Life-Saving Equipment A/S Approval No:', 'approval_number': 'DK.145.0102', 'address': 'Sædding Ringvej 13 6710 Esbjerg V.', 'country': 'Denmark', 'source': 'trafikstyrelsen', 'source_url': 'https://www.en.trafikstyrelsen.dk/media/13045/Approved%20Part-145%20Maintenance%20Organisations%20august%202015.pdf', 'source_date': '2015-08-03'}
    ]
    
    imported = skipped = 0
    for w in data:
        try:
            cur.execute("SELECT id FROM maintenance_org WHERE approval_number = %s", (w['approval_number'],))
            if cur.fetchone():
                skipped += 1
                continue
            cur.execute("INSERT INTO maintenance_org (name, approval_number, address, country, source, source_url, source_date) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (w['name'], w['approval_number'], w['address'], w['country'], w['source'], w['source_url'], w['source_date']))
            imported += 1
        except Exception as e:
            conn.rollback()
    conn.commit()
    conn.close()
    return f"Done! Importeret: {imported}, Sprunget over: {skipped}"

@app.route('/admin/scrape-winglist')
def admin_scrape_winglist():
    import requests as _req
    from bs4 import BeautifulSoup as _BS
    import re as _re
    import json as _json
    import time as _time

    BASE = "https://www.winglist.aero"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    def get_urls(page_url):
        resp = _req.get(page_url, headers=HEADERS, timeout=10)
        soup = _BS(resp.text, "html.parser")
        urls = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "/listings/" in href:
                if not href.startswith("http"): href = BASE + href
                if href not in urls: urls.append(href)
        return urls

    def ph(t):
        if not t: return None
        m = _re.search(r"(\d+)", str(t).replace(" ","").replace(",",""))
        try: return float(m.group(1)) if m else None
        except: return None

    def scrape(url):
        resp = _req.get(url, headers=HEADERS, timeout=10)
        soup = _BS(resp.text, "html.parser")
        d = {"source_url": url, "source": "winglist"}
        h1 = soup.find("h1")
        if h1: d["title"] = h1.get_text(strip=True)
        images = [img["src"] for img in soup.find_all("img", src=True) if "stwinglist01" in img["src"] and "/marketing/" not in img["src"]]
        d["images"] = images[:8]
        for dt in soup.find_all("dt"):
            dd = dt.find_next_sibling("dd")
            if dd: d[dt.get_text(strip=True).lower().strip(":").replace(" ","_")] = dd.get_text(" ", strip=True)
        pm = _re.search(r"(\d[\d\s]{2,})\s*(EUR|USD|GBP)", soup.get_text())
        if pm:
            try: d["price"] = int(pm.group(1).replace(" ","")); d["currency"] = pm.group(2)
            except: pass
        sections = []
        for h2 in soup.find_all(["h2","h3"]):
            st = h2.get_text(strip=True)
            if st in ["Highlights","Maintenance","Additional Remarks","Avionics","Engine"]:
                ul = h2.find_next("ul")
                if ul: sections.append(st+": "+"; ".join(li.get_text(strip=True) for li in ul.find_all("li")))
        d["description"] = "\n".join(sections)
        return d

    all_urls = set()
    import time as _time2
    for region in ["EU","NA","AS","AF"]:
        prev = set()
        for page in range(1, 50):
            urls = set(get_urls(BASE+f"/?region={region}&page={page}"))
            new = urls - all_urls
            all_urls |= urls
            if not new or urls == prev:
                break
            prev = urls
            _time2.sleep(0.2)
    all_urls = list(all_urls)

    conn = get_pg_conn()
    cur = conn.cursor()
    imported = skipped = errors = 0
    err_msgs = []

    batch = int(request.args.get('batch', 0))
    batch_size = 50
    start = batch * batch_size
    end = start + batch_size
    batch_urls = all_urls[start:end]
    total_urls = len(all_urls)
    for url in batch_urls:
        try:
            cur.execute("SELECT id FROM aircraft_listing WHERE source_url = %s", (url,))
            if cur.fetchone():
                skipped += 1
                continue
            d = scrape(url)
            title = d.get("title","")
            parts = title.split(" ", 2)
            year = parts[0] if parts and parts[0].isdigit() else d.get("year","")
            manufacturer = d.get("make", parts[1] if len(parts) > 1 else "")
            model = d.get("model", parts[2] if len(parts) > 2 else "")
            desc = d.get("description","")
            reg = d.get("registration","") or ("WING-"+str(imported+1))
            price_val = d.get("price") if isinstance(d.get("price"), (int, float)) else None
            cur.execute("INSERT INTO aircraft_listing (tail,manufacturer,model,year,price,location,condition,seller_type,hours_total,images,description,source_url,source,has_autopilot,has_adsb,contact_name,contact_email,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (reg, manufacturer, model, year, price_val, d.get("location",""), d.get("condition","Pre-owned"), d.get("seller_type",""), ph(d.get("total_time")), _json.dumps(d.get("images",[])), desc, url, "winglist", "autopilot" in desc.lower(), ("ads-b" in desc.lower() or "adsb" in desc.lower()), "Winglist Seller", "listings@winglist.aero", "active"))
            imported += 1
            _time.sleep(0.3)
        except Exception as e:
            errors += 1
            err_msgs.append(str(e)[:80])
            continue

    conn.commit()
    conn.close()
    return f"Batch {batch}: {start}-{min(end,total_urls)} af {total_urls}. Importeret: {imported}, Sprunget over: {skipped}, Fejl: {errors}. <br>Næste: <a href='/admin/scrape-winglist?batch={batch+1}'>Batch {batch+1}</a>" + "<br>".join(err_msgs[:5])


@app.route('/workshops')
def workshops():
    conn = get_pg_conn()
    cur = conn.cursor()
    cur.execute("SELECT name, approval_number, address, country FROM maintenance_org ORDER BY country, name")
    rows = cur.fetchall()
    conn.close()

    search = request.args.get('q', '').strip().lower()
    filter_type = request.args.get('type', '').strip().upper()
    filter_country = request.args.get('country', '').strip().upper()

    all_countries = sorted(set(r[3] for r in rows if r[3]))
    total = len(rows)

    def get_type(approval):
        if '.145.' in approval: return '145'
        if '.147.' in approval: return '147'
        if '.CAMO.' in approval or '.CAO.' in approval: return 'CAMO'
        return '145'

    filtered = []
    for r in rows:
        name, approval, address, country = r[0], r[1], r[2] or '', r[3] or 'Unknown'
        atype = get_type(approval)
        if search and search not in name.lower() and search not in approval.lower() and search not in country.lower():
            continue
        if filter_type and atype != filter_type:
            continue
        if filter_country and country.upper() != filter_country:
            continue
        filtered.append({'name': name, 'approval': approval, 'address': address, 'country': country, 'type': atype})

    by_country = {}
    for o in filtered:
        c = o['country']
        if c not in by_country: by_country[c] = []
        by_country[c].append(o)

    type_colors = {'145': '#ff6b35', '147': '#4caf50', 'CAMO': '#2196f3'}
    type_labels = {'145': 'Part-145 MRO', '147': 'Part-147 Training', 'CAMO': 'CAMO/CAO'}

    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Workshops - PanPanParts</title>
<style>
*{{box-sizing:border-box}}
body{{font-family:-apple-system,sans-serif;background:#0d0d1a;color:#fff;margin:0}}
.nav{{background:#0d0d1a;border-bottom:1px solid #1a1a2e;padding:16px 24px;display:flex;align-items:center;justify-content:space-between}}
.nav a{{color:#fff;text-decoration:none;font-size:14px;margin-left:16px}}
.logo{{font-size:20px;font-weight:800}}.logo span{{color:#ff6b35}}
.container{{max-width:1400px;margin:0 auto;padding:40px 20px}}
h1{{font-size:32px;margin-bottom:4px}}h1 span{{color:#ff6b35}}
.subtitle{{color:#666;margin-bottom:24px}}
.filters{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:32px;align-items:center}}
.filters input{{background:#1a1a2e;border:1px solid #2a2a3e;color:#fff;padding:10px 16px;border-radius:8px;font-size:14px;width:280px;outline:none}}
.filters input:focus{{border-color:#ff6b35}}
.filters select{{background:#1a1a2e;border:1px solid #2a2a3e;color:#fff;padding:10px 16px;border-radius:8px;font-size:14px;outline:none;cursor:pointer}}
.filters select:focus{{border-color:#ff6b35}}
.stats{{color:#888;font-size:13px;margin-bottom:24px}}
.stats span{{color:#ff6b35;font-weight:600}}
.country-section{{margin-bottom:40px}}
.country-title{{font-size:13px;text-transform:uppercase;letter-spacing:2px;color:#ff6b35;margin-bottom:12px;border-bottom:1px solid #1a1a2e;padding-bottom:8px;display:flex;justify-content:space-between}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}}
.card{{background:#1a1a2e;border-radius:10px;padding:16px;border:1px solid #2a2a3e;transition:border-color 0.2s}}
.card:hover{{border-color:#ff6b35}}
.card-name{{font-size:14px;font-weight:600;margin-bottom:6px;line-height:1.3}}
.card-approval{{font-size:11px;font-family:monospace;margin-bottom:8px;opacity:0.7}}
.badge{{display:inline-block;border-radius:4px;padding:2px 8px;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px}}
.no-results{{text-align:center;padding:60px;color:#666}}
</style></head><body>
<div class="nav"><a href="/" class="logo">PanPan<span>Parts</span></a><div>
<a href="/aircraft-for-sale">Aircraft for sale</a>
<a href="/parts">Parts for sale</a>
<a href="/workshops">Workshops</a>
</div></div>
<div class="container">
<h1>Certified <span>Workshops</span></h1>
<p class="subtitle">EASA approved maintenance, training and continuing airworthiness organisations worldwide</p>
<form method="get" class="filters">
<input type="text" name="q" placeholder="Search by name, country or approval number..." value="{search}">
<select name="type" onchange="this.form.submit()">
<option value="">All types</option>
<option value="145" {"selected" if filter_type=="145" else ""}>Part-145 MRO</option>
<option value="147" {"selected" if filter_type=="147" else ""}>Part-147 Training</option>
<option value="CAMO" {"selected" if filter_type=="CAMO" else ""}>CAMO/CAO</option>
</select>
<select name="country" onchange="this.form.submit()">
<option value="">All countries</option>
"""
    for c in all_countries:
        sel = 'selected' if filter_country == c.upper() else ''
        html += f'<option value="{c}" {sel}>{c.title()}</option>'
    html += f"""</select>
<button type="submit" style="background:#ff6b35;color:#fff;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-size:14px">Search</button>
</form>
<div class="stats">Showing <span>{len(filtered)}</span> of <span>{total}</span> organisations across <span>{len(by_country)}</span> countries</div>
"""
    if not filtered:
        html += '<div class="no-results">No organisations found. Try a different search.</div>'
    for country, orgs in sorted(by_country.items()):
        html += f'<div class="country-section"><div class="country-title"><span>🌍 {country.title()}</span><span>{len(orgs)} orgs</span></div><div class="grid">'
        for o in orgs:
            color = type_colors.get(o["type"], "#ff6b35")
            label = type_labels.get(o["type"], o["type"])
            html += f'''<div class="card">
<div class="card-name">{o["name"]}</div>
<div class="card-approval">{o["approval"]}</div>
<span class="badge" style="background:{color}22;color:{color};border:1px solid {color}44">{label}</span>
</div>'''
        html += '</div></div>'
    html += '</div></body></html>'
    return html


@app.route('/admin/import-easa-foreign')
def admin_import_easa_foreign():
    conn = get_pg_conn()
    cur = conn.cursor()
    imported = skipped = 0
    orgs = [{'name': 'GOODRICH AEROSTRUCTURES SERVICE CENTER - ASIA PTE Ltd.', 'approval_number': 'EASA.145.0003', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHROMALLOY (THAILAND) LTD.', 'approval_number': 'EASA.145.0005', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': '"UZBEKISTAN AIRWAYS TECHNICS" LIMITED LIABILITY COMPANY', 'approval_number': 'EASA.145.0007', 'country': 'UZBEKISTAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KUWAIT AIRWAYS COMPANY', 'approval_number': 'EASA.145.0008', 'country': 'KUWAIT', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ABU DHABI AVIATION', 'approval_number': 'EASA.145.0010', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR ASTANA JOINT STOCK COMPANY', 'approval_number': 'EASA.145.0015', 'country': 'KAZAKHSTAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AI ENGINEERING SERVICES LIMITED', 'approval_number': 'EASA.145.0016', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR MAURITIUS PLC', 'approval_number': 'EASA.145.0017', 'country': 'MAURITIUS', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRFOIL SERVICES SDN. BHD.', 'approval_number': 'EASA.145.0018', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AVIATION, ENGINE SERVICES - SING PTE. LTD.', 'approval_number': 'EASA.145.0019', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ALIA - THE ROYAL JORDANIAN AIRLINES PLC (ROYAL JORDANIAN)', 'approval_number': 'EASA.145.0020', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT MAINTENANCE AND ENGINEERING CORPORATION, BEIJING (AMECO)', 'approval_number': 'EASA.145.0021', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMSAFE AVIATION (CHONGQING) Ltd.', 'approval_number': 'EASA.145.0022', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ASIA PACIFIC AEROSPACE Pty. Ltd.', 'approval_number': 'EASA.145.0024', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ASIAN COMPRESSOR TECHNOLOGY SERVICES CO. LTD', 'approval_number': 'EASA.145.0025', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ASIAN SURFACE TECHNOLOGIES PTE LTD', 'approval_number': 'EASA.145.0026', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BAHRAIN AIRPORT SERVICES COMPANY BAS', 'approval_number': 'EASA.145.0028', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BET SHEMESH ENGINES Ltd.', 'approval_number': 'EASA.145.0031', 'country': 'ISRAEL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH AEROSPACE PTE LTD.', 'approval_number': 'EASA.145.0032', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHINA AIRCRAFT SERVICES Ltd.', 'approval_number': 'EASA.145.0037', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHINA AIRLINES Ltd.', 'approval_number': 'EASA.145.0038', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TURBOCHROME LTD.', 'approval_number': 'EASA.145.0039', 'country': 'ISRAEL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WINDSOR AIRMOTIVE ASIA PTE LTD', 'approval_number': 'EASA.145.0040', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHROMALLOY SA DE CV', 'approval_number': 'EASA.145.0041', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'COMPOSITE TECHNOLOGY INTERNATIONAL PTE LTD', 'approval_number': 'EASA.145.0043', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'COOPERATIVA AUTOGESTIONARIA DE SERVICIOS AERO INDUSTRIALES, R. L.', 'approval_number': 'EASA.145.0044', 'country': 'COSTA RICA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SABENA TECHNICS MIR', 'approval_number': 'EASA.145.0049', 'country': 'TUNISIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EAGLE SERVICES ASIA PTE. LTD.', 'approval_number': 'EASA.145.0050', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EL AL ISRAEL AIRLINES LTD', 'approval_number': 'EASA.145.0052', 'country': 'ISRAEL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EMIRATES', 'approval_number': 'EASA.145.0054', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EVERGREEN AVIATION TECHNOLOGIES CORPORATION', 'approval_number': 'EASA.145.0057', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FUEL ACCESSORY SERVICE TECHNOLOGIES PTE LTD.', 'approval_number': 'EASA.145.0061', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE ENGINE SERVICES MALAYSIA Sdn. Bh', 'approval_number': 'EASA.145.0066', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GUANGZHOU AIRCRAFT MAINTENANCE ENGINEERING Co. Ltd.', 'approval_number': 'EASA.145.0070', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GUANGZHOU HANGXIN AVIONICS Co. Ltd.', 'approval_number': 'EASA.145.0071', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULF AIR B.S.C. (C)', 'approval_number': 'EASA.145.0072', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ETIHAD AIRWAYS ENGINEERING L.L.C. T/A ETIHAD ENGINEERING TECHNICAL TRAININ', 'approval_number': 'EASA.145.0073', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL AEROSPACE SINGAPORE PTE Ltd.', 'approval_number': 'EASA.145.0076', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONG KONG AERO ENGINE SERVICES LIMITED (HAESL)', 'approval_number': 'EASA.145.0079', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONG KONG AIRCRAFT ENGINEERING COMPANY LIMITED (HAECO)', 'approval_number': 'EASA.145.0080', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'IBECA S.A.', 'approval_number': 'EASA.145.0081', 'country': 'CUBA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'IHI CORPORATION', 'approval_number': 'EASA.145.0084', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JORDAN AIRMOTIVE LIMITED COMPANY (JALCO)', 'approval_number': 'EASA.145.0090', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JORDAN AIRCRAFT MAINTENANCE Ltd.', 'approval_number': 'EASA.145.0091', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KOREAN AIRLINES Co.,Ltd', 'approval_number': 'EASA.145.0092', 'country': 'SOUTH KOREA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'W H BRENNAN & CO. PTE. LTD. LIMITED', 'approval_number': 'EASA.145.0093', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN ELECTRONICS & DEFENSE SERVIC ASIA PTE Ltd.', 'approval_number': 'EASA.145.0094', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LIEBHERR-SINGAPORE PTE LTD. (LIEBHERR AEROSPACE DIVISION)', 'approval_number': 'EASA.145.0095', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MAB ENGINEERING SERVICES SDN. BHD.', 'approval_number': 'EASA.145.0100', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN LANDING SYSTEMS SERVICES SINGAPORE PTE. LTD.', 'approval_number': 'EASA.145.0101', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MEXICANA MRO S.A. DE C.V.', 'approval_number': 'EASA.145.0102', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MITSUBISHI HEAVY INDUSTRIES AERO ENGINES, LTD.', 'approval_number': 'EASA.145.0104', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MOOG CONTROLS CORPORATION PHILIPPINE BRANCH', 'approval_number': 'EASA.145.0105', 'country': 'PHILIPPINES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MTU MAINTENANCE ZHUHAI Co., Ltd.', 'approval_number': 'EASA.145.0106', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'OMAN AIR (S.A.O.C.)', 'approval_number': 'EASA.145.0108', 'country': 'OMAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRATT & WHITNEY CANADA (SEA) PTE LT', 'approval_number': 'EASA.145.0109', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PAN ASIA PACIFIC AVIATION SERVICES LTD', 'approval_number': 'EASA.145.0112', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRATT & WHITNEY HOLDINGS SAS (PRATT & WHITNEY AIR NEW ZEALAND SERVICES)', 'approval_number': 'EASA.145.0113', 'country': 'NEW ZEALAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'QATAR AIRWAYS Q.C.S.C.', 'approval_number': 'EASA.145.0115', 'country': 'QATAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROCKWELL COLLINS SOUTHEAST ASIA PTE LTD LTD', 'approval_number': 'EASA.145.0117', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CIE NATIONALE ROYAL AIR MAROC', 'approval_number': 'EASA.145.0120', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRBUS NEW ZEALAND LIMITED', 'approval_number': 'EASA.145.0123', 'country': 'NEW ZEALAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAUDIA AEROSPACE ENGINEERING INDUSTRIES T/A SAUDIA TECHNIC', 'approval_number': 'EASA.145.0125', 'country': 'SAUDI ARABIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MADAGASCAR AIRLINES', 'approval_number': 'EASA.145.0127', 'country': 'MADAGASCAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SIA ENGINEERING COMPANY LIMITED', 'approval_number': 'EASA.145.0129', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SINGAPORE AERO ENGINE SERVICES PRIVATE LIMITED (SAESL)', 'approval_number': 'EASA.145.0131', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN AIRCRAFT ENGINE SERVICES MOROCCO', 'approval_number': 'EASA.145.0134', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TUNISAIR TECHNICS', 'approval_number': 'EASA.145.0135', 'country': 'TUNISIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ST ENGINEERING AEROSPACE ENGINES PTE LTD.', 'approval_number': 'EASA.145.0138', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ST ENGINEERING AEROSPACE SYSTEMS PTE LTD.', 'approval_number': 'EASA.145.0139', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ST ENGINEERING AEROSPACE SERVICES COMPANY PTE. LTD.', 'approval_number': 'EASA.145.0140', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SUMITOMO PRECISION PRODUCTS Co. Ltd', 'approval_number': 'EASA.145.0141', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROMANTENIMIENTO S.A.', 'approval_number': 'EASA.145.0142', 'country': 'EL SALVADOR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAIKOO (XIAMEN) AIRCRAFT ENGINEERING COMPANY LTD.', 'approval_number': 'EASA.145.0143', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TALLERES AERONAUTICOS DEL CARIBE S.A. (TAC)', 'approval_number': 'EASA.145.0144', 'country': 'DOMINICAN REPUBLIC', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TELAIR INTERNATIONAL SERVICES PTE. Ltd.', 'approval_number': 'EASA.145.0145', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THAI AIRWAYS INTERNATIONAL PUBLIC COMPANY LIMITED', 'approval_number': 'EASA.145.0147', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THALES SOLUTIONS ASIA PTE. LTD.', 'approval_number': 'EASA.145.0148', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SATAIR PTE. LTD.', 'approval_number': 'EASA.145.0149', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH TAECO AERONAUTICAL SYSTEMS XIAMEN Co. Ltd.', 'approval_number': 'EASA.145.0151', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TURBINE OVERHAUL SERVICES PTE. LTD.', 'approval_number': 'EASA.145.0152', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR NEW ZEALAND LTD.', 'approval_number': 'EASA.145.0159', 'country': 'NEW ZEALAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR ALGERIE TECHNICS', 'approval_number': 'EASA.145.0163', 'country': 'ALGERIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SOCIETE TUNISIENNE DE TRANSPORTS ET TRAVAUX AERIENS', 'approval_number': 'EASA.145.0176', 'country': 'TUNISIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TURK HAVA YOLLARI TEKNIK A.S.', 'approval_number': 'EASA.145.0276', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SICHUAN SERVICES AERO ENGINE MAINTENANCE Corp. Ltd.', 'approval_number': 'EASA.145.0289', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EGYPTAIR HOLDING COMPANY', 'approval_number': 'EASA.145.0290', 'country': 'EGYPT', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MIAT MONGOLIAN AIRLINES', 'approval_number': 'EASA.145.0293', 'country': 'MONGOLIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VAZDUHOPLOVNA AKADEMIJA AVIATION ACADEMY', 'approval_number': 'EASA.145.0298', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AUXITROL WESTON SINGAPORE PTE Ltd.', 'approval_number': 'EASA.145.0301', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JAT-TEHNIKA D.O.O.', 'approval_number': 'EASA.145.0304', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PARKER HANNIFIN (MALAYSIA) Sdn. Bhd.', 'approval_number': 'EASA.145.0308', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'A&P INTERNATIONAL SERVICES S.A.P.I. DE C.V.', 'approval_number': 'EASA.145.0309', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PT JAS AERO-ENGINEERING SERVICES (PTJAES)', 'approval_number': 'EASA.145.0310', 'country': 'INDONESIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HAMILTON SUNDSTRAND CUSTOMER SUPPORT CENTRE (MALAYSIA) Sdn. Bhd.', 'approval_number': 'EASA.145.0313', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'RBIH MIDDLE EAST FZE', 'approval_number': 'EASA.145.0314', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR SEYCHELLES Ltd.', 'approval_number': 'EASA.145.0324', 'country': 'SEYCHELLES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERODYNAMIC PTY LTD', 'approval_number': 'EASA.145.0325', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ENSAMBLADORES ELECTRONICOS DE MEXICO S. de R.L. de C.V.', 'approval_number': 'EASA.145.0328', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAIKOO (SHANDONG) AIRCRAFT ENGINEERING CO. Ltd.', 'approval_number': 'EASA.145.0339', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN AEROSYSTEMS SERVICES ASIA PTE. Ltd.', 'approval_number': 'EASA.145.0349', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROSPACE COMPONENT ENGINEERING (ACE) SERVICES PRIVATE LIMITED', 'approval_number': 'EASA.145.0350', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROTECHNIC INDUSTRIES', 'approval_number': 'EASA.145.0353', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ELBIT SYSTEMS Ltd.', 'approval_number': 'EASA.145.0355', 'country': 'ISRAEL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN LANDING SYSTEMS SERVICES AMERICAS S.A. DE C.V.', 'approval_number': 'EASA.145.0356', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SRILANKAN AIRLINES LTD.', 'approval_number': 'EASA.145.0360', 'country': 'SRI LANKA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHANGHAI TECHNOLOGIES AEROSPACE COMPANY LIMITED (STARCO)', 'approval_number': 'EASA.145.0361', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AAR COMPONENT SERVICES (THAILAND) LTD.', 'approval_number': 'EASA.145.0363', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH CUSTOMER SERVICES Inc. t/a COLLINS AEROSPACE', 'approval_number': 'EASA.145.0370', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EXECUJET MRO SERVICES MIDDLE EAST L.L.C. DWC-BRANCH', 'approval_number': 'EASA.145.0378', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH ASIA-PACIFIC Ltd.', 'approval_number': 'EASA.145.0383', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BEIJING OU TUO TECHNOLOGY Co., Ltd.', 'approval_number': 'EASA.145.0389', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN AIRCRAFT ENGINE SERVICES AMERICAS S.A. DE C.V.', 'approval_number': 'EASA.145.0390', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FALCON AVIATION SERVICES L.L.C.', 'approval_number': 'EASA.145.0400', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAIKOO (XIAMEN) LANDING GEAR SERVICES CO. LTD.', 'approval_number': 'EASA.145.0406', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MRO TEKNIK SERVIS SAN. VE TIC. A.S.', 'approval_number': 'EASA.145.0412', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULF HELICOPTERS COMPANY', 'approval_number': 'EASA.145.0419', 'country': 'QATAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMETEK REYNOSA SERVICE CENTER', 'approval_number': 'EASA.145.0420', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT EQUIPMENT OVERHAULS & SALES', 'approval_number': 'EASA.145.0428', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMETEK SINGAPORE PTE LTD', 'approval_number': 'EASA.145.0431', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HAVACILIK TEKNIK ANONIM SIRKETI', 'approval_number': 'EASA.145.0433', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WUHAN HANGDA AERO SCIENCE & TECHNOLOGY DEVELOPMENT CO., LTD.', 'approval_number': 'EASA.145.0434', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIATION COMPONENT SERVICES PTY LTD', 'approval_number': 'EASA.145.0438', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ETIHAD AIRWAYS P.J.S.C. PUBLIC JOINT STOCK COMPANY', 'approval_number': 'EASA.145.0442', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRIME AVIATION JSC JOINT STOCK COMPANY', 'approval_number': 'EASA.145.0450', 'country': 'KAZAKHSTAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRIMA HAVACILIK HIZMETLERI SANAYI VE TICARET A.S.', 'approval_number': 'EASA.145.0454', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR WORKS INDIA ENGINEERING PVT. Ltd.', 'approval_number': 'EASA.145.0464', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MDS AVIATION, SARL', 'approval_number': 'EASA.145.0471', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DUNLOP AIRCRAFT TYRES  (JINJIANG) COMPANY LIMITED', 'approval_number': 'EASA.145.0473', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PANASONIC AVIONICS SERVICES SINGAPORE PTE Ltd (PACSS)', 'approval_number': 'EASA.145.0475', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PANASONIC AVIONICS CORPORATION', 'approval_number': 'EASA.145.0480', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ETHIOPIAN AIRLINES GROUP', 'approval_number': 'EASA.145.0482', 'country': 'ETHIOPIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAIKOO ENGINE SERVICES (XIAMEN) CO.', 'approval_number': 'EASA.145.0483', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MAX MRO SERVICES PVT. LIMITED', 'approval_number': 'EASA.145.0485', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROSTRUCTURES MIDDLE EAST SERVICES, FZCO', 'approval_number': 'EASA.145.0488', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GRUPO AERONAUTICO DE MANTENIMIENTO', 'approval_number': 'EASA.145.0491', 'country': 'CUBA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOEING SHANGHAI AVIATION SERVICES CO., LTD.', 'approval_number': 'EASA.145.0497', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HORIZON AEROSPACE (INDIA) PRIVATE LIMITED', 'approval_number': 'EASA.145.0500', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GROUND 2 AIR LTD.', 'approval_number': 'EASA.145.0501', 'country': 'MAURITIUS', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHANGHAI PRATT & WHITNEY AIRCRAFT ENGINE MAINTENANCE CO., Ltd.', 'approval_number': 'EASA.145.0506', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AVIATION SYSTEMS AUSTRALIA Pty Ltd.', 'approval_number': 'EASA.145.0507', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MEGGITT AEROSPACE ASIA PACIFIC PTE. LTD.', 'approval_number': 'EASA.145.0509', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': '"SILK WAY WEST AIRLINES" LLC', 'approval_number': 'EASA.145.0510', 'country': 'AZERBAIJAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRATT & WHITNEY THY TEKNIK UCAK MOTORU BAKIM MERKEZI LTD. STI', 'approval_number': 'EASA.145.0512', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMSG AVIATION PTY LTD', 'approval_number': 'EASA.145.0516', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRIDGESTONE AIRCRAFT TIRE COMPANY (CHINA), LTD.', 'approval_number': 'EASA.145.0522', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SIA ENGINEERING (PHILIPPINES), CORPORATION', 'approval_number': 'EASA.145.0526', 'country': 'PHILIPPINES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GENEL HAVACILIK A.S.', 'approval_number': 'EASA.145.0527', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TOTAL HAVACILIK IC VE DIS TICARET LTD. STI.', 'approval_number': 'EASA.145.0530', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ASG HELICOPTER SERVICES LIMITED LIABILITY COMPANY', 'approval_number': 'EASA.145.0531', 'country': 'AZERBAIJAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL AEROSPACE AVIONICS MALAYSIA SDN. BHD.', 'approval_number': 'EASA.145.0535', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': '"AIRLINE" COMLUX-KZ" L.L.P.', 'approval_number': 'EASA.145.0536', 'country': 'KAZAKHSTAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HAECO COMPOSITE STRUCTURES (JINJIANG) CO., LTD.', 'approval_number': 'EASA.145.0537', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL AVIONICS (SHANGHAI) CO., LTD.', 'approval_number': 'EASA.145.0539', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ST ENGINEERING AEROSPACE TECHNOLOGIES', 'approval_number': 'EASA.145.0540', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'COCHIN INTERNATIONAL AVIATION SERVICES LTD.', 'approval_number': 'EASA.145.0545', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ISRAEL AEROSPACE INDUSTRIES, Ltd. (IAI)', 'approval_number': 'EASA.145.0552', 'country': 'ISRAEL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GUNES EKSPRES HAVACILIK ANONIM SIRKETI', 'approval_number': 'EASA.145.0553', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BEIJING ANDAWELL SCIENCE & TECHNOLOGY CO., LTD.', 'approval_number': 'EASA.145.0555', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JAMCO CORPORATION', 'approval_number': 'EASA.145.0560', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GMR AIR CARGO AND AEROSPACE ENGINEERING LIMITED', 'approval_number': 'EASA.145.0565', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BE AERO HAVACILIK A.S.', 'approval_number': 'EASA.145.0572', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HUTCHINSON INDUSTRIAL RUBBER PRODUCTS (SUZHOU) CO, Ltd. AEROSERVICES', 'approval_number': 'EASA.145.0577', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH AEROSTRUCTURES SERVICE (CHINA) CO, LTD.', 'approval_number': 'EASA.145.0579', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NATIONAL AVIATION GROUND SUPPORT', 'approval_number': 'EASA.145.0583', 'country': 'SAUDI ARABIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRINCE AVIATION D.O.O.', 'approval_number': 'EASA.145.0584', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH THY TEKNIK SERVIS MERKEZI Ltd. SIRKETI TURKISH NACELLE CENTER', 'approval_number': 'EASA.145.0585', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHAANXI SINTEK AVIATION TECHNOLOGIES Co., Ltd.', 'approval_number': 'EASA.145.0587', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SEPANG AIRCRAFT ENGINEERING SDN. BHD.', 'approval_number': 'EASA.145.0588', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EXECUJET MRO SERVICES MALAYSIA SDN. BHD.', 'approval_number': 'EASA.145.0589', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AVIATION SYSTEMS NORTH AMERICA QSTP‐B', 'approval_number': 'EASA.145.0597', 'country': 'QATAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NABTESCO CORPORATION', 'approval_number': 'EASA.145.0601', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIROD AEROSPACE TECHNOLOGY SDN. BHD', 'approval_number': 'EASA.145.0620', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE ON WING SUPPORT KOREA Inc.', 'approval_number': 'EASA.145.0622', 'country': 'SOUTH KOREA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR EXPRESS ALGERIA', 'approval_number': 'EASA.145.0623', 'country': 'ALGERIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'RSE STATE AIR COMPANY BERKUT', 'approval_number': 'EASA.145.0626', 'country': 'KAZAKHSTAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SALUS AVIATION AW LIMITED', 'approval_number': 'EASA.145.0628', 'country': 'NEW ZEALAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VECTOR AEROSPACE AUSTRALIA PTY LTD', 'approval_number': 'EASA.145.0635', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMAC AEROSPACE TURKEY HAVAARACI BAKIM ONARIM VE MODIFIKASYON HIZMETLERI ANONIM SIRKETI', 'approval_number': 'EASA.145.0636', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOMBARDIER AEROSPACE SERVICES SINGAPORE PTE. LTD.', 'approval_number': 'EASA.145.0642', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JAL ENGINEERING CO., LTD.', 'approval_number': 'EASA.145.0645', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SICHUAN HAITE HIGH-TECH CO., Ltd.', 'approval_number': 'EASA.145.0655', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AI ENGINEERING SERVICES LIMITED', 'approval_number': 'EASA.145.0661', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LIEBHERR (CHINA) CO.LTD.', 'approval_number': 'EASA.145.0663', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRATT & WHITNEY COMPONENT SOLUTIONS PTE. LTD.', 'approval_number': 'EASA.145.0664', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EASTERN AIRLINES TECHNIC CO.,LTD', 'approval_number': 'EASA.145.0665', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHANDONG XIANGYU AVIATION TECHNOLOGY SERVICE CO., LTD.', 'approval_number': 'EASA.145.0672', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WUHU SHUANGYI AERO-TECH CO. LTD.', 'approval_number': 'EASA.145.0676', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROSPACE ENGINEERING SERVICES JOINT STOCK COMPANY (AESC JSC)', 'approval_number': 'EASA.145.0677', 'country': 'VIETNAM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHANGHAI TAIKOO AIRCRAFT ENGINEERING SERVICES CO., LTD.', 'approval_number': 'EASA.145.0678', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'INTERIORS AEROSERVICES PTY. LTD.', 'approval_number': 'EASA.145.0679', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'INTERIORS AEROSERVICES PTE LTD.', 'approval_number': 'EASA.145.0684', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAE AEROSPACE PTY. LTD.', 'approval_number': 'EASA.145.0691', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NANJING WANGHANG AIRCRAFT COMPONENT MAINTENANCE ENGINEERING COMPANY Ltd.', 'approval_number': 'EASA.145.0692', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': "XI'AN KANGBEI ELECTRO-MECHANICAL TECHNOLOGY INC.", 'approval_number': 'EASA.145.0698', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AVIATION SYSTEMS NORTH AMERICA LLC', 'approval_number': 'EASA.145.0699', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL TAECO AEROSPACE (XIAMEN) CO., Ltd.', 'approval_number': 'EASA.145.0702', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE ON WING SUPPORT (SHANGHAI) CO, LTD.', 'approval_number': 'EASA.145.0705', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRECISION AVIATION GROUP AUSTRALIA', 'approval_number': 'EASA.145.0709', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GENERAL AVIATION SERVICE GAS-AVIATION LTD.', 'approval_number': 'EASA.145.0713', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERO INTERIORS PVT LTD', 'approval_number': 'EASA.145.0714', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROSPACE TURBINE SERVICES AND SOLUTIONS L.L.C.', 'approval_number': 'EASA.145.0717', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR FRANCE KLM COMPONENTS SERVICES (SHANGHAI) CO., LTD.', 'approval_number': 'EASA.145.0721', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ELBIT SYSTEMS - ELECTRO-OPTICS-ELOP, LTD', 'approval_number': 'EASA.145.0723', 'country': 'ISRAEL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VECTOR AEROSPACE ASIA PTE LTD', 'approval_number': 'EASA.145.0726', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'QSA AERONAUTICAL ENGINEERING SERVICES S.A.R.L.AU', 'approval_number': 'EASA.145.0731', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HRD AERO SYSTEMS SDN. BHD.', 'approval_number': 'EASA.145.0732', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAAB GRINTEK DEFENSE (PTY) LTD', 'approval_number': 'EASA.145.0733', 'country': 'SOUTH AFRICA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PROFESSIONAL FOR AIRCRAFT MAINTENANCE LLC', 'approval_number': 'EASA.145.0734', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TOPCAST AVIATION SERVICES LIMITED', 'approval_number': 'EASA.145.0737', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BEIJING CRONDA AVIATION TECHNOLOGY CORP. LTD.', 'approval_number': 'EASA.145.0738', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN AEROSYSTEMS SERVICES MIDDLE EAST DWC L.L.C.', 'approval_number': 'EASA.145.0739', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ABW HONG KONG LTD.', 'approval_number': 'EASA.145.0745', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EASTERN AIRLINES TECHNIC CO., LTD.', 'approval_number': 'EASA.145.0748', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GANSU BRANCH OF EASTERN AIRLINES TECHNIC CO.,LTD', 'approval_number': 'EASA.145.0750', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRBUS HELICOPTERS JAPAN CO., LTD.', 'approval_number': 'EASA.145.0751', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SPP NAGASAKI ENGINEERING CO. LTD.', 'approval_number': 'EASA.145.0753', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EASTERN AIRLINES TECHNIC CO., LTD. YUNNAN BRANCH', 'approval_number': 'EASA.145.0755', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ATLANTIC AIR INDUSTRIES MAROC', 'approval_number': 'EASA.145.0758', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROTORPOWER HOLDINGS PTY LTD', 'approval_number': 'EASA.145.0761', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROTECH AVIATION PTY LTD', 'approval_number': 'EASA.145.0762', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SERVICIO DE MANTENIMIENTO DEL PERU SOCIEDAD ANONIMA CERRADA', 'approval_number': 'EASA.145.0764', 'country': 'PERU', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TUSAS MOTOR SANAYII A.S.', 'approval_number': 'EASA.145.0767', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROSTRUCTURES SOLUTIONS MOROCCO LLC', 'approval_number': 'EASA.145.0768', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIC QINLING AEROSPACE (XIAMEN) LTD.', 'approval_number': 'EASA.145.0769', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EMAIR HAVACILIK VE TICARET ANONIM SIRKETI', 'approval_number': 'EASA.145.0772', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VIETNAM AIRLINES ENGINEERING COMPANY LTD', 'approval_number': 'EASA.145.0775', 'country': 'VIETNAM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TEXEL AIR W.L.L', 'approval_number': 'EASA.145.0776', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SINGAPORE COMPONENT SOLUTIONS PTE.', 'approval_number': 'EASA.145.0777', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KAAN HAVACILIK SANAYI VE TICARET A.S.', 'approval_number': 'EASA.145.0778', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MAVI GOK HAVACILIK ANONIM SIRKETI (MGA)', 'approval_number': 'EASA.145.0782', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HAECO COMPONENT OVERHAUL (XIAMEN) LTD', 'approval_number': 'EASA.145.0784', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHANGHAI HANGXIN AERO-MECHANICS CO., LTD', 'approval_number': 'EASA.145.0785', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TIANJIN HAITE AIRCRAFT ENGINEERING Co., Ltd.', 'approval_number': 'EASA.145.0788', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EXECUJET HAITE AVIATION SERVICES CHINA Co. Ltd.', 'approval_number': 'EASA.145.0794', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MYANMAR NATIONAL AIRLINES COMPANY LIMITED', 'approval_number': 'EASA.145.0801', 'country': 'MYANMAR/BURMA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GRAND CHINA AVIATION MAINTENANCE CO., LTD', 'approval_number': 'EASA.145.0809', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHINA SOUTHERN AIRLINES COMPANY LIMITED SHENYANG MAINTENANCE BASE', 'approval_number': 'EASA.145.0810', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TP AEROSPACE TECHNICS PTY LTD', 'approval_number': 'EASA.145.0811', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHENGDU FALCON AIRCRAFT ENGINEERING SERVICES CO., LTD', 'approval_number': 'EASA.145.0813', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ST ENGINEERING AEROSPACE (GUANGZHOU) AVIATION SERVICES CO., LTD', 'approval_number': 'EASA.145.0815', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HAVEUS AEROTECH INDIA LIMITED', 'approval_number': 'EASA.145.0831', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GLOBAL TURBINE ASIA SDN. BHD.', 'approval_number': 'EASA.145.0835', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LEONARDO MALAYSIA SDN. BHD.', 'approval_number': 'EASA.145.0838', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRIDGESTONE AIRCRAFT TIRE MANUFACTURING (THAILAND) Co. Ltd.', 'approval_number': 'EASA.145.0839', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROGULF SERVICES COMPANY LLC', 'approval_number': 'EASA.145.0842', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TURBINEAERO REPAIR LTD', 'approval_number': 'EASA.145.0844', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIA TECHNIQUE ASIA SDN. BHD.', 'approval_number': 'EASA.145.0851', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SICHUAN AIRCRAFT MAINTENANCE ENGINEERING CO., LTD.', 'approval_number': 'EASA.145.0857', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MOOG AIRCRAFT SERVICES ASIA PTE. LTD.', 'approval_number': 'EASA.145.0864', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EATON SAMC (SHANGHAI) AIRCRAFT CONVEYANCE SYSTEM MANUFACTURING CO., LTD.', 'approval_number': 'EASA.145.0866', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE EVERGREEN ENGINE SERVICES CORPORATION', 'approval_number': 'EASA.145.0868', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR ASIA COMPANY LIMITED.', 'approval_number': 'EASA.145.0871', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOMBARDIER TIANJIN AVIATION SERVICES COMPANY Ltd.', 'approval_number': 'EASA.145.0878', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PNG AIR LIMITED', 'approval_number': 'EASA.145.0879', 'country': 'PAPUA NEW GUINEA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MINDTREE AEROSPACE REPAIRING AND MAINTENANCE AIRCRAFT LLC', 'approval_number': 'EASA.145.0880', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRBUS AFRICA AND MIDDLE EAST FZE', 'approval_number': 'EASA.145.0881', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SETSCO SERVICES PTE LTD', 'approval_number': 'EASA.145.0885', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAIWAN AIRCRAFT MAINTENANCE AND ENGINEERING CO., LTD.', 'approval_number': 'EASA.145.0892', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MRO JAPAN CO., LTD.', 'approval_number': 'EASA.145.0896', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'UTE TECHNICS HAVACILIK SANAYI TICARET LIMITED SIRKETI', 'approval_number': 'EASA.145.0897', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHINA SOUTHERN TECHNIC XINJIANG BRANCH', 'approval_number': 'EASA.145.0904', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'REVIMA ASIA PACIFIC LTD.', 'approval_number': 'EASA.145.0905', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ACP METAL FINISHING PTE LTD', 'approval_number': 'EASA.145.0906', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DNATA', 'approval_number': 'EASA.145.0908', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'COWAY ENGINEERING & MARKETING PTE LTD', 'approval_number': 'EASA.145.0910', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CO PRODUCTION DE TIJUANA S.A. DE C.V.', 'approval_number': 'EASA.145.0911', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GKN ENGINE SYSTEMS COMPONENT REPAIR SDN. BHD.', 'approval_number': 'EASA.145.0913', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AAL GROUP LTD', 'approval_number': 'EASA.145.0919', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN ELECTRONICS & DEFENSE AVIONICS MEXICO S.A. DE C.V', 'approval_number': 'EASA.145.0920', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'B/E AEROSPACE B.V.', 'approval_number': 'EASA.145.0926', 'country': 'PHILIPPINES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TOTAL EXPERTISE FOR TRADING & INDUSTRIALS CO LTD ABUDHABI LLC', 'approval_number': 'EASA.145.0928', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOSA-THAYAAN AIRCRAFT SERVICE CO LTD.', 'approval_number': 'EASA.145.0931', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'XIAMEN AIRLINES', 'approval_number': 'EASA.145.0933', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THALES INTERNATIONAL MIDDLE EAST BRANCHES SAL', 'approval_number': 'EASA.145.0934', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': "DUBAI AVIATON CORPORATION ''FLYDUBAI''", 'approval_number': 'EASA.145.0936', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SPS AIRCRAFT SERVICES L.L.C.', 'approval_number': 'EASA.145.0938', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': "XI'AN CEA SAFRAN LANDING SYSTEMS SERVICES Co., Ltd.", 'approval_number': 'EASA.145.0942', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MC2 UCAK KOMPOZIT BAKIM ONARIM MERKEZI TICARET LIMITED SIRKETI', 'approval_number': 'EASA.145.0943', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SCHAEFFLER AEROSPACE BEARINGS (TAICANG) CO. LTD.', 'approval_number': 'EASA.145.0944', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LEONARDO AUSTRALIA PTY LTD', 'approval_number': 'EASA.145.0946', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOMBARDIER AEROSPACE (DUBAI) DWC-LLC', 'approval_number': 'EASA.145.0947', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL AEROSPACE DE MEXICO S. DE R.L. DE C.V.', 'approval_number': 'EASA.145.0949', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': "LIMA AVIONIC'S SYSTEMS S.A.C.", 'approval_number': 'EASA.145.0954', 'country': 'PERU', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': '2AS TECHNICS', 'approval_number': 'EASA.145.0956', 'country': 'SENEGAL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL AEROSPACE DE MEXICO S. DE R.L. DE C.V.', 'approval_number': 'EASA.145.0958', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SOUTHERN AIRPORTS AIRCRAFT MAINTENANCE SERVICES Co. Ltd.', 'approval_number': 'EASA.145.0961', 'country': 'VIETNAM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERO-TECHNICS FZCO', 'approval_number': 'EASA.145.0962', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ASIA DIGITAL ENGINEERING SDN. BHD.', 'approval_number': 'EASA.145.0967', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHANGHAI Z&H AERO TECHNOLOGY CO., LTD.', 'approval_number': 'EASA.145.0969', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ASIA PACIFIC AIRCRAFT COMPONENT SERVICES SDN. BHD.', 'approval_number': 'EASA.145.0972', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DRAYTON AEROSPACE (XIAMEN) LANDING SYSTEMS LTD.', 'approval_number': 'EASA.145.0973', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MAC AVIATION ENGINEERING LTD', 'approval_number': 'EASA.145.0978', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ECUBE MAINTENANCE LIMITED', 'approval_number': 'EASA.145.0981', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIATION & ELECTRONICS SUPPORT PTE. LTD.', 'approval_number': 'EASA.145.0982', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'R.I.S.E AEROSPACE PTE LTD', 'approval_number': 'EASA.145.0984', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SPIRIT EVERGREEN AFTERMARKET SOLUTIONS CO., LTD.', 'approval_number': 'EASA.145.0986', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AUSTRALIAN AERO PROPELLER MAINTENANCE', 'approval_number': 'EASA.145.0988', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WILLIS AVIATION SERVICES LIMITED', 'approval_number': 'EASA.145.0990', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LATAM AIRLINES GROUP S.A.', 'approval_number': 'EASA.145.0991', 'country': 'CHILE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WEST ATLANTIC UK LIMITED', 'approval_number': 'EASA.145.0992', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HAECO GLOBAL ENGINE SUPPORT LTD', 'approval_number': 'EASA.145.0995', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MACH TECHNIK AIRCRAFTS MAINTENANCE', 'approval_number': 'EASA.145.0998', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROENLACES NACIONALES S.A. DE C.V.', 'approval_number': 'EASA.145.0999', 'country': 'MEXICO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KAWASAKI HEAVY INDUSTRIES, LTD.', 'approval_number': 'EASA.145.1000', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FARAH CONTAINERS AND TROLLEYS  MAINTENANCE', 'approval_number': 'EASA.145.1001', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH AEROSPACE SERVICES PRIVATE LIMITED', 'approval_number': 'EASA.145.1002', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HANWHA AEROSPACE CO. LTD', 'approval_number': 'EASA.145.1005', 'country': 'SOUTH KOREA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMAN AVIATION & AEROSPACE SOLUTIONS PRIVATE LIMITED', 'approval_number': 'EASA.145.1006', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STAR AVIATION SPA', 'approval_number': 'EASA.145.1007', 'country': 'ALGERIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ATS TECHNIC AIRCRAFTS REPAIR FZCO', 'approval_number': 'EASA.145.1008', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STEEL DESIGN (FZE)', 'approval_number': 'EASA.145.1009', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRBUS (CHENGDU) LIFECYCLE SERVICES LTD.', 'approval_number': 'EASA.145.1013', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'IPECO SINGAPORE PTE. LTD.', 'approval_number': 'EASA.145.1017', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ONTIC ENGINEERING AND MANUFACTURING ASIA-PACIFIC PTE. LTD.', 'approval_number': 'EASA.145.1019', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT ACCESSORIES AND COMPONENTS COMPANY LTD.', 'approval_number': 'EASA.145.1020', 'country': 'SAUDI ARABIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULF AIRCRAFT & ENGINEERING SERVICES (GAES) (FZE) t/a GAES', 'approval_number': 'EASA.145.1022', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KENYA AIRWAYS PLC', 'approval_number': 'EASA.145.1024', 'country': 'KENYA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ISLAND AVIATION SERVICES LIMITED D/B/A MALDIVIAN', 'approval_number': 'EASA.145.1032', 'country': 'MALDIVES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERO DESIGN DWC-LLC AERO DESIGN BY LIBERTY AVIATION', 'approval_number': 'EASA.145.1033', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THALES AEROSPACE BEIJING CO., LTD.', 'approval_number': 'EASA.145.1035', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SETNIX LTD', 'approval_number': 'EASA.145.1043', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GLOBAL COMPONENT ASIA SDN. BHD', 'approval_number': 'EASA.145.1045', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN ELECTRICAL & POWER SINGAPORE PTE. LTD.', 'approval_number': 'EASA.145.1046', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VIETNAM SINGAPORE TECHNOLOGIES ENGINEERING AEROSPACE  CO. LTD T/A VSTEA', 'approval_number': 'EASA.145.1048', 'country': 'VIETNAM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BEIJING AERO ENGINE SERVICES CO. LTD', 'approval_number': 'EASA.145.1050', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DHL AVIATION EEMEA B.S.C.CLOSED', 'approval_number': 'EASA.145.1059', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEM LIMITED', 'approval_number': 'EASA.145.3002', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CHELTON LIMITED', 'approval_number': 'EASA.145.3003', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HELIWORK (SERVICES) LIMITED', 'approval_number': 'EASA.145.3004', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRITISH AIRWAYS PLC', 'approval_number': 'EASA.145.3005', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'INFLITE ENGINEERING SERVICES LIMITED', 'approval_number': 'EASA.145.3006', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRISTOW HELICOPTERS LIMITED', 'approval_number': 'EASA.145.3010', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AIRCRAFT ENGINE SERVICES LIMITED', 'approval_number': 'EASA.145.3011', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MEGGITT (UK) LIMITED', 'approval_number': 'EASA.145.3012', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KEARSLEY AIRWAYS LIMITED', 'approval_number': 'EASA.145.3013', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AVIATION SYSTEMS LIMITED', 'approval_number': 'EASA.145.3014', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HARRODS AVIATION LIMITED', 'approval_number': 'EASA.145.3015', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SLOANE HELICOPTERS LIMITED', 'approval_number': 'EASA.145.3016', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'UNILODE AVIATION SOLUTIONS UK LIMITED', 'approval_number': 'EASA.145.3017', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TURNER AVIATION LIMITED', 'approval_number': 'EASA.145.3020', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KLM UK ENGINEERING LIMITED', 'approval_number': 'EASA.145.3021', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRITISH AIRWAYS ENGINEERING WALES LIMITED', 'approval_number': 'EASA.145.3024', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MEL AVIATION LIMITED', 'approval_number': 'EASA.145.3027', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMSAFE BRIDPORT LIMITED', 'approval_number': 'EASA.145.3028', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE CALEDONIAN LIMITED', 'approval_number': 'EASA.145.3029', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PENNY & GILES AEROSPACE LIMITED', 'approval_number': 'EASA.145.3032', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ULTRA PCS LIMITED', 'approval_number': 'EASA.145.3033', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SMITHS AEROSPACE LIMITED', 'approval_number': 'EASA.145.3034', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH AEROSPACE UK LIMITED', 'approval_number': 'EASA.145.3035', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SURVIVAL ONE LTD', 'approval_number': 'EASA.145.3037', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MOOG CONTROLS LIMITED', 'approval_number': 'EASA.145.3038', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROLUX LIMITED', 'approval_number': 'EASA.145.3039', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CSE BOURNEMOUTH LIMITED', 'approval_number': 'EASA.145.3041', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PERCIVAL AVIATION LIMITED', 'approval_number': 'EASA.145.3042', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GKN AEROSPACE SERVICES LIMITED', 'approval_number': 'EASA.145.3043', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HANLEY SMITH LIMITED', 'approval_number': 'EASA.145.3044', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FLITETEC LIMITED', 'approval_number': 'EASA.145.3046', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SHORT BROTHERS PLC', 'approval_number': 'EASA.145.3048', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AMETEK AIRTECHNOLOGY GROUP LIMITED', 'approval_number': 'EASA.145.3050', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SKYWHEELS LTD', 'approval_number': 'EASA.145.3051', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MORGAN-WARD (NON-DESTRUCTIVE TESTING) LIMITED', 'approval_number': 'EASA.145.3055', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GARMIN (EUROPE) LIMITED', 'approval_number': 'EASA.145.3059', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EURAVIA ENGINEERING & SUPPLY CO. LIMITED', 'approval_number': 'EASA.145.3061', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SATAIR UK LIMITED', 'approval_number': 'EASA.145.3063', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'OAKENHURST AIRCRAFT SERVICES LIMITED', 'approval_number': 'EASA.145.3064', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NORDAM EUROPE LIMITED', 'approval_number': 'EASA.145.3066', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DUNLOP AIRCRAFT TYRES LIMITED', 'approval_number': 'EASA.145.3068', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROHR AERO SERVICES LIMITED', 'approval_number': 'EASA.145.3069', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MULTIFLIGHT LTD.', 'approval_number': 'EASA.145.3074', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MUIRHEAD AEROSPACE LIMITED', 'approval_number': 'EASA.145.3077', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL UK LIMITED', 'approval_number': 'EASA.145.3078', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WOODWARD INTERNATIONAL, INC.', 'approval_number': 'EASA.145.3079', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AD AEROSPACE LIMITED', 'approval_number': 'EASA.145.3080', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRATT & WHITNEY CANADA (UK) LTD', 'approval_number': 'EASA.145.3082', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN LANDING SYSTEMS SERVICES UK LTD', 'approval_number': 'EASA.145.3083', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROLLS-ROYCE PLC', 'approval_number': 'EASA.145.3085', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR ATLANTA AVIASERVICES LIMITED', 'approval_number': 'EASA.145.3086', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HS MARSTON AEROSPACE LIMITED', 'approval_number': 'EASA.145.3087', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BABCOCK MISSION CRITICAL SERVICES ONSHORE LIMITED', 'approval_number': 'EASA.145.3089', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'IPECO HOLDINGS LIMITED', 'approval_number': 'EASA.145.3091', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DRUCK LIMITED', 'approval_number': 'EASA.145.3092', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TRT LIMITED', 'approval_number': 'EASA.145.3093', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EATON LIMITED', 'approval_number': 'EASA.145.3100', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROTABLE REPAIRS LIMITED', 'approval_number': 'EASA.145.3101', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERORESPONSE LTD', 'approval_number': 'EASA.145.3103', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ACLAS TECHNICS LIMITED', 'approval_number': 'EASA.145.3104', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN SEATS GB LIMITED', 'approval_number': 'EASA.145.3106', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ALTITUDE GLOBAL LIMITED', 'approval_number': 'EASA.145.3107', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIA TECHNIQUE Ltd.', 'approval_number': 'EASA.145.3109', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT COMPONENT SERVICES LIMITED', 'approval_number': 'EASA.145.3110', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DHL AIR (UK) LIMITED', 'approval_number': 'EASA.145.3111', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH CONTROL SYSTEMS', 'approval_number': 'EASA.145.3112', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GOODRICH ACTUATION SYSTEMS LTD.', 'approval_number': 'EASA.145.3113', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EXPRESS AVIATION SUPPORT INTERNATIONAL LIMITED', 'approval_number': 'EASA.145.3115', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL UK LIMITED', 'approval_number': 'EASA.145.3116', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL UK LIMITED', 'approval_number': 'EASA.145.3118', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULFSTREAM AEROSPACE, LTD', 'approval_number': 'EASA.145.3119', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BAE SYSTEMS (OPERATIONS) LIMITED', 'approval_number': 'EASA.145.3120', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRESTWICK AIRCRAFT MAINTENANCE LTD.', 'approval_number': 'EASA.145.3122', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MEGGITT AEROSPACE LIMITED', 'approval_number': 'EASA.145.3123', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'REMOTE VISUAL INSPECTIONS LIMITED', 'approval_number': 'EASA.145.3125', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'B/E AEROSPACE (UK) Ltd.', 'approval_number': 'EASA.145.3126', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROPEOPLE LIMITED', 'approval_number': 'EASA.145.3127', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'IMT AVIATION SCOTLAND LIMITED', 'approval_number': 'EASA.145.3128', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STANSTED AEROSPACE LIMITED', 'approval_number': 'EASA.145.3129', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'IMT AVIATION LIMITED', 'approval_number': 'EASA.145.3132', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STORM AVIATION LIMITED', 'approval_number': 'EASA.145.3134', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN AEROSYSTEMS SERVICES UK LIMITED', 'approval_number': 'EASA.145.3136', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AVIATION SYSTEMS LIMITED', 'approval_number': 'EASA.145.3137', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NORTH WALES MILITARY AVIATION SERVICES LIMITED', 'approval_number': 'EASA.145.3138', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'RDDS AVIONICS LIMITED', 'approval_number': 'EASA.145.3141', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MEGGITT AEROSPACE LIMITED', 'approval_number': 'EASA.145.3143', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'H.R. SMITH (TECHNICAL DEVELOPMENTS) LIMITED', 'approval_number': 'EASA.145.3144', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRIMEFLIGHT ENGINEERING LTD', 'approval_number': 'EASA.145.3146', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOURNEMOUTH AVIATION SERVICES LTD.', 'approval_number': 'EASA.145.3149', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NICHOLSON MCLAREN AVIATION LIMITED', 'approval_number': 'EASA.145.3151', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BCT AVIATION MAINTENANCE LIMITED', 'approval_number': 'EASA.145.3153', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROTOR BLADES LIMITED', 'approval_number': 'EASA.145.3154', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PARADIGM PRECISION BURNLEY LTD', 'approval_number': 'EASA.145.3156', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'F.P.T INDUSTRIES LIMITED', 'approval_number': 'EASA.145.3157', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GKN AEROSPACE SERVICES LIMITED', 'approval_number': 'EASA.145.3160', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SKYSMART MRO LTD', 'approval_number': 'EASA.145.3161', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VECTOR AEROSPACE INTERNATIONAL LTD', 'approval_number': 'EASA.145.3162', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRINKLEY PROPELLER SERVICES LIMITED', 'approval_number': 'EASA.145.3163', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': '25 REPAIR CENTRE LIMITED', 'approval_number': 'EASA.145.3164', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WORLD AERO LIMITED', 'approval_number': 'EASA.145.3165', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NORVIC AERO ENGINES LIMITED', 'approval_number': 'EASA.145.3169', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PROPTECH AERO LTD', 'approval_number': 'EASA.145.3170', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EUROPEAN SKYBUS LIMITED', 'approval_number': 'EASA.145.3171', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GRIFFITHS AERO LIMITED', 'approval_number': 'EASA.145.3172', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOSTONAIR LIMITED', 'approval_number': 'EASA.145.3174', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ONTIC ENGINEERING & MANUFACTURING UK LIMITED', 'approval_number': 'EASA.145.3177', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVMAN ENGINEERING LIMITED', 'approval_number': 'EASA.145.3178', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MOOG WOLVERHAMPTON LIMITED', 'approval_number': 'EASA.145.3179', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CABINAIR SERVICES LIMITED', 'approval_number': 'EASA.145.3180', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GJD AEROTECH LIMITED', 'approval_number': 'EASA.145.3181', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STS AVIATION SERVICES UK LIMITED', 'approval_number': 'EASA.145.3184', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PALL EUROPE LIMITED', 'approval_number': 'EASA.145.3185', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ADAMS AVIATION SUPPLY COMPANY LIMITED', 'approval_number': 'EASA.145.3186', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STS ENGINE SERVICES LTD', 'approval_number': 'EASA.145.3187', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERO TECHNICS (MANCHESTER) LIMITED', 'approval_number': 'EASA.145.3189', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'APMS AVIATION  LIMITED', 'approval_number': 'EASA.145.3191', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GE AIRCRAFT ENGINE SERVICES LIMITED', 'approval_number': 'EASA.145.3193', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SOUTHERN AIRFRAME SERVICES LTD', 'approval_number': 'EASA.145.3195', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GAS TURBINE SOLUTIONS LIMITED', 'approval_number': 'EASA.145.3196', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THOMPSON AERO SEATING LIMITED', 'approval_number': 'EASA.145.3197', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CFS AEROPRODUCTS LTD', 'approval_number': 'EASA.145.3198', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CAERDAV LIMITED', 'approval_number': 'EASA.145.3199', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROCO GROUP INTERNATIONAL LIMITED', 'approval_number': 'EASA.145.3200', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOS AEROSPACE LTD', 'approval_number': 'EASA.145.3202', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRX JET SUPPORT LIMITED', 'approval_number': 'EASA.145.3203', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFRAN ELECTRICAL & POWER UK LIMITED', 'approval_number': 'EASA.145.3204', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MISSION SYSTEMS WIMBORNE LIMITED', 'approval_number': 'EASA.145.3206', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SKYWARDS AVIATION CONSULTANTS LTD', 'approval_number': 'EASA.145.3210', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EATON LIMITED', 'approval_number': 'EASA.145.3212', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THALES UK LIMITED', 'approval_number': 'EASA.145.3213', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ACS AVIATION INDUSTRIES LIMITED', 'approval_number': 'EASA.145.3216', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DEA AVIATION LIMITED', 'approval_number': 'EASA.145.3217', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GAMA AVIATION (ENGINEERING) LIMITED', 'approval_number': 'EASA.145.3220', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GC AVIATION MAINTENANCE LIMITED', 'approval_number': 'EASA.145.3222', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KAL AVIATION SERVICES LIMITED', 'approval_number': 'EASA.145.3223', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': '2 EXCEL ENGINEERING LIMITED', 'approval_number': 'EASA.145.3227', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ATC HOLDINGS LIMITED', 'approval_number': 'EASA.145.3228', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VOLARE AVIATION LIMITED', 'approval_number': 'EASA.145.3229', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'THURSTON AVIATION ENGINEERING LIMITED', 'approval_number': 'EASA.145.3232', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOMBARDIER SERVICES (UK) LIMITED', 'approval_number': 'EASA.145.3234', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CRS TECHNICS LIMITED', 'approval_number': 'EASA.145.3235', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WILLIS ENGINE REPAIR CENTRE (UK) LTD', 'approval_number': 'EASA.145.3236', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'APPH LIMITED', 'approval_number': 'EASA.145.3237', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AJW TECHNIQUE EUROPE LIMITED', 'approval_number': 'EASA.145.3238', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LEONARDO UK LTD', 'approval_number': 'EASA.145.3240', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AEROTRON AVOTEC LIMITED', 'approval_number': 'EASA.145.3242', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ORIENS MAINTENANCE SERVICES LIMITED', 'approval_number': 'EASA.145.3243', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PREMIER JET SUPPORT LTD.', 'approval_number': 'EASA.145.3244', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONEYWELL UK LIMITED', 'approval_number': 'EASA.145.3246', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LUFTAVIA LTD', 'approval_number': 'EASA.145.3247', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'INTERIORS NEWCO LIMITED T/A AIRLINE SERVICES INTERIORS', 'approval_number': 'EASA.145.3248', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'REPAERO LIMITED', 'approval_number': 'EASA.145.3249', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EASYJET UK LIMITED', 'approval_number': 'EASA.145.3251', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AERFIN LIMITED', 'approval_number': 'EASA.145.3252', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JMI - JET MAINTENANCE INTERNATIONAL', 'approval_number': 'EASA.145.3254', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'APPLUS UK LTD', 'approval_number': 'EASA.145.3255', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ARGO MOBILE REPAIR TEAM (UK) LTD.', 'approval_number': 'EASA.145.3256', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT SERVICING GUERNSEY LTD', 'approval_number': 'EASA.145.3261', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'INFLITE MRO SERVICES LIMITED', 'approval_number': 'EASA.145.3262', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SOUTHDOWN AERO SERVICES LIMITED', 'approval_number': 'EASA.145.3263', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PB ENGINEERING SOLUTIONS LIMITED', 'approval_number': 'EASA.145.3264', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FRM AVIATION SERVICES Ltd.', 'approval_number': 'EASA.145.3265', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TELEDYNE UK LIMITED', 'approval_number': 'EASA.145.3266', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCAMO ENGINES LTD', 'approval_number': 'EASA.145.3267', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'REHEAT AERO Ltd.', 'approval_number': 'EASA.145.3268', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EXETER AEROSPACE LIMITED', 'approval_number': 'EASA.145.3270', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRBUS HELICOPTERS UK LIMITED', 'approval_number': 'EASA.UK.145.00124', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STARLING AEROSPACE LIMITED', 'approval_number': 'EASA.UK.145.01249', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FLIGHT DATA SYSTEMS LTD', 'approval_number': 'EASA.UK.145.01332', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FLIGHTSAFETY INTERNATIONAL Inc.', 'approval_number': 'EASA.147.0001', 'country': 'UNITED STATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BAS AIRCRAFT ENGINEERING TRAINING CENTRE', 'approval_number': 'EASA.147.0002', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DELTA AIR LINES, INC. TECHNICAL OPERATIONS TRAINING', 'approval_number': 'EASA.147.0003', 'country': 'UNITED STATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT MAINTENANCE AND ENGINEERING CORPORATION, BEIJING (AMECO)', 'approval_number': 'EASA.147.0004', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CAE INC.', 'approval_number': 'EASA.147.0005', 'country': 'CANADA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIATION AUSTRALIA PTY LTD', 'approval_number': 'EASA.147.0012', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EMIRATES', 'approval_number': 'EASA.147.0014', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EGYPTAIR HOLDING COMPANY', 'approval_number': 'EASA.147.0019', 'country': 'EGYPT', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TAIKOO (XIAMEN) AIRCRAFT ENGINEERING COMPANY LTD.', 'approval_number': 'EASA.147.0027', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HONG KONG AIRCRAFT ENGINEERING COMPANY LIMITED (HAECO)', 'approval_number': 'EASA.147.0029', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'QUEENSLAND AEROSPACE Pty. Ltd.', 'approval_number': 'EASA.147.0030', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KUWAIT AIRWAYS COMPANY', 'approval_number': 'EASA.147.0033', 'country': 'KUWAIT', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULF AVIATION ACADEMY', 'approval_number': 'EASA.147.0036', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BELL TEXTRON INC.', 'approval_number': 'EASA.147.0039', 'country': 'UNITED STATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VAZDUHOPLOVNA AKADEMIJA (AVIATION ACADEMY)', 'approval_number': 'EASA.147.0041', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SIA ENGINEERING COMPANY LIMITED', 'approval_number': 'EASA.147.0044', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SRILANKAN AIRLINES LTD.', 'approval_number': 'EASA.147.0045', 'country': 'SRI LANKA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TURK HAVA YOLLARI TEKNIK A.S.', 'approval_number': 'EASA.147.0046', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BIMAN BANGLADESH AIRLINES LIMITED', 'approval_number': 'EASA.147.0047', 'country': 'BANGLADESH', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR NEW ZEALAND LTD.', 'approval_number': 'EASA.147.0048', 'country': 'NEW ZEALAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'NEW ENDEAVOURS, Inc.', 'approval_number': 'EASA.147.0050', 'country': 'CANADA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JORDAN AIRLINES TRAINING AND SIMULATION CO. LTD. (JATS)', 'approval_number': 'EASA.147.0058', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EMBRAER S.A.', 'approval_number': 'EASA.147.0059', 'country': 'BRAZIL', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'QATAR AERONAUTICAL ACADEMY', 'approval_number': 'EASA.147.0065', 'country': 'QATAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ABU DHABI POLYTECHNIC - AL AIN CAMPUS', 'approval_number': 'EASA.147.0066', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ETHIOPIAN AIRLINES AVIATION ACADEMY', 'approval_number': 'EASA.147.0069', 'country': 'ETHIOPIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AFAQ ACADEMY FOR AVIATION TECHNOLOGY W.L.L', 'approval_number': 'EASA.147.0072', 'country': 'BAHRAIN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'QATAR AIRWAYS Q.C.S.C.', 'approval_number': 'EASA.147.0073', 'country': 'QATAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AUSTRALIAN UNIVERSITY', 'approval_number': 'EASA.147.0074', 'country': 'KUWAIT', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CATHAY PACIFIC AIRWAYS, LTD.', 'approval_number': 'EASA.147.0076', 'country': 'HONG KONG', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MAB ENGINEERING SERVICES SDN. BHD.', 'approval_number': 'EASA.147.0078', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULF HELICOPTERS COMPANY', 'approval_number': 'EASA.147.0079', 'country': 'QATAR', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOEING US TRAINING AND FLIGHT SERVICES L.L.C.', 'approval_number': 'EASA.147.0080', 'country': 'UNITED STATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FLIGHTPATH INTERNATIONAL TECHNICAL LTD.', 'approval_number': 'EASA.147.0081', 'country': 'CANADA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'UNIVERSITI TEKNIKAL MARA Sdn. Bhd.', 'approval_number': 'EASA.147.0083', 'country': 'MALAYSIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ST ENGINEERING AEROSPACE LTD.', 'approval_number': 'EASA.147.0088', 'country': 'SINGAPORE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MILITARY TECHNOLOGICAL COLLEGE (MTC)', 'approval_number': 'EASA.147.0096', 'country': 'OMAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PT. GARUDA MAINTENANCE FACILITY AERO ASIA TBK.', 'approval_number': 'EASA.147.0100', 'country': 'INDONESIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRINCE AVIATION D.O.O.', 'approval_number': 'EASA.147.0104', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FUJAIRAH AVIATION ACADEMY', 'approval_number': 'EASA.147.0107', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SIA ENGINEERING (PHILIPPINES), CORPORATION', 'approval_number': 'EASA.147.0108', 'country': 'PHILIPPINES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ZAGDU SINGH CHARITABLE TRUST', 'approval_number': 'EASA.147.0113', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR ASTANA JOINT STOCK COMPANY', 'approval_number': 'EASA.147.0117', 'country': 'KAZAKHSTAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ETIHAD AIRWAYS ENGINEERING L.L.C. T/A ETIHAD ENGINEERING TECHNICAL TRAININ', 'approval_number': 'EASA.147.0118', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SOUTH AFRICAN AIRWAYS TECHNICAL SOC LTD.', 'approval_number': 'EASA.147.0120', 'country': 'SOUTH AFRICA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CIRRUS DESIGN CORPORATION', 'approval_number': 'EASA.147.0122', 'country': 'UNITED STATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EASTERN AIRLINES TECHNIC CO., LTD.', 'approval_number': 'EASA.147.0123', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GUANGZHOU AIRCRAFT MAINTENANCE ENGINEERING Co. Ltd.', 'approval_number': 'EASA.147.0125', 'country': 'CHINA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'J.R.N. INSTITUTE PRIVATE LIMITED', 'approval_number': 'EASA.147.0127', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ALDIS HAVACILIK LIMITED SIRKETI', 'approval_number': 'EASA.147.0128', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ANVA (FZE)', 'approval_number': 'EASA.147.0129', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AI ENGINEERING SERVICES LIMITED', 'approval_number': 'EASA.147.0131', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'DEHAVILLAND AVIATION TRAINING LTD', 'approval_number': 'EASA.147.0133', 'country': 'CANADA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'UNITED TECHNOLOGIES CORPORATION INDIA PRIVATE LIMITED', 'approval_number': 'EASA.147.0134', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JAL ENGINEERING CO., LTD.', 'approval_number': 'EASA.147.0135', 'country': 'JAPAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ROYAL JORDANIAN AIR ACADEMY', 'approval_number': 'EASA.147.0139', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIATION TRAINING EXPERTS D.O.O.', 'approval_number': 'EASA.147.0140', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BAE SYSTEMS ARABIAN INDUSTRIES LIMITED', 'approval_number': 'EASA.147.0141', 'country': 'SAUDI ARABIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MOROCCO AVIATION PRIVATE ACADEMY', 'approval_number': 'EASA.147.0142', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PEGASUS HAVA TASIMACILIGI ANONIM SIRKETI', 'approval_number': 'EASA.147.0146', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TOTAL AVIATION TRAINING LTD', 'approval_number': 'EASA.147.0147', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'Q S A AERONAUTICAL ENGINEERING SERVICES', 'approval_number': 'EASA.147.0148', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MRO TEKNIK SERVIS SAN. VE TIC. A.S.', 'approval_number': 'EASA.147.0149', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'INTELEK TRAINING AND CONSULTATION ACADEMY', 'approval_number': 'EASA.147.0151', 'country': 'SOUTH AFRICA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EMIRATES', 'approval_number': 'EASA.147.0152', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MIDEAST AVIATION ACADEMY OF AERONAUTICS, MAINTENANCE AND ADMINISTRATION', 'approval_number': 'EASA.147.0153', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'POENTE TECHNICAL ACADEMY LLC', 'approval_number': 'EASA.147.0154', 'country': 'SERBIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LUFTAVIA TECHNICAL TRAINING', 'approval_number': 'EASA.147.0155', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BE AERO HAVACILIK A.S.', 'approval_number': 'EASA.147.0160', 'country': 'TÜRKIYE', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'HELITSA PTY LTD', 'approval_number': 'EASA.147.0161', 'country': 'AUSTRALIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIR INDIA LTD', 'approval_number': 'EASA.147.0162', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRITISH AIRWAYS PLC', 'approval_number': 'EASA.147.0173', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'KLM UK ENGINEERING LIMITED', 'approval_number': 'EASA.147.0176', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'FR AVIATION LIMITED', 'approval_number': 'EASA.147.0178', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GLENNAIR TRAINING CENTRE LIMITED', 'approval_number': 'EASA.147.0179', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRBUS HELICOPTERS UK LIMITED', 'approval_number': 'EASA.147.0180', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'LRTT LIMITED', 'approval_number': 'EASA.147.0181', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'STORM AVIATION LIMITED', 'approval_number': 'EASA.147.0182', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ADVANCED AIRCRAFT TRAINING LIMITED', 'approval_number': 'EASA.147.0183', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MORNINGTON SANFORD AVIATION (TRAINING) Ltd.', 'approval_number': 'EASA.147.0184', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'ANGEL TRAINING SYSTEMS LTD', 'approval_number': 'EASA.147.0185', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CIVIL AVIATION TECHNICAL TRAINING SOLUTIONS LIMITED', 'approval_number': 'EASA.147.0186', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BOSTONAIR TECHNICAL TRAINING LTD', 'approval_number': 'EASA.147.0187', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'PRESTWICK AERO LIMITED', 'approval_number': 'EASA.147.0188', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCRAFT ENGINEERING CONSULTANCY', 'approval_number': 'EASA.147.0190', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRLINE TRAINING ACADEMY UK LTD', 'approval_number': 'EASA.147.0191', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'A2BAERO LTD', 'approval_number': 'EASA.147.0192', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'UNIVERSITY OF SOUTH WALES', 'approval_number': 'EASA.147.0194', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VOLARE AVIATION LIMITED', 'approval_number': 'EASA.147.0195', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'P & P AVIATION TRAINING LTD', 'approval_number': 'EASA.147.0196', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AVIATION CONSULT LTD', 'approval_number': 'EASA.147.0197', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MACAV LTD', 'approval_number': 'EASA.147.0199', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'BRITISH SCHOOL OF AVIATION LTD', 'approval_number': 'EASA.147.0202', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CITY OF BRISTOL COLLEGE', 'approval_number': 'EASA.147.0203', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'JORDAN AIRCRAFT MAINTENANCE Ltd.', 'approval_number': 'EASA.147.0204', 'country': 'JORDAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GMR AIR CARGO AND AEROSPACE ENGINEERING LIMITED', 'approval_number': 'EASA.147.0207', 'country': 'INDIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CIVIL AVIATION TRAINING CENTER (CATC)', 'approval_number': 'EASA.147.0208', 'country': 'THAILAND', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CSE BOURNEMOUTH LIMITED', 'approval_number': 'EASA.147.0209', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GLOBAL AVIATION CENTER 3A', 'approval_number': 'EASA.147.0212', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'TUNISAIR TECHNICS', 'approval_number': 'EASA.147.0213', 'country': 'TUNISIA', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GAMA AVIATION (ENGINEERING) LIMITED', 'approval_number': 'EASA.147.0216', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'SAFESKY SOLUTION SSS', 'approval_number': 'EASA.147.0220', 'country': 'MOROCCO', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'GULF AIRCRAFT & ENGINEERING SERVICES (GAES) (FZE) t/a GAES', 'approval_number': 'EASA.147.0221', 'country': 'UNITED ARAB EMIRATES', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EVERGREEN AVIATION TECHNOLOGIES CORPORATION EVERGREEN AVIATION TECHNOLOGIES CORP. MAINTENANCE TRAINING CENTER', 'approval_number': 'EASA.147.0223', 'country': 'TAIWAN', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'VIETNAM AIRLINES ENGINEERING COMPANY LTD.', 'approval_number': 'EASA.147.0224', 'country': 'VIETNAM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'MIDDLE EAST AIRLINES - AIR LIBAN S.A.L.', 'approval_number': 'EASA.CAMO.0002', 'country': 'LEBANON', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'AIRCAMO AVIATION Ltd.', 'approval_number': 'EASA.CAMO.0009', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'WILLIS MITSUI & CO ASSET MANAGEMENT LIMI', 'approval_number': 'EASA.CAMO.0012', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'EUROWINGS TECHNIK GMBH', 'approval_number': 'EASA.CAMO.0017', 'country': 'GERMANY', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}, {'name': 'CAMERON BALLOONS LIMITED', 'approval_number': 'EASA.CAO.0001', 'country': 'UNITED KINGDOM', 'address': '', 'source': 'easa_foreign', 'source_url': 'https://easa.europa.eu', 'source_date': '2026-03-27'}]
    for w in orgs:
        try:
            cur.execute("SELECT id FROM maintenance_org WHERE approval_number = %s", (w["approval_number"],))
            if cur.fetchone():
                skipped += 1
                continue
            cur.execute("INSERT INTO maintenance_org (name, approval_number, address, country, source, source_url, source_date) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (w["name"], w["approval_number"], w["address"], w["country"], w["source"], w["source_url"], w["source_date"]))
            imported += 1
        except Exception as e:
            conn.rollback()
    conn.commit()
    conn.close()
    return f"Done! Importeret: {imported}, Sprunget over: {skipped}"

@app.route('/sitemap.xml')
def sitemap():
    conn_s = get_pg_conn()
    cur_s = conn_s.cursor()
    cur_s.execute("SELECT COUNT(*) FROM aircraft")
    total = cur_s.fetchone()[0]
    conn_s.close()
    pages = (total // 10000) + 1
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '    <sitemap><loc>https://panpanparts.com/sitemap-pages.xml</loc></sitemap>\n'
    for i in range(1, pages + 1):
        xml += f'    <sitemap><loc>https://panpanparts.com/sitemap-aircraft-{i}.xml</loc></sitemap>\n'
    xml += '</sitemapindex>'
    return xml, 200, {'Content-Type': 'application/xml'}

@app.route('/sitemap-pages.xml')
def sitemap_pages():
    conn_s = get_pg_conn()
    cur_s = conn_s.cursor()
    cur_s.execute("SELECT id, manufacturer, model, tail FROM aircraft_listing WHERE status='active' ORDER BY id")
    listings = cur_s.fetchall()
    conn_s.close()
    urls = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://panpanparts.com/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>
    <url><loc>https://panpanparts.com/parts</loc><changefreq>daily</changefreq><priority>0.9</priority></url>
    <url><loc>https://panpanparts.com/aircraft-for-sale</loc><changefreq>daily</changefreq><priority>0.9</priority></url>
    <url><loc>https://panpanparts.com/workshops</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>
"""
    for l in listings:
        urls += f"    <url><loc>https://panpanparts.com/aircraft-listing/{l[0]}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n"
    urls += "</urlset>"
    return urls, 200, {'Content-Type': 'application/xml'}

@app.route('/sitemap-aircraft-<int:page>.xml')
def sitemap_aircraft(page):
    limit = 10000
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

def run_daily_notifications():
    try:
        from notifications import check_and_notify
        check_and_notify(app, db, User, ClaimedAircraft, PilotCertificate)
    except Exception as e:
        print(f"Notification fejl: {e}")

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
scheduler.add_job(run_daily_notifications, 'cron', hour=2, minute=30)
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
        date_fields = ['license_valid_until', 'medical_valid_until']
        other_fields = ['license_number', 'license_type', 'medical_class', 'total_flight_hours', 'ratings']
        for field in other_fields:
            val = request.form.get(field)
            if val is not None:
                setattr(current_user, field, val)
        for field in date_fields:
            val = request.form.get(field)
            if val is not None:
                setattr(current_user, field, normalize_date(val))
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
                        {{ current_user.medical_valid_until[:10] if current_user.medical_valid_until else "" }}
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
                        {{ current_user.license_valid_until[:10] if current_user.license_valid_until else "" }}
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
                    <input type="text" name="license_valid_until" type="date" value="{{ current_user.license_valid_until or '' }}">
                    <label>Medical class</label>
                    <select name="medical_class">
                        <option value="">Select...</option>
                        <option value="Class 1" {% if current_user.medical_class == 'Class 1' %}selected{% endif %}>Class 1 — Commercial</option>
                        <option value="Class 2" {% if current_user.medical_class == 'Class 2' %}selected{% endif %}>Class 2 — Private</option>
                        <option value="LAPL" {% if current_user.medical_class == 'LAPL' %}selected{% endif %}>LAPL Medical</option>
                    </select>
                    <label>Medical valid until</label>
                    <input type="text" name="medical_valid_until" type="date" value="{{ current_user.medical_valid_until or '' }}">
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

@app.route('/my-logbook/all')
@login_required
def my_logbook_all():
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
    return render_template_string(LOGBOOK_ALL_HTML, entries=entries, current_user=current_user, total_time=total_str, total_flights=len(entries))

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

    # Mine fly — unikke tail# med antal flyvninger og seneste dato
    import json as _json
    from sqlalchemy import func
    from collections import defaultdict
    aircraft_stats = defaultdict(lambda: {'flights': 0, 'last_date': None, 'type': None})
    for e in entries:
        if e.registration:
            reg = e.registration.strip()
            aircraft_stats[reg]['flights'] += 1
            if e.flight_date:
                if not aircraft_stats[reg]['last_date'] or e.flight_date > aircraft_stats[reg]['last_date']:
                    aircraft_stats[reg]['last_date'] = e.flight_date
            if e.aircraft_type and not aircraft_stats[reg]['type']:
                aircraft_stats[reg]['type'] = e.aircraft_type

    # Preferred aircraft fra user
    preferred = []
    if current_user.preferred_aircraft:
        try:
            preferred = _json.loads(current_user.preferred_aircraft)
        except:
            preferred = []

    # Tilføj fly fra logbog til preferred hvis ikke allerede der
    for reg in aircraft_stats:
        if reg not in preferred:
            preferred.append(reg)
    
    # Gem opdateret preferred_aircraft
    if preferred:
        current_user.preferred_aircraft = _json.dumps(preferred)
        db.session.commit()

    # Træningsbarometer — seneste 6 måneder
    from datetime import datetime, timedelta
    import re as _re
    six_months_ago = datetime.now() - timedelta(days=182)
    recent_minutes = 0
    recent_landings = 0
    for e in entries:
        if e.flight_date:
            try:
                # Parse DD/MM/YYYY
                parts = e.flight_date.split('/')
                if len(parts) == 3:
                    edate = datetime(int(parts[2]), int(parts[1]), int(parts[0]))
                    if edate >= six_months_ago:
                        if e.total_time and e.total_time not in ['—', '-', '']:
                            tp = e.total_time.replace(':', ' ').split()
                            if len(tp) == 2:
                                recent_minutes += int(tp[0]) * 60 + int(tp[1])
                        if e.landings_day:
                            recent_landings += int(e.landings_day)
            except:
                pass
    recent_hours = recent_minutes / 60

    # Grøn/gul/rød baseret på timer OG landinger
    if recent_hours >= 6 and recent_landings >= 12:
        baro_status = 'green'
        baro_text = 'You are in good flying practice'
        baro_emoji = '🟢'
    elif recent_hours >= 3 and recent_landings >= 6:
        baro_status = 'yellow'
        baro_text = 'Your training is not optimal — be extra careful'
        baro_emoji = '🟡'
    else:
        baro_status = 'red'
        baro_text = 'You are rusty — contact an instructor before flying'
        baro_emoji = '🔴'

    recent_hours_str = f"{int(recent_hours)}:{int(recent_minutes % 60):02d}"

    return render_template_string(LOGBOOK_HTML, entries=entries, current_user=current_user, total_time=total_str, total_flights=len(entries), aircraft_stats=dict(aircraft_stats), preferred=preferred, baro_status=baro_status, baro_text=baro_text, baro_emoji=baro_emoji, recent_hours_str=recent_hours_str, recent_landings=recent_landings)

@app.route('/logbook/add-aircraft', methods=['POST'])
@login_required
def logbook_add_aircraft():
    import json as _json
    data = request.get_json()
    reg = data.get('registration', '').strip().upper()
    if not reg:
        return _json.dumps({'ok': False})
    preferred = []
    if current_user.preferred_aircraft:
        try:
            preferred = _json.loads(current_user.preferred_aircraft)
        except:
            preferred = []
    if reg not in preferred:
        preferred.append(reg)
        current_user.preferred_aircraft = _json.dumps(preferred)
        db.session.commit()
    return _json.dumps({'ok': True})

@app.route('/logbook/update-landings', methods=['POST'])
@login_required
def logbook_update_landings():
    import json as _json
    data = request.get_json()
    entry_id = data.get('entry_id')
    landings = data.get('landings_day', 0)
    entry = LogbookEntry.query.filter_by(id=entry_id, user_id=current_user.id).first()
    if not entry:
        return _json.dumps({'ok': False})
    entry.landings_day = landings
    db.session.commit()
    return _json.dumps({'ok': True})

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
    
    # Preferred aircraft
    import json as _json
    preferred = []
    if current_user.preferred_aircraft:
        try:
            preferred = _json.loads(current_user.preferred_aircraft)
        except:
            preferred = []
    if preferred:
        known_regs = list(set(known_regs + preferred))

    context_hint = ""
    if known_regs:
        context_hint = f"\n\nThis pilot flies: {', '.join(known_regs)}. Use these as PRIMARY reference for registration."

    # Licens-baserede regler
    license_rules = ""
    lt = current_user.license_type or 'PPL'
    if lt == 'SPL':
        license_rules = """
PILOT LICENSE: Student Pilot (SPL)
- sep_vfr: ALWAYS fill with total_time
- dual: ALWAYS fill with total_time (always flies with instructor)
- pic_time: ALWAYS null
- night_time: ALWAYS null
- sep_ifr: ALWAYS null
- landings_night: ALWAYS null"""
    elif lt == 'PPL':
        license_rules = """
PILOT LICENSE: PPL
- sep_vfr: fill if VFR flight
- pic_time: fill if flying as PIC
- dual: fill if flying with instructor
- night_time: only if actual night flight
- sep_ifr: null unless rated"""

    content_parts.append({"type": "text", "text": f"""These are pages from a pilot logbook. Extract all flight entries carefully.

IMPORTANT:
- Dates are ALWAYS in DD/MM/YY format (European). Day first, then month, then 2-digit year.
- Examples: 02/10/25 = 02/10/2025, 20/01/26 = 20/01/2026, 04/03/26 = 04/03/2026.
- NEVER interpret dates as MM/DD/YY — this is a European logbook.
- Aircraft registrations: OY-XXX (Denmark), LN-XXX (Norway), N12345 (USA). 
- Danish registrations are always OY- followed by 3 letters. Read each letter carefully.
- Times are H:MM format. A space between digits means colon e.g. "1 55" = 1:55.
- Block time MAX 5 hours — if over 5 hours set off_block, on_block and total_time to null.
- Only extract rows with actual flight data — skip empty rows.
- CRITICAL: Preserve the EXACT order of rows as they appear on the page. Do NOT sort or reorder entries.
- Read rows strictly from top to bottom. Row 1 in the logbook must be row 1 in your output.
- landings_day: READ CAREFULLY from right page — this is important for training currency.
- At the bottom of the page there are totals: "Total This Page", "Total Previous Pages", "Total".
- Read these totals and include them in a "page_totals" field in your response.
- Calculate your own total of all flight times and compare with "Total This Page".
- If they differ, add a "validation_warning" field explaining the discrepancy.
{license_rules}{context_hint}

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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
    <title>My Logbook - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script>
        function adjustLandings(entryId, delta) {
            var span = document.getElementById("ldg-" + entryId);
            var current = parseInt(span.textContent) || 0;
            var newVal = Math.max(0, current + delta);
            span.textContent = newVal;
            fetch("/logbook/update-landings", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({entry_id: entryId, landings_day: newVal})
            })
            .then(r => r.json())
            .then(result => { if (!result.ok) span.textContent = current; });
        }
    </script>
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
        .table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
        th { text-align: left; padding: 8px 6px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; white-space: nowrap; }
        td { padding: 8px 6px; border-bottom: 1px solid #1a1a2e; white-space: nowrap; }
        tr:hover td { background: #1a1a2e; cursor: pointer; }
        .total-row td { color: #ff6b35; font-weight: 600; border-top: 2px solid #2a2a3e; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }
        .delete-btn:hover { color: #ff6b35; }
        .desktop-col { display: table-cell; }
        @media (max-width: 768px) {
            .desktop-col { display: none; }
            .container { padding: 0 10px; }
            .header { padding: 16px 20px; }
            table { font-size: 12px; }
        }
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

        <!-- Træningsbarometer -->
        <div class="card" style="border-left: 4px solid {% if baro_status == 'green' %}#4caf50{% elif baro_status == 'yellow' %}#ffc107{% else %}#f44336{% endif %}">
            <h3>Flight Currency — last 6 months</h3>
            <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px">
                <div style="font-size:48px">{{ baro_emoji }}</div>
                <div>
                    <div style="font-size:20px;font-weight:700;color:{% if baro_status == 'green' %}#4caf50{% elif baro_status == 'yellow' %}#ffc107{% else %}#f44336{% endif %}">
                        {% if baro_status == 'green' %}GREEN{% elif baro_status == 'yellow' %}YELLOW{% else %}RED{% endif %}
                    </div>
                    <div style="font-size:14px;color:#aaa;margin-top:4px">{{ baro_text }}</div>
                </div>
            </div>
            <div style="display:flex;gap:24px">
                <div style="background:#0d0d1a;border-radius:8px;padding:12px 20px;text-align:center">
                    <div style="font-size:24px;font-weight:700;font-family:monospace;color:#ff6b35">{{ recent_hours_str }}</div>
                    <div style="font-size:11px;color:#666;margin-top:2px">Hours (need {% if recent_hours_str < '3:00' %}3:00 for yellow, {% endif %}6:00 for green)</div>
                </div>
                <div style="background:#0d0d1a;border-radius:8px;padding:12px 20px;text-align:center">
                    <div style="font-size:24px;font-weight:700;font-family:monospace;color:#ff6b35">{{ recent_landings }}</div>
                    <div style="font-size:11px;color:#666;margin-top:2px">Landings (need 6 for yellow, 12 for green)</div>
                </div>
            </div>
        </div>

        <!-- Træningsbarometer -->


        <!-- Mine fly -->
        <div class="card">
            <h3>My flight history</h3>
            {% if aircraft_stats %}
            <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px">
                {% for reg, stats in aircraft_stats.items() %}
                <div style="background:#0d0d1a;border:1px solid #2a2a3e;border-radius:8px;padding:12px 16px;min-width:140px">
                    <div style="font-size:18px;font-weight:700;font-family:monospace;color:#ff6b35">{{ reg }}</div>
                    <div style="font-size:12px;color:#666;margin-top:4px">{{ stats.flights }} flight{{ 's' if stats.flights != 1 else '' }}</div>
                    {% if stats.last_date %}<div style="font-size:11px;color:#444">Last: {{ stats.last_date }}</div>{% endif %}
                </div>
                {% endfor %}
            </div>
            {% endif %}
            <div style="display:flex;gap:10px;align-items:center">
                <input type="text" id="new-reg-input" placeholder="Add aircraft (e.g. OY-BLZ)" 
                    style="background:#0d0d1a;border:1px solid #333;border-radius:8px;padding:10px 12px;color:white;font-size:14px;width:200px">
                <button onclick="addAircraft()" 
                    style="background:#ff6b35;color:white;border:none;padding:10px 16px;border-radius:8px;font-size:14px;cursor:pointer;font-weight:600">
                    + Add
                </button>
            </div>
        </div>


        <!-- Logbog entries -->
        <div class="card">
            <h3>Recent flights</h3>
            {% if entries %}
            <div class="table-scroll">
            <table>
                <tr>
                    <th>Date</th>
                    <th class="desktop-col">From</th>
                    <th class="desktop-col">To</th>
                    <th class="desktop-col">Off</th>
                    <th class="desktop-col">On</th>
                    <th class="desktop-col">Type</th>
                    <th>Reg</th>
                    <th>Total</th>
                    <th class="desktop-col">SEP VFR</th>
                    <th>Dual</th>
                    <th>Ldg</th>
                    <th></th>
                </tr>
                {% for e in entries[:5] %}
                <tr onclick="editEntry({{ e.id }}, '{{ e.flight_date or '' | replace("'", "") }}', '{{ e.dep_place or '' | replace("'", "") }}', '{{ e.arr_place or '' | replace("'", "") }}', '{{ e.aircraft_type or '' | replace("'", "") }}', '{{ e.registration or '' | replace("'", "") }}', '{{ e.total_time or '' | replace("'", "") }}', '{{ e.dual or '' | replace("'", "") }}', '{{ e.landings_day or 0 }}')">
                    <td>{{ e.flight_date or '—' }}</td>
                    <td class="desktop-col">{{ e.dep_place or '—' }}</td>
                    <td class="desktop-col">{{ e.arr_place or '—' }}</td>
                    <td class="desktop-col">{{ e.off_block or '—' }}</td>
                    <td class="desktop-col">{{ e.on_block or '—' }}</td>
                    <td class="desktop-col">{{ e.aircraft_type or '—' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or '—' }}</td>
                    <td>{{ e.total_time or '—' }}</td>
                    <td class="desktop-col">{{ e.sep_vfr or '—' }}</td>
                    <td>{{ e.dual or '—' }}</td>
                    <td onclick="event.stopPropagation()" style="white-space:nowrap">
                        <button onclick="event.stopPropagation();adjustLandings({{ e.id }}, -1)" style="background:#1a1a2e;border:1px solid #333;color:#aaa;width:22px;height:22px;border-radius:4px;cursor:pointer;font-size:14px;line-height:1">-</button>
                        <span id="ldg-{{ e.id }}" style="margin:0 6px;font-family:monospace">{{ e.landings_day or 0 }}</span>
                        <button onclick="event.stopPropagation();adjustLandings({{ e.id }}, 1)" style="background:#1a1a2e;border:1px solid #333;color:#aaa;width:22px;height:22px;border-radius:4px;cursor:pointer;font-size:14px;line-height:1">+</button>
                    </td>
                    <td class="desktop-col">{{ e.landings_night or '—' }}</td>
                    <td class="desktop-col" style="color:#666;font-size:12px">{{ e.remarks or '' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="event.stopPropagation();return confirm('Delete?')">✕</a></td>
                </tr>
                {% endfor %}
            </table>
            </div>
            {% if entries|length > 5 %}
            <div style="text-align:center;margin-top:16px">
                <a href="/my-logbook/all" style="color:#ff6b35;font-size:14px;text-decoration:none;font-weight:600">View all {{ entries|length }} flights →</a>
            </div>
            {% endif %}
            {% else %}
            <p style="color:#444;font-size:14px;padding:16px 0">No flights yet — scan your logbook pages above!</p>
            {% endif %}
        </div>
    </div>

    <!-- Edit modal -->
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
            <a href="/logbook-review" style="display:block;text-align:center;margin-top:10px;color:#ff6b35;font-size:14px">Or use step-by-step review →</a>
            <div class="status" id="status"></div>
        </div>

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

        function adjustLandings(entryId, delta) {
            var span = document.getElementById("ldg-" + entryId);
            var current = parseInt(span.textContent) || 0;
            var newVal = Math.max(0, current + delta);
            span.textContent = newVal;
            fetch("/logbook/update-landings", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({entry_id: entryId, landings_day: newVal})
            })
            .then(r => r.json())
            .then(result => {
                if (!result.ok) span.textContent = current; // Rul tilbage ved fejl
            });
        }

        function addAircraft() {
            var reg = document.getElementById("new-reg-input").value.trim().toUpperCase();
            if (!reg) return;
            fetch("/logbook/add-aircraft", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({registration: reg})
            })
            .then(r => r.json())
            .then(result => {
                if (result.ok) { location.reload(); }
                else { alert("Could not add aircraft"); }
            });
        }

        document.addEventListener("DOMContentLoaded", function() {
            var inp = document.getElementById("new-reg-input");
            if (inp) inp.addEventListener("keypress", function(e) {
                if (e.key === "Enter") addAircraft();
            });
        });

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

@app.route('/logbook-review', methods=['GET', 'POST'])
@login_required
def logbook_review():
    from flask import session
    import anthropic as ac
    import json

    if request.method == 'POST':
        data = request.get_json()
        
        if data.get('action') == 'scan':
            # Scan siden og gem alle rækker i session
            image_data = data.get('image')
            
            # Hent tidligere godkendte entries som kontekst
            prev_entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.id.desc()).limit(5).all()
            known_regs = list(set([e.registration for e in prev_entries if e.registration]))
            
            context = ""
            if known_regs:
                context = f"\nThis pilot flies: {', '.join(known_regs)}. Use as reference."
            
            if prev_entries:
                last = prev_entries[0]
                context += f"\nLast database entry: {last.flight_date}, {last.registration}, {last.total_time}"

            # Tilføj godkendte linjer fra denne session som kontekst
            approved = session.get('review_approved', [])
            if approved:
                context += f"\nAlready approved in this session ({len(approved)} flights):"
                for a in approved[-3:]:  # Kun de 3 seneste
                    context += f"\n  - {a.get('flight_date','?')} {a.get('registration','?')} {a.get('dep_place','?')}->{a.get('arr_place','?')} total={a.get('total_time','?')}"
                last_approved = approved[-1]
                context += f"\nNext date must be >= {last_approved.get('flight_date','?')}. Registration is likely {last_approved.get('registration','?')} unless changed."

            # Licens-baserede regler for AI
            license_rules = ""
            lt = current_user.license_type or 'PPL'
            if lt == 'SPL':
                license_rules = """
PILOT LICENSE: Student Pilot (SPL)
- sep_vfr: ALWAYS fill with total_time (student flies VFR only)
- dual: ALWAYS fill with total_time (student always flies with instructor)
- pic_time: ALWAYS null (student cannot log PIC)
- night_time: ALWAYS null (student cannot fly night)
- sep_ifr: ALWAYS null (student cannot fly IFR)
- landings_night: ALWAYS null"""
            elif lt == 'PPL':
                license_rules = """
PILOT LICENSE: PPL (Private Pilot)
- sep_vfr: fill if VFR flight
- pic_time: fill if flying as PIC
- dual: fill if flying with instructor
- night_time: only if actual night flight
- sep_ifr: ALWAYS null unless specifically rated"""
            elif lt in ('CPL', 'ATPL'):
                license_rules = """
PILOT LICENSE: CPL/ATPL
- Fill all relevant columns based on actual flight conditions"""

            client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=3000,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data}},
                        {"type": "text", "text": f"""This is a page from a pilot logbook. Extract ALL flight rows carefully.

RULES:
- Dates are DD/MM/YY (European). 25=2025, 26=2026. NEVER MM/DD.
- Off Block and On Block are UTC times HH:MM. Total = On Block - Off Block.
- Calculate total_time yourself from off_block and on_block as validation. MAX 5 hours — if calculated time exceeds 5 hours, set off_block, on_block and total_time to null.
- Aircraft registrations: OY-XXX (Denmark). Read each letter carefully.
- Preserve EXACT row order — do NOT sort.
- Only rows with actual flight data.
{license_rules}{context}

Respond ONLY with JSON array:
[{{
  "flight_date": "DD/MM/YYYY",
  "dep_place": "ICAO",
  "arr_place": "ICAO", 
  "off_block": "HH:MM",
  "on_block": "HH:MM",
  "aircraft_type": "type",
  "registration": "OY-XXX",
  "total_time": "H:MM",
  "night_time": "H:MM or null",
  "sep_vfr": "H:MM or null",
  "sep_ifr": "H:MM or null",
  "pic_time": "H:MM or null",
  "dual": "H:MM or null",
  "landings_day": number or null,
  "landings_night": number or null,
  "remarks": "text or null"
}}]"""}
                    ]
                }]
            )
            
            text = response.content[0].text
            clean = text.replace("```json", "").replace("```", "").strip()
            flights = json.loads(clean)
            
            # Gem i session
            session['review_flights'] = flights
            session['review_index'] = 0
            session['review_approved'] = []
            
            # Find sidst godkendte dato til kronologi-tjek i frontend
            last_date = None
            if approved:
                last_date = approved[-1].get('flight_date')
            elif prev_entries:
                last_date = prev_entries[0].flight_date

            return json.dumps({'ok': True, 'total': len(flights), 'first': flights[0] if flights else None, 'last_approved_date': last_date})
        
        elif data.get('action') == 'approve':
            # Godkend nuværende linje (med eventuelle rettelser)
            flight_data = data.get('flight')
            flights = session.get('review_flights', [])
            index = session.get('review_index', 0)
            approved = session.get('review_approved', [])
            
            # Gem i database
            entry = LogbookEntry(
                user_id=current_user.id,
                flight_date=flight_data.get('flight_date'),
                dep_place=flight_data.get('dep_place'),
                arr_place=flight_data.get('arr_place'),
                off_block=flight_data.get('off_block'),
                on_block=flight_data.get('on_block'),
                aircraft_type=flight_data.get('aircraft_type'),
                registration=flight_data.get('registration'),
                total_time=flight_data.get('total_time'),
                night_time=flight_data.get('night_time'),
                sep_vfr=flight_data.get('sep_vfr'),
                sep_ifr=flight_data.get('sep_ifr'),
                pic_time=flight_data.get('pic_time'),
                dual=flight_data.get('dual'),
                landings_day=flight_data.get('landings_day'),
                landings_night=flight_data.get('landings_night'),
                remarks=flight_data.get('remarks'),
            )
            db.session.add(entry)
            db.session.commit()
            
            approved.append(flight_data)
            index += 1
            session['review_index'] = index
            session['review_approved'] = approved
            
            if index < len(flights):
                return json.dumps({'ok': True, 'done': False, 'next': flights[index], 'index': index, 'total': len(flights), 'last_approved_date': flight_data.get('flight_date')})
            else:
                session.pop('review_flights', None)
                session.pop('review_index', None)
                session.pop('review_approved', None)
                return json.dumps({'ok': True, 'done': True, 'saved': len(approved)})
    
    return render_template_string(LOGBOOK_REVIEW_HTML, current_user=current_user)


LOGBOOK_ALL_HTML = """<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
    <title>All Flights - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
        table { width: 100%; border-collapse: collapse; font-size: 12px; }
        th { text-align: left; padding: 8px 6px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; white-space: nowrap; }
        td { padding: 8px 6px; border-bottom: 1px solid #1a1a2e; white-space: nowrap; }
        tr:hover td { background: #1a1a2e; }
        .total-row td { color: #ff6b35; font-weight: 600; border-top: 2px solid #2a2a3e; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }
        .delete-btn:hover { color: #ff6b35; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <a href="/my-logbook" class="back">← My logbook</a>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px">
            <h1 style="font-size:28px">All <span style="color:#ff6b35">Flights</span></h1>
            <div style="text-align:right">
                <div style="font-size:32px;font-weight:700;color:#ff6b35;font-family:monospace">{{ total_time }}</div>
                <div style="font-size:12px;color:#666">{{ total_flights }} flights total</div>
            </div>
        </div>
        <div class="card">
            <div class="table-scroll">
            <table>
                <tr>
                    <th>Date</th>
                    <th>From</th>
                    <th>To</th>
                    <th>Off</th>
                    <th>On</th>
                    <th>Type</th>
                    <th>Reg</th>
                    <th>Total</th>
                    <th>Night</th>
                    <th>SEP VFR</th>
                    <th>SEP IFR</th>
                    <th>PIC</th>
                    <th>Dual</th>
                    <th>Ldg D</th>
                    <th>Ldg N</th>
                    <th>Remarks</th>
                    <th></th>
                </tr>
                {% for e in entries %}
                <tr>
                    <td>{{ e.flight_date or '—' }}</td>
                    <td>{{ e.dep_place or '—' }}</td>
                    <td>{{ e.arr_place or '—' }}</td>
                    <td>{{ e.off_block or '—' }}</td>
                    <td>{{ e.on_block or '—' }}</td>
                    <td>{{ e.aircraft_type or '—' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or '—' }}</td>
                    <td>{{ e.total_time or '—' }}</td>
                    <td>{{ e.night_time or '—' }}</td>
                    <td>{{ e.sep_vfr or '—' }}</td>
                    <td>{{ e.sep_ifr or '—' }}</td>
                    <td>{{ e.pic_time or '—' }}</td>
                    <td>{{ e.dual or '—' }}</td>
                    <td>{{ e.landings_day or '—' }}</td>
                    <td>{{ e.landings_night or '—' }}</td>
                    <td style="color:#666;font-size:11px">{{ e.remarks or '' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="return confirm('Delete?')">✕</a></td>
                </tr>
                {% endfor %}
                <tr class="total-row">
                    <td colspan="7">Total</td>
                    <td>{{ total_time }}</td>
                    <td colspan="9"></td>
                </tr>
            </table>
            </div>
        </div>
    </div>
</body>
</html>"""

LOGBOOK_REVIEW_HTML = """<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
    <title>Logbook Review - PanPanParts</title>
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
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .upload-box { border: 2px dashed #333; border-radius: 8px; padding: 40px; text-align: center; cursor: pointer; color: #666; font-size: 14px; }
        .upload-box:hover { border-color: #ff6b35; color: #ff6b35; }
        .upload-box img { max-width: 100%; border-radius: 8px; display: none; margin-top: 12px; }
        input[type=file] { display: none; }
        .scan-btn { background: #ff6b35; color: white; border: none; padding: 14px 28px; border-radius: 8px; font-size: 15px; cursor: pointer; font-weight: 600; width: 100%; margin-top: 12px; }
        .scan-btn:disabled { background: #444; cursor: not-allowed; }
        .progress { background: #0d0d1a; border-radius: 8px; padding: 8px; margin-bottom: 16px; }
        .progress-bar { background: #ff6b35; height: 6px; border-radius: 3px; transition: width 0.3s; }
        .progress-text { font-size: 12px; color: #666; margin-top: 6px; text-align: center; }
        .field-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px; }
        .field-row-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 10px; }
        label { font-size: 12px; color: #666; display: block; margin-bottom: 4px; }
        input[type=text], input[type=number] { width: 100%; padding: 10px 12px; border: 1px solid #333; border-radius: 8px; font-size: 14px; background: #0d0d1a; color: white; }
        input[type=text]:focus, input[type=number]:focus { border-color: #ff6b35; outline: none; }
        .warning { background: rgba(255,193,7,0.15); border: 1px solid rgba(255,193,7,0.3); border-radius: 8px; padding: 12px; margin-bottom: 12px; color: #ffc107; font-size: 13px; }
        .btn-row { display: flex; gap: 12px; margin-top: 16px; }
        .approve-btn { flex: 1; background: #2d7a3a; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 15px; cursor: pointer; font-weight: 600; }
        .approve-btn:hover { background: #3d9a4a; }
        .skip-btn { background: #1a1a2e; color: #aaa; border: 1px solid #333; padding: 14px 20px; border-radius: 8px; font-size: 14px; cursor: pointer; }
        .done-card { text-align: center; padding: 40px; }
        .done-card h2 { font-size: 28px; color: #4caf50; margin-bottom: 12px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <a href="/my-logbook" class="back">← My logbook</a>
        <h1 style="font-size:28px;margin-bottom:24px">Scan <span style="color:#ff6b35">Logbook Page</span></h1>

        <!-- Upload -->
        <div class="card" id="upload-card">
            <h3>Step 1 — Upload logbook page</h3>
            <div class="upload-box" onclick="document.getElementById('page-input').click()">
                <div id="upload-label">📷 Tap to photograph or upload logbook page</div>
                <img id="page-preview">
                <input type="file" id="page-input" accept="image/*" onchange="loadPage(this)">
            </div>
            <button class="scan-btn" id="scan-btn" onclick="startScan()" disabled>Scan with AI →</button>
        </div>

        <!-- Progress -->
        <div id="progress-card" style="display:none" class="card">
            <h3>Progress</h3>
            <div class="progress">
                <div class="progress-bar" id="progress-bar" style="width:0%"></div>
            </div>
            <div class="progress-text" id="progress-text">Scanning...</div>
        </div>

        <!-- Review -->
        <div id="review-card" style="display:none" class="card">
            <h3 id="review-title">Review flight entry</h3>
            
            <div id="time-warning" class="warning" style="display:none">
                ⚠ Calculated time from Off/On Block differs from Total Time
            </div>

            <div class="field-row">
                <div><label>Date (DD/MM/YYYY)</label><input type="text" id="f-date"></div>
                <div><label>Registration</label><input type="text" id="f-reg"></div>
            </div>
            <div class="field-row">
                <div><label>From</label><input type="text" id="f-dep"></div>
                <div><label>To</label><input type="text" id="f-arr"></div>
            </div>
            <div class="field-row">
                <div><label>Off Block (UTC)</label><input type="text" id="f-off" oninput="validateTime()"></div>
                <div><label>On Block (UTC)</label><input type="text" id="f-on" oninput="validateTime()"></div>
            </div>
            <div class="field-row-3">
                <div><label>Total time</label><input type="text" id="f-total"></div>
                <div><label>SEP VFR</label><input type="text" id="f-sepvfr"></div>
                <div><label>Dual</label><input type="text" id="f-dual"></div>
            </div>
            <div class="field-row-3">
                <div><label>PIC</label><input type="text" id="f-pic"></div>
                <div><label>Night</label><input type="text" id="f-night"></div>
                <div><label>Landings</label><input type="number" id="f-ldg"></div>
            </div>
            <div><label>Remarks</label><input type="text" id="f-remarks"></div>

            <div class="btn-row">
                <button class="approve-btn" id="approve-btn" onclick="approveFlight()">✓ Approve & next</button>
                <button class="skip-btn" onclick="skipFlight()">Skip</button>
            </div>
        </div>

        <!-- Done -->
        <div id="done-card" style="display:none" class="done-card">
            <h2>✓ All done!</h2>
            <p style="color:#aaa;margin-bottom:24px" id="done-text">Flights saved to your logbook.</p>
            <a href="/my-logbook" style="background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600">View logbook →</a>
        </div>
    </div>

    <script>
        var imageData = null;
        var currentFlight = null;
        var currentIndex = 0;
        var totalFlights = 0;
        var lastApprovedDate = null;  // Til dato-kronologi tjek

        function loadPage(input) {
            var file = input.files[0];
            if (!file) return;
            var reader = new FileReader();
            reader.onload = function(e) {
                var img = new Image();
                img.onload = function() {
                    var canvas = document.createElement("canvas");
                    var maxSize = 1800;
                    var w = img.width, h = img.height;
                    if (w > maxSize || h > maxSize) {
                        if (w > h) { h = h * maxSize / w; w = maxSize; }
                        else { w = w * maxSize / h; h = maxSize; }
                    }
                    canvas.width = w; canvas.height = h;
                    canvas.getContext("2d").drawImage(img, 0, 0, w, h);
                    var compressed = canvas.toDataURL("image/jpeg", 0.85);
                    imageData = compressed.split(",")[1];
                    document.getElementById("page-preview").src = compressed;
                    document.getElementById("page-preview").style.display = "block";
                    document.getElementById("upload-label").style.display = "none";
                    document.getElementById("scan-btn").disabled = false;
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }

        function startScan() {
            document.getElementById("scan-btn").disabled = true;
            document.getElementById("scan-btn").textContent = "Scanning...";
            document.getElementById("progress-card").style.display = "block";
            document.getElementById("progress-text").textContent = "AI is reading your logbook page...";

            fetch("/logbook-review", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({action: "scan", image: imageData})
            })
            .then(r => r.json())
            .then(result => {
                if (result.ok) {
                    totalFlights = result.total;
                    currentIndex = 0;
                    if (result.last_approved_date) lastApprovedDate = result.last_approved_date;
                    showFlight(result.first, 0, totalFlights);
                }
            });
        }

        function showFlight(flight, index, total) {
            currentFlight = flight;
            currentIndex = index;
            document.getElementById("upload-card").style.display = "none";
            document.getElementById("review-card").style.display = "block";
            document.getElementById("review-title").textContent = 
                "Flight " + (index + 1) + " of " + total + " — Review & approve";
            
            var pct = Math.round((index / total) * 100);
            document.getElementById("progress-bar").style.width = pct + "%";
            document.getElementById("progress-text").textContent = 
                (index + 1) + " of " + total + " flights";

            document.getElementById("f-date").value = flight.flight_date || "";
            document.getElementById("f-reg").value = flight.registration || "";
            document.getElementById("f-dep").value = flight.dep_place || "";
            document.getElementById("f-arr").value = flight.arr_place || "";
            document.getElementById("f-off").value = flight.off_block || "";
            document.getElementById("f-on").value = flight.on_block || "";
            document.getElementById("f-total").value = flight.total_time || "";
            document.getElementById("f-sepvfr").value = flight.sep_vfr || "";
            document.getElementById("f-dual").value = flight.dual || "";
            document.getElementById("f-pic").value = flight.pic_time || "";
            document.getElementById("f-night").value = flight.night_time || "";
            document.getElementById("f-ldg").value = flight.landings_day || "";
            document.getElementById("f-remarks").value = flight.remarks || "";
            
            validateTime();
        }

        function validateTime() {
            var off = document.getElementById("f-off").value;
            var on = document.getElementById("f-on").value;
            var warnings = [];

            if (off && on) {
                // Normaliser HHMM -> HH:MM
                if (off.length == 4 && !off.includes(":")) off = off.slice(0,2) + ":" + off.slice(2);
                if (on.length == 4 && !on.includes(":")) on = on.slice(0,2) + ":" + on.slice(2);
                document.getElementById("f-off").value = off;
                document.getElementById("f-on").value = on;

                var offParts = off.split(":");
                var onParts = on.split(":");
                if (offParts.length == 2 && onParts.length == 2) {
                    var offMin = parseInt(offParts[0]) * 60 + parseInt(offParts[1]);
                    var onMin = parseInt(onParts[0]) * 60 + parseInt(onParts[1]);
                    var diffMin = onMin - offMin;
                    if (diffMin < 0) diffMin += 24 * 60;
                    var calcH = Math.floor(diffMin / 60);
                    var calcM = diffMin % 60;
                    var calcStr = calcH + ":" + (calcM < 10 ? "0" : "") + calcM;

                    if (diffMin > 300) {
                        // Over 5 timer — ryd alle tidsfelter, piloten skal indtaste selv
                        document.getElementById("f-off").value = "";
                        document.getElementById("f-on").value = "";
                        document.getElementById("f-total").value = "";
                        warnings.push("Tider kunne ikke læses — indtast Off Block, On Block manuelt");
                    } else {
                        document.getElementById("f-total").value = calcStr;
                    }
                }
            }

            // Dato-kronologi — kan ikke godkendes hvis dato er før forrige
            var dateVal = document.getElementById("f-date").value;
            var dateBlocked = false;
            if (dateVal && lastApprovedDate) {
                var parseDMY = function(s) {
                    var p = s.split("/");
                    if (p.length == 3) return new Date(parseInt(p[2]), parseInt(p[1])-1, parseInt(p[0]));
                    return null;
                };
                var d1 = parseDMY(lastApprovedDate);
                var d2 = parseDMY(dateVal);
                if (d1 && d2 && d2 < d1) {
                    document.getElementById("f-date").value = "";
                    document.getElementById("f-date").placeholder = "Indtast dato (efter " + lastApprovedDate + ")";
                    document.getElementById("f-date").style.borderColor = "#ff4444";
                    dateBlocked = true;
                    warnings.push("Dato er ryddet — skal være efter " + lastApprovedDate);
                } else {
                    document.getElementById("f-date").style.borderColor = "";
                }
            }

            // Bloker Approve-knappen hvis dato mangler
            document.getElementById("approve-btn").disabled = dateBlocked || !document.getElementById("f-date").value;

            var warnEl = document.getElementById("time-warning");
            if (warnings.length > 0) {
                warnEl.innerHTML = warnings.join("<br>");
                warnEl.style.display = "block";
            } else {
                warnEl.style.display = "none";
            }
        }

        function getFlight() {
            return {
                flight_date: document.getElementById("f-date").value,
                registration: document.getElementById("f-reg").value,
                dep_place: document.getElementById("f-dep").value,
                arr_place: document.getElementById("f-arr").value,
                off_block: document.getElementById("f-off").value,
                on_block: document.getElementById("f-on").value,
                total_time: document.getElementById("f-total").value,
                sep_vfr: document.getElementById("f-sepvfr").value,
                dual: document.getElementById("f-dual").value,
                pic_time: document.getElementById("f-pic").value,
                night_time: document.getElementById("f-night").value,
                landings_day: parseInt(document.getElementById("f-ldg").value) || null,
                remarks: document.getElementById("f-remarks").value,
            };
        }

        function approveFlight() {
            fetch("/logbook-review", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({action: "approve", flight: getFlight()})
            })
            .then(r => r.json())
            .then(result => {
                if (result.done) {
                    document.getElementById("review-card").style.display = "none";
                    document.getElementById("progress-card").style.display = "none";
                    document.getElementById("done-card").style.display = "block";
                    document.getElementById("done-text").textContent = 
                        result.saved + " flights saved to your logbook!";
                } else {
                    if (result.last_approved_date) lastApprovedDate = result.last_approved_date;
                    showFlight(result.next, result.index, result.total);
                }
            });
        }

        function skipFlight() {
            fetch("/logbook-review", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({action: "approve", flight: {skip: true}})
            })
            .then(r => r.json())
            .then(result => {
                if (result.done) {
                    document.getElementById("review-card").style.display = "none";
                    document.getElementById("done-card").style.display = "block";
                } else {
                    showFlight(result.next, result.index, result.total);
                }
            });
        }
    </script>
</body>
</html>"""

@app.route('/api/live/<tail>')
def live_tracking(tail):
    import requests
    import json
    
    try:
        # Søg i hele verden
        r = requests.get('https://opensky-network.org/api/states/all', timeout=5)
        data = r.json()
        
        if not data.get('states'):
            return json.dumps({'airborne': False, 'reason': 'No data'})
        
        # Søg efter tail# som callsign
        search = tail.upper().replace('-', '')
        
        for s in data['states']:
            callsign = (s[1] or '').strip().upper().replace('-', '')
            if callsign == search or callsign == tail.upper().replace('-', ''):
                return json.dumps({
                    'airborne': s[7] is not None and s[7] > 0,
                    'altitude': round(s[7]) if s[7] else 0,
                    'speed': round(s[9] * 3.6) if s[9] else 0,
                    'latitude': s[6],
                    'longitude': s[5],
                    'heading': round(s[10]) if s[10] else 0,
                    'callsign': s[1].strip() if s[1] else tail,
                    'icao24': s[0]
                })
        
        return json.dumps({'airborne': False, 'reason': 'Not found in airspace'})
    
    except Exception as e:
        return json.dumps({'airborne': False, 'reason': str(e)})

@app.route('/my-aircraft/<tail>/maintenance')
@login_required
def aircraft_maintenance(tail):
    import json
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return redirect('/my-aircraft')
    entries = AircraftMaintenanceLog.query.filter_by(tail=tail).order_by(AircraftMaintenanceLog.id.asc()).all()
    r = get_aircraft(tail)
    def s(val):
        v = str(val).strip() if val else ""
        return "" if v in ["nan", "None"] else v
    manufacturer = s(r["manufacturer"]) if r else ""
    model = s(r["model"]) if r else ""
    if model.lower().startswith(manufacturer.lower()):
        model = model[len(manufacturer):].strip()
    aircraft = {"tail": tail, "model": model, "manufacturer": manufacturer}
    return render_template_string(MAINTENANCE_HTML, entries=entries, aircraft=aircraft, current_user=current_user)

@app.route('/my-aircraft/<tail>/maintenance/add', methods=['POST'])
@login_required
def add_maintenance_entry(tail):
    import json
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return redirect('/my-aircraft')
    doc_data = request.form.get('document', '') or None
    description = request.form.get('description', '').strip()
    performed_by = request.form.get('performed_by', '').strip() or None
    approved_by = request.form.get('approved_by', '').strip() or None
    entry_date = request.form.get('entry_date', '').strip() or None
    hours = request.form.get('hours_at_entry', '').strip() or None
    entry_type = request.form.get('entry_type', '').strip() or 'Other'
    if doc_data and not description:
        try:
            import anthropic as ac
            import json as js
            client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": doc_data}},
                    {"type": "text", "text": 'Extract from this aircraft maintenance document. Respond ONLY with JSON: {"entry_type": "Service/Repair/AD/Inspection/Component/Other", "description": "brief description", "performed_by": "name or null", "approved_by": "name or null", "entry_date": "DD/MM/YYYY or null", "hours_at_entry": number or null}'}
                ]}]
            )
            text = response.content[0].text
            clean = text.replace("```json", "").replace("```", "").strip()
            result = js.loads(clean)
            description = description or result.get("description", "")
            performed_by = performed_by or result.get("performed_by")
            approved_by = approved_by or result.get("approved_by")
            entry_date = entry_date or result.get("entry_date")
            hours = hours or result.get("hours_at_entry")
            entry_type = entry_type or result.get("entry_type", "Other")
        except Exception as e:
            print("AI fejl:", e)
    entry = AircraftMaintenanceLog(
        tail=tail, user_id=current_user.id, entry_date=entry_date,
        entry_type=entry_type, description=description, performed_by=performed_by,
        approved_by=approved_by, hours_at_entry=float(hours) if hours else None,
        document=doc_data[:500] if doc_data else None,
    )
    db.session.add(entry)
    db.session.commit()
    return redirect(f'/my-aircraft/{tail}/maintenance')

@app.route('/my-aircraft/<tail>/maintenance/delete/<int:entry_id>')
@login_required
def delete_maintenance_entry(tail, entry_id):
    import json
    claimed_list = json.loads(current_user.claimed_aircraft or '[]')
    if tail not in claimed_list:
        return redirect('/my-aircraft')
    entry = AircraftMaintenanceLog.query.get_or_404(entry_id)
    if entry.tail == tail:
        db.session.delete(entry)
        db.session.commit()
    return redirect(f'/my-aircraft/{tail}/maintenance')

MAINTENANCE_HTML = """<!DOCTYPE html>
<html>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
    <title>{{ aircraft.tail }} Maintenance - PanPanParts</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a1a2e; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .back { color: #666; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 24px; border: 1px solid #2a2a3e; margin-bottom: 16px; }
        .card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #666; margin-bottom: 16px; }
        .entry { padding: 16px 0; border-bottom: 1px solid #2a2a3e; display: flex; justify-content: space-between; align-items: flex-start; }
        .entry:last-child { border-bottom: none; }
        .entry-type { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; margin-bottom: 6px; }
        .type-Service { background: rgba(76,175,80,0.2); color: #4caf50; }
        .type-Inspection { background: rgba(33,150,243,0.2); color: #2196f3; }
        .type-Repair { background: rgba(255,152,0,0.2); color: #ff9800; }
        .type-AD { background: rgba(244,67,54,0.2); color: #f44336; }
        .type-Component { background: rgba(156,39,176,0.2); color: #9c27b0; }
        .type-Other { background: rgba(158,158,158,0.2); color: #9e9e9e; }
        .entry-desc { font-size: 14px; margin-bottom: 4px; }
        .entry-meta { font-size: 12px; color: #666; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; margin-left: 12px; }
        .delete-btn:hover { color: #ff6b35; }
        label { font-size: 12px; color: #666; display: block; margin-bottom: 4px; margin-top: 10px; }
        input[type=text], input[type=number], textarea, select { width: 100%; padding: 10px 12px; border: 1px solid #333; border-radius: 8px; font-size: 14px; background: #0d0d1a; color: white; margin-bottom: 4px; }
        textarea { height: 80px; resize: vertical; }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .add-btn { background: #ff6b35; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 15px; cursor: pointer; font-weight: 600; width: 100%; margin-top: 12px; }
        .upload-box { border: 2px dashed #333; border-radius: 8px; padding: 16px; text-align: center; cursor: pointer; color: #666; font-size: 13px; margin-bottom: 8px; }
        .upload-box:hover { border-color: #ff6b35; }
        .upload-box img { max-width: 100%; max-height: 150px; border-radius: 6px; display: none; margin-top: 8px; }
        input[type=file] { display: none; }
        .edit-btn { background: transparent; border: 1px solid #333; color: #aaa; padding: 6px 14px; border-radius: 6px; font-size: 12px; cursor: pointer; float: right; }
        .edit-btn:hover { border-color: #ff6b35; color: #ff6b35; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
    </div>
    <div class="container">
        <a href="/my-aircraft/{{ aircraft.tail }}" class="back">← {{ aircraft.tail }} cockpit</a>
        <h1 style="font-size:28px;margin-bottom:8px">{{ aircraft.tail }} <span style="color:#ff6b35">Maintenance Log</span></h1>
        <p style="color:#666;font-size:14px;margin-bottom:24px">{{ aircraft.manufacturer }} {{ aircraft.model }}</p>

        <!-- Entries -->
        <div class="card">
            <h3>Maintenance history ({{ entries|length }} entries)
                <button class="edit-btn" onclick="document.getElementById('add-form').classList.toggle('hidden')">+ Add entry</button>
            </h3>

            <!-- Add form -->
            <div id="add-form" class="hidden" style="margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid #2a2a3e">
                <form method="POST" action="/my-aircraft/{{ aircraft.tail }}/maintenance/add">
                    <input type="hidden" name="document" id="doc-data">
                    
                    <div class="upload-box" onclick="document.getElementById('doc-input').click()">
                        <img id="doc-preview">
                        <span id="doc-label">📷 Upload maintenance document (optional — AI reads automatically)</span>
                        <input type="file" id="doc-input" accept="image/*" onchange="loadDoc(this)">
                    </div>

                    <label>Entry type</label>
                    <select name="entry_type">
                        <option value="Service">100-hour Service</option>
                        <option value="Inspection">Annual Inspection</option>
                        <option value="Repair">Repair</option>
                        <option value="AD">AD Compliance</option>
                        <option value="Component">Component Replacement</option>
                        <option value="Other">Other</option>
                    </select>

                    <label>Description</label>
                    <textarea name="description" placeholder="Describe the work performed..."></textarea>

                    <div class="grid-2">
                        <div>
                            <label>Date (DD/MM/YYYY)</label>
                            <input type="text" name="entry_date" placeholder="e.g. 15/03/2026">
                        </div>
                        <div>
                            <label>Aircraft hours</label>
                            <input type="number" name="hours_at_entry" placeholder="Total hours" step="0.1">
                        </div>
                    </div>

                    <div class="grid-2">
                        <div>
                            <label>Performed by</label>
                            <input type="text" name="performed_by" placeholder="Mechanic / organization">
                        </div>
                        <div>
                            <label>Approved by</label>
                            <input type="text" name="approved_by" placeholder="Inspector / authority">
                        </div>
                    </div>

                    <button type="submit" class="add-btn">Save entry</button>
                </form>
            </div>

            {% if entries %}
                {% for e in entries[:5] %}
                <div class="entry">
                    <div style="flex:1">
                        <span class="entry-type type-{{ e.entry_type }}">{{ e.entry_type }}</span>
                        <div class="entry-desc">{{ e.description or '—' }}</div>
                        <div class="entry-meta">
                            {% if e.entry_date %}{{ e.entry_date }}{% endif %}
                            {% if e.hours_at_entry %} · {{ e.hours_at_entry }}h{% endif %}
                            {% if e.performed_by %} · {{ e.performed_by }}{% endif %}
                            {% if e.approved_by %} · Approved: {{ e.approved_by }}{% endif %}
                        </div>
                    </div>
                    <a href="/my-aircraft/{{ aircraft.tail }}/maintenance/delete/{{ e.id }}" 
                       class="delete-btn" onclick="return confirm('Delete?')">✕</a>
                </div>
                {% endfor %}
            {% else %}
                <p style="color:#444;font-size:14px;padding:16px 0">No maintenance entries yet. Add your first entry above.</p>
            {% endif %}
        </div>
    </div>

    <script>
        function loadDoc(input) {
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
                    canvas.width = w; canvas.height = h;
                    canvas.getContext("2d").drawImage(img, 0, 0, w, h);
                    var compressed = canvas.toDataURL("image/jpeg", 0.75);
                    document.getElementById("doc-preview").src = compressed;
                    document.getElementById("doc-preview").style.display = "block";
                    document.getElementById("doc-label").style.display = "none";
                    document.getElementById("doc-data").value = compressed.split(",")[1];
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    </script>
</body>
</html>"""

def run_monthly_updates():
    """Kører den 1. hver måned og opdaterer flyregistre"""
    try:
        import requests
        import psycopg2
        import psycopg2.extras
        import pandas as pd
        from io import StringIO
        
        print("Starter månedlig opdatering...")
        
        # Sverige — hent fra GitHub
        r = requests.get('https://raw.githubusercontent.com/civictechsweden/oppna-luftfartygsregistret/master/register.csv', timeout=30)
        if r.status_code == 200:
            df = pd.read_csv(StringIO(r.text), dtype=str)
            active = df[df['Avregistrerad'].isna()].copy()
            
            data = []
            for _, row in active.iterrows():
                data.append((
                    str(row.get('code', '') or '')[:20],
                    '',
                    str(row.get('Luftfartygstyp', '') or '')[:200],
                    str(row.get('Tillverkningsår', '') or '')[:10],
                    str(row.get('Tillverkningsnummer', '') or '')[:100],
                    'SE',
                    'Transportstyrelsen',
                    str(row.get('owner.name', '') or '')[:200],
                    '',
                    'Sweden'
                ))
            
            conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
            cur = conn.cursor()
            cur.execute("DELETE FROM aircraft WHERE country = 'SE'")
            psycopg2.extras.execute_batch(cur, '''
                INSERT INTO aircraft (registration, manufacturer, model, year, serial, country, source, owner, city, state)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', data)
            conn.commit()
            conn.close()
            print(f"Sverige opdateret: {len(data)} fly")
        
        print("Månedlig opdatering færdig!")
    
    except Exception as e:
        print(f"Månedlig opdatering fejl: {e}")
