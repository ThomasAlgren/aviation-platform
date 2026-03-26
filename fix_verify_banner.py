with open('app.py', 'r') as f:
    content = f.read()

old = '''        .tab { padding: 8px 20px; border-radius: 20px; font-size: 14px; cursor: pointer; border: 1px solid #333; color: #aaa; background: transparent; }'''

new = '''        .tab { padding: 8px 20px; border-radius: 20px; font-size: 14px; cursor: pointer; border: 1px solid #333; color: #aaa; background: transparent; }
        .verify-banner { background: rgba(255,193,7,0.15); border-bottom: 1px solid rgba(255,193,7,0.3); padding: 12px 40px; text-align: center; font-size: 14px; color: #ffc107; }
        .verify-banner a { color: #ff6b35; text-decoration: none; font-weight: 600; }'''

if old in content:
    content = content.replace(old, new)
    print("Banner CSS tilføjet!")
else:
    print("CSS IKKE FUNDET")

# Tilføj banner HTML efter body tag i SEARCH_HTML
old2 = '''    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">'''

new2 = '''    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav">'''

if old2 in content:
    content = content.replace(old2, new2)
    print("Banner HTML tilføjet!")
else:
    print("HTML IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
