with open('app.py', 'r') as f:
    content = f.read()

old = '''        <div class="link">No account? <a href="/register">Sign up free</a></div>'''
new = '''        <div class="link">No account? <a href="/register">Sign up free</a></div>
        <div class="link" style="margin-top:10px"><a href="/forgot-password" style="color:#666;font-size:13px">Forgot password?</a></div>'''

if old in content:
    content = content.replace(old, new)
    print("Forgot password link tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
