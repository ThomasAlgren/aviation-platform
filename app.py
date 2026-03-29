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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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

        <div id="search" style="margin-top:32px">
            <form method="GET">
                <div class="search-box">
                    <input name="tail" placeholder="Find your aircraft — e.g. OY-RYY or N12345..." value="{{ tail }}">
                    <button type="submit">Search</button>
                </div>
            </form>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
            ai_description=ai_description,
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
        return _json.dumps({'matches': listings, 'suggestion': None})


AIRCRAFT_FOR_SALE_HTML = """<!DOCTYPE html>
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
                <a href="/" class="btn-list">+ List your aircraft — free</a>
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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3PJMNF1JE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K3PJMNF1JE');
    </script>
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
        .info-bar { display: flex; align-items: stretch; background: #0d0d1a; border-bottom: 1px solid #1a2a1a; font-family: monospace; }
        .info-bar-gauge { padding: 12px 16px; border-right: 1px solid #1a2a1a; text-align: center; flex-shrink: 0; }
        .info-bar-price { padding: 12px 20px; display: flex; flex-direction: column; justify-content: center; flex-shrink: 0; border-right: 1px solid #1a2a1a; }
        .info-bar-thumbs { display: flex; gap: 6px; padding: 8px 12px; align-items: center; overflow-x: auto; flex: 1; }
        .info-bar-gauge-lbl { font-size: 9px; color: #4a8a4a; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 4px; }
        .info-bar-gauge-val { font-size: 12px; color: #ccc; font-weight: 700; margin-top: 4px; }
        .info-bar-price-amount { font-size: 26px; font-weight: 800; color: #ff6b35; font-family: monospace; line-height: 1; }
        .info-bar-price-label { font-size: 9px; color: #666; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
        .info-bar-badges { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px; }
        .info-thumb { width: 80px; height: 60px; object-fit: cover; border-radius: 4px; cursor: pointer; opacity: 0.6; flex-shrink: 0; }
        .info-thumb.active { opacity: 1; outline: 2px solid #ff6b35; }
        .hero-wrap { position: relative; }
        .hero-nav { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; font-size: 28px; width: 52px; height: 52px; border-radius: 50%; cursor: pointer; z-index: 10; transition: background 0.2s; display: flex; align-items: center; justify-content: center; }
        .hero-nav:hover { background: rgba(255,107,53,0.8); }
        .hero-nav-left { left: 16px; }
        .hero-nav-right { right: 16px; }
        .thumb { width: 80px; height: 60px; object-fit: cover; border-radius: 4px; cursor: pointer; opacity: 0.6; flex-shrink: 0; }
        .thumb.active { opacity: 1; outline: 2px solid #ff6b35; }
        
        .container { max-width: 1000px; margin: 0 auto; padding: 32px 20px; }
        .layout { display: block; max-width: 900px; }

        
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
        
        /* Health panel */
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
    <div class="hero-wrap">
    {% if listing.hero_image %}
    <img class="hero-img" id="hero-img" src="{{ listing.hero_image }}" alt="{{ listing.tail }}">
    {% elif images %}
    <img class="hero-img" id="hero-img" src="{{ images[0] }}" alt="{{ listing.tail }}">
    {% else %}
    <div class="hero-placeholder">✈️</div>
    {% endif %}
    {% if images|length > 1 %}
    <button class="hero-nav hero-nav-left" onclick="navHero(-1)">&#8592;</button>
    <button class="hero-nav hero-nav-right" onclick="navHero(1)">&#8594;</button>
    {% endif %}
    </div>
    <script>
        var allImages = [{% for img in images %}'{{ img }}'{% if not loop.last %},{% endif %}{% endfor %}];
        var currentIndex = 0;
    </script>

    <!-- INFO BAR: titel + gauges + pris + thumbnails -->
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
        <div class="info-bar-price">
            <div class="info-bar-price-label">Asking price</div>
            <div class="info-bar-price-amount">EUR {{ "{:,.0f}".format(listing.price) }}</div>
            <div class="info-bar-badges">
                {% if listing.has_autopilot %}<span class="hbadge yes">▲ AP</span>{% endif %}
                {% if listing.has_adsb %}<span class="hbadge yes">▲ ADS-B</span>{% endif %}
                {% if listing.is_hangared %}<span class="hbadge yes">▲ HANGAR</span>{% endif %}
                {% if listing.arc_verified %}<span class="hbadge yes">▲ ARC</span>{% endif %}
            </div>
        </div>
        <!-- Thumbnails til højre -->
        {% if images|length > 1 %}
        <div class="info-bar-thumbs">
            {% for img in images %}
            <img class="info-thumb {% if loop.first %}active{% endif %}" src="{{ img }}" onclick="setHero(this, '{{ img }}')">
            {% endfor %}
        </div>
        {% endif %}
    </div>

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

                <!-- Kontakt -->
                <div style="background:#1a1a2e;border-radius:16px;padding:24px;border:1px solid #2a2a3e;margin-top:8px;">
                    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
                        <div>
                            <div style="font-size:13px;color:#666;margin-bottom:4px;">Listed by</div>
                            <div style="font-size:16px;font-weight:600;">{{ listing.contact_name }}</div>
                            <div style="font-size:14px;color:#aaa;">{{ listing.contact_email }}</div>
                            {% if listing.contact_phone %}<div style="font-size:14px;color:#aaa;">{{ listing.contact_phone }}</div>{% endif %}
                        </div>
                        <div style="text-align:right;">
                            <a href="mailto:{{ listing.contact_email }}?subject=Re: {{ listing.tail }} for sale on PanPanParts" class="btn-contact" style="display:inline-block;padding:14px 32px;font-size:16px;">✉ Send message</a>
                            <div style="font-size:12px;color:#444;margin-top:8px;">{{ listing.views or 0 }} views</div>
                        </div>
                    </div>
                </div>
            </div>

        <script>
        // Tegn gauges med canvas
        window.addEventListener("load", function() {
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

            // Baggrund arc
            ctx.beginPath();
            ctx.arc(cx, cy, r, startAngle, endAngle);
            ctx.strokeStyle = '#1a2a1a';
            ctx.lineWidth = 12;
            ctx.lineCap = 'butt';
            ctx.stroke();

            // Gradient arc
            var grad = ctx.createLinearGradient(14, 0, 116, 0);
            grad.addColorStop(0, '#4caf50');
            grad.addColorStop(0.55, '#ffc107');
            grad.addColorStop(1, '#f44336');
            ctx.beginPath();
            ctx.arc(cx, cy, r, startAngle, endAngle);
            ctx.strokeStyle = grad;
            ctx.globalAlpha = 0.8;
            ctx.stroke();
            ctx.globalAlpha = 1;

            // Tick marks
            ctx.strokeStyle = '#2a3a2a';
            ctx.lineWidth = 1;
            [[14,76,19,71],[29,43,35,46],[65,28,65,35],[101,43,95,46],[116,76,111,71]].forEach(function(t) {
                ctx.beginPath(); ctx.moveTo(t[0],t[1]); ctx.lineTo(t[2],t[3]); ctx.stroke();
            });

            // Nål
            var angle = Math.PI + (pct / 100) * Math.PI;
            var nx = cx + r * Math.cos(angle);
            var ny = cy + r * Math.sin(angle);
            ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(nx, ny);
            ctx.strokeStyle = '#000'; ctx.lineWidth = 4; ctx.lineCap = 'round';
            ctx.globalAlpha = 0.4; ctx.stroke(); ctx.globalAlpha = 1;
            ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(nx, ny);
            ctx.strokeStyle = '#fff'; ctx.lineWidth = 2.5; ctx.stroke();

            // Hub
            ctx.beginPath(); ctx.arc(cx, cy, 5, 0, 2*Math.PI);
            ctx.fillStyle = '#0d0d1a'; ctx.fill();
            ctx.strokeStyle = color; ctx.lineWidth = 1.5; ctx.stroke();
            ctx.beginPath(); ctx.arc(cx, cy, 2, 0, 2*Math.PI);
            ctx.fillStyle = color; ctx.fill();

            // Label
            ctx.fillStyle = color;
            ctx.font = 'bold 12px monospace';
            ctx.textAlign = 'center';
            ctx.fillText(label || pct + '%', cx, 62);
        });
        }); // end load
        function setHero(thumb, src) {
            document.getElementById('hero-img').src = src;
            document.querySelectorAll('.thumb, .info-thumb').forEach(t => t.classList.remove('active'));
            thumb.classList.add('active');
            currentIndex = allImages.indexOf(src);
        }

        function navHero(dir) {
            if (allImages.length === 0) return;
            currentIndex = (currentIndex + dir + allImages.length) % allImages.length;
            var src = allImages[currentIndex];
            document.getElementById('hero-img').src = src;
            document.querySelectorAll('.thumb').forEach(function(t, i) {
                t.classList.toggle('active', i === currentIndex);
            });
        }

        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') navHero(-1);
            if (e.key === 'ArrowRight') navHero(1);
        });
    </script>
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
