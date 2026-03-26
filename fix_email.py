with open('app.py', 'r') as f:
    content = f.read()

# Tilføj kolonner til User model
old = '    medical_document = db.Column(db.Text)'
new = '''    medical_document = db.Column(db.Text)
    email_verified = db.Column(db.Boolean, default=False)
    verification_token = db.Column(db.String(100))
    reset_token = db.Column(db.String(100))
    reset_token_expires = db.Column(db.DateTime)'''

if old in content:
    content = content.replace(old, new)
    print("User model opdateret!")
else:
    print("User model IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
