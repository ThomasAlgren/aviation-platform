with open('app.py', 'r') as f:
    content = f.read()

old = 'class LogbookEntry(db.Model):'
new = '''class AircraftMaintenanceLog(db.Model):
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

class LogbookEntry(db.Model):'''

if old in content:
    content = content.replace(old, new)
    print("AircraftMaintenanceLog model tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
