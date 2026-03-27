with open('app.py', 'r') as f:
    content = f.read()

# Tilføj nye kolonner til LogbookEntry model
old = '''    remarks = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PilotCertificate(db.Model):'''

new = '''    remarks = db.Column(db.Text)
    mep_vfr = db.Column(db.String(10))
    mep_ifr = db.Column(db.String(10))
    pic_time = db.Column(db.String(10))
    copilot_time = db.Column(db.String(10))
    instructor_time = db.Column(db.String(10))
    multipilot_time = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PilotCertificate(db.Model):'''

if old in content:
    content = content.replace(old, new)
    print("Model opdateret!")
else:
    print("Model IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
