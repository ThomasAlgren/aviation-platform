with open('app.py', 'r') as f:
    content = f.read()

old = '''    if request.method == 'POST':
        fields = ['license_number', 'license_type', 'license_valid_until',
                  'medical_class', 'medical_valid_until', 'total_flight_hours', 'ratings']
        for field in fields:
            val = request.form.get(field)
            if val is not None:
                setattr(current_user, field, val)
        db.session.commit()
        return redirect('/my-profile')'''

new = '''    if request.method == 'POST':
        date_fields = ['license_valid_until', 'medical_valid_until']
        other_fields = ['license_number', 'license_type', 'medical_class', 'total_flight_hours', 'ratings']
        for field in other_fields:
            val = request.form.get(field)
            if val is not None:
                setattr(current_user, field, val)
        for field in date_fields:
            val = request.form.get(field)
            if val is not None:
                setattr(current_user, field, normalize_date(val))
        db.session.commit()
        return redirect('/my-profile')'''

if old in content:
    content = content.replace(old, new)
    print("Profile dates normaliseret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
