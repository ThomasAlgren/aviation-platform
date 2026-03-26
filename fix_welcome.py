with open('app.py', 'r') as f:
    content = f.read()

# Find startsiden og tilføj velkomstbesked
old = '''@app.route("/")
def index():'''

new = '''@app.route("/")
def index():
    welcome = request.args.get("welcome")
    if welcome and current_user.is_authenticated and not current_user.email_verified:
        flash("Welcome! Please check your email and verify your account.", "info")'''

if old in content:
    content = content.replace(old, new)
    print("Welcome besked tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
