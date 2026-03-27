with open('app.py', 'r') as f:
    content = f.read()

old = 'class ClaimProtest(db.Model):'
new = '''class PilotCertificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    cert_type = db.Column(db.String(100))
    cert_number = db.Column(db.String(100))
    issued_by = db.Column(db.String(200))
    issued_date = db.Column(db.String(50))
    valid_until = db.Column(db.String(50))
    document = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ClaimProtest(db.Model):'''

if old in content:
    content = content.replace(old, new)
    print("PilotCertificate model tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
