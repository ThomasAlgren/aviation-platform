with open('app.py', 'r') as f:
    content = f.read()

old = '''            {% for cert in certificates %}
            <div class="date-item">
                <div>
                    <div style="font-size:14px;font-weight:600">{{ cert.cert_type }}</div>
                    {% if cert.cert_number %}<div style="font-size:12px;color:#666">{{ cert.cert_number }}</div>{% endif %}
                    {% if cert.issued_by %}<div style="font-size:12px;color:#666">{{ cert.issued_by }}</div>{% endif %}
                </div>'''

new = '''            {% for cert in certificates %}
            <div class="date-item" onclick="showCert({{ cert.id }})" style="cursor:pointer">
                <div>
                    <div style="font-size:14px;font-weight:600">{{ cert.cert_type }}</div>
                    {% if cert.cert_number %}<div style="font-size:12px;color:#666">{{ cert.cert_number }}</div>{% endif %}
                    {% if cert.issued_by %}<div style="font-size:12px;color:#666">{{ cert.issued_by }}</div>{% endif %}
                </div>'''

if old in content:
    content = content.replace(old, new)
    print("OK!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
