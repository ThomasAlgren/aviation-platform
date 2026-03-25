content = open('app.py').read()

about_html = '''
ABOUT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>About - PanPanParts</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #0d0d1a; color: white; }
        .header { padding: 20px 40px; display: flex; justify-content: space-between; }
        .logo { font-size: 22px; font-weight: 700; }
        .logo span { color: #ff6b35; }
        .nav a { color: #aaa; text-decoration: none; font-size: 14px; margin-left: 24px; }
        .container { max-width: 760px; margin: 60px auto; padding: 0 20px; }
        h1 { font-size: 42px; font-weight: 700; margin-bottom: 16px; }
        h1 span { color: #ff6b35; }
        .lead { font-size: 18px; color: #aaa; line-height: 1.7; margin-bottom: 40px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 28px; margin-bottom: 20px; border: 1px solid #2a2a3e; }
        .card h3 { font-size: 16px; color: #ff6b35; margin-bottom: 12px; }
        .card p { color: #aaa; line-height: 1.7; font-size: 15px; }
        .contact { margin-top: 40px; color: #666; font-size: 14px; }
        .contact a { color: #ff6b35; text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="/" style="color:white;text-decoration:none">PanPan<span>Parts</span></a></div>
        <div class="nav"><a href="/parts">Parts for sale</a><a href="/upload">+ List a part</a></div>
    </div>
    <div class="container">
        <h1>About <span>PanPanParts</span></h1>
        <p class="lead">A global marketplace for verified aviation parts — built by a pilot, for the aviation community.</p>
        <div class="card"><h3>Why PanPanParts?</h3><p>Finding quality aviation parts has always been fragmented — scattered across forums, emails, and phone calls. PanPanParts brings it all together in one verified marketplace, making it faster and safer to buy and sell aircraft parts anywhere in the world.</p></div>
        <div class="card"><h3>AI-verified documentation</h3><p>Every part listed on PanPanParts goes through AI-powered document verification. Upload a photo of the part and its airworthiness certificate — our system checks it automatically and flags anything that needs a closer look.</p></div>
        <div class="card"><h3>Aircraft registry</h3><p>Search across 346,000+ registered aircraft from the USA, Denmark, Norway, Switzerland and Australia. More registries are being added continuously.</p></div>
        <div class="card"><h3>Pan Pan</h3><p>In aviation, Pan Pan is an urgency call — the step before Mayday. We chose the name because finding the right part quickly can be exactly that urgent.</p></div>
        <div class="contact">Questions: <a href="mailto:hello@panpanparts.com">hello@panpanparts.com</a></div>
    </div>
</body>
</html>
"""
'''

route = '''
@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML)
'''

open('app.py', 'w').write(content + about_html + route)
