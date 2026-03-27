with open('app.py', 'r') as f:
    content = f.read()

# Opdater my_profile route til at hente certifikater
old = '''    return render_template_string(MY_PROFILE_HTML,
        current_user=current_user,
        medical_days=medical_days,
        license_days=license_days)'''

new = '''    # Hent certifikater med dage til udløb
    from datetime import date
    raw_certs = PilotCertificate.query.filter_by(user_id=current_user.id).order_by(PilotCertificate.created_at).all()
    certificates = []
    for cert in raw_certs:
        days_left = None
        if cert.valid_until:
            try:
                exp = datetime.strptime(cert.valid_until, '%Y-%m-%d').date()
                days_left = (exp - date.today()).days
            except:
                pass
        certificates.append({
            'id': cert.id,
            'cert_type': cert.cert_type,
            'cert_number': cert.cert_number,
            'issued_by': cert.issued_by,
            'valid_until': cert.valid_until,
            'days_left': days_left
        })

    return render_template_string(MY_PROFILE_HTML,
        current_user=current_user,
        medical_days=medical_days,
        license_days=license_days,
        certificates=certificates)'''

if old in content:
    content = content.replace(old, new)
    print("my_profile route opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
