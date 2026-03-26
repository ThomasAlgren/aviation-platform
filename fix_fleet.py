with open('app.py', 'r') as f:
    content = f.read()

# Fjern fleet statistics HTML blok
old = '''        {% if type_total %}
            <h3>Fleet statistics</h3>
            <div class="field"><span class="field-label">{{ aircraft.model }} in {{ country_name }}</span><span class="field-value">{{ type_in_country }} aircraft</span></div>
            <div class="field"><span class="field-label">{{ aircraft.model }} worldwide</span><span class="field-value">{{ type_total }} aircraft</span></div>'''

new = ''

if old in content:
    content = content.replace(old, new)
    print("Fleet statistics HTML fjernet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
