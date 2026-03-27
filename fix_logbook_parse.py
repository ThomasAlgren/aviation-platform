with open('app.py', 'r') as f:
    content = f.read()

old = '''    text = response.content[0].text
    clean = text.replace("```json", "").replace("```", "").strip()
    flights = json.loads(clean)
    
    # Gem flyvninger
    saved = 0
    for f in flights:'''

new = '''    text = response.content[0].text
    clean = text.replace("```json", "").replace("```", "").strip()
    parsed = json.loads(clean)
    
    # Håndter både gammelt array format og nyt objekt format
    if isinstance(parsed, list):
        flights = parsed
        validation_warning = None
        page_totals = None
    else:
        flights = parsed.get("flights", [])
        validation_warning = parsed.get("validation_warning")
        page_totals = parsed.get("page_totals")
    
    # Gem flyvninger
    saved = 0
    for f in flights:'''

if old in content:
    content = content.replace(old, new)
    print("Parse opdateret!")
else:
    print("IKKE FUNDET")

# Opdater return til at inkludere validering
old2 = "    return json.dumps({'ok': True, 'saved': saved, 'flights': flights})"
new2 = "    return json.dumps({'ok': True, 'saved': saved, 'flights': flights, 'validation_warning': validation_warning, 'page_totals': page_totals})"

if old2 in content:
    content = content.replace(old2, new2)
    print("Return opdateret!")
else:
    print("Return IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
