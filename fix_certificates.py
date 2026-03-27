with open('app.py', 'r') as f:
    content = f.read()

old = '''        </div>
    </div>
</body>
</html>"""

# Email verificering og password reset'''

new = '''        <!-- Certifikater -->
        <div class="card">
            <h3>Certificates & Ratings</h3>
            {% if certificates %}
            {% for cert in certificates %}
            <div class="date-item">
                <div>
                    <div style="font-size:14px;font-weight:600">{{ cert.cert_type }}</div>
                    {% if cert.cert_number %}<div style="font-size:12px;color:#666">{{ cert.cert_number }}</div>{% endif %}
                    {% if cert.issued_by %}<div style="font-size:12px;color:#666">{{ cert.issued_by }}</div>{% endif %}
                </div>
                <div style="text-align:right">
                    {% if cert.valid_until %}
                    <div class="date-value {% if cert.days_left is not none %}{% if cert.days_left < 0 %}date-alert{% elif cert.days_left < 60 %}date-warn{% else %}date-ok{% endif %}{% endif %}">
                        {{ cert.valid_until }}
                        {% if cert.days_left is not none and cert.days_left < 60 %}
                            {% if cert.days_left < 0 %} — EXPIRED{% else %} — {{ cert.days_left }} days{% endif %}
                        {% endif %}
                    </div>
                    {% else %}
                    <div style="color:#444;font-size:13px">No expiry</div>
                    {% endif %}
                    <a href="/delete-certificate/{{ cert.id }}" style="color:#444;font-size:11px;text-decoration:none" onclick="return confirm('Delete this certificate?')">remove</a>
                </div>
            </div>
            {% endfor %}
            {% else %}
            <p style="color:#444;font-size:14px;padding:12px 0">No certificates added yet.</p>
            {% endif %}

            <div style="margin-top:16px;border-top:1px solid #2a2a3e;padding-top:16px">
                <button class="edit-btn" style="float:none;margin:0 0 12px 0" onclick="document.getElementById('cert-form').classList.toggle('hidden')">+ Add certificate</button>
                <div id="cert-form" class="hidden">
                    <form method="POST" action="/add-certificate">
                        <label>Certificate type</label>
                        <select name="cert_type">
                            <option value="">Select type...</option>
                            <option>PPL Theory</option>
                            <option>PPL Licence</option>
                            <option>CPL Licence</option>
                            <option>ATPL Licence</option>
                            <option>Medical Class 1</option>
                            <option>Medical Class 2</option>
                            <option>LAPL Medical</option>
                            <option>Radio Certificate — National</option>
                            <option>Radio Certificate — International (English)</option>
                            <option>Rating — Night VFR</option>
                            <option>Rating — IFR</option>
                            <option>Rating — Tailwheel</option>
                            <option>Rating — Retractable Gear</option>
                            <option>Rating — Multi Engine (MEP)</option>
                            <option>Rating — SEP</option>
                            <option>Other</option>
                        </select>
                        <label>Certificate number (optional)</label>
                        <input type="text" name="cert_number" placeholder="e.g. DK.FCL.2026.PPL.12345">
                        <label>Issued by (optional)</label>
                        <input type="text" name="issued_by" placeholder="e.g. Trafikstyrelsen, FAA, CAA">
                        <label>Issue date (optional)</label>
                        <input type="text" name="issued_date" placeholder="YYYY-MM-DD">
                        <label>Valid until (leave blank if no expiry)</label>
                        <input type="text" name="valid_until" placeholder="YYYY-MM-DD">
                        <button type="submit" class="save-btn">Add certificate</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

# Email verificering og password reset'''

if old in content:
    content = content.replace(old, new)
    print("Certifikat sektion tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
