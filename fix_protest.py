with open('app.py', 'r') as f:
    content = f.read()

# Tilføj disputed til ClaimedAircraft model
old = '    notes = db.Column(db.Text)'
new = '''    notes = db.Column(db.Text)
    disputed = db.Column(db.Boolean, default=False)'''

if old in content:
    content = content.replace(old, new)
    print("ClaimedAircraft opdateret!")
else:
    print("ClaimedAircraft IKKE FUNDET")

# Tilføj ClaimProtest model
old2 = 'class AircraftListing(db.Model):'
new2 = '''class ClaimProtest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tail = db.Column(db.String(20))
    protester_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    protester_email = db.Column(db.String(200))
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AircraftListing(db.Model):'''

if old2 in content:
    content = content.replace(old2, new2)
    print("ClaimProtest model tilføjet!")
else:
    print("ClaimProtest IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
