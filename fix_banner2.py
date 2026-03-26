with open('app.py', 'r') as f:
    content = f.read()

old = '''            {% endif %}
        </div>
    </div>
    {% if not results %}
    <div class="hero">'''

new = '''            {% endif %}
        </div>
    </div>
    {% if current_user.is_authenticated and not current_user.email_verified %}
    <div class="verify-banner">
        ⚠ Please verify your email address. 
        <a href="/resend-verification">Resend verification email</a>
    </div>
    {% endif %}
    {% if not results %}
    <div class="hero">'''

if old in content:
    content = content.replace(old, new)
    print("Banner tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
