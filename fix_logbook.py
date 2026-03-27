with open('app.py', 'r') as f:
    content = f.read()

# Tilføj LogbookEntry model
old = 'class PilotCertificate(db.Model):'
new = '''class LogbookEntry(db.Model):
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

class PilotCertificate(db.Model):'''

if old in content:
    content = content.replace(old, new)
    print("LogbookEntry model tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
