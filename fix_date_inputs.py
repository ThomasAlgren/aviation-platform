with open('app.py', 'r') as f:
    content = f.read()

replacements = [
    # ARC
    ('placeholder="ARC valid until (e.g. 2026-12-01)"', 'type="date"'),
    # CoA
    ('placeholder="CoA valid until"', 'type="date"'),
    # Insurance
    ('placeholder="Insurance valid until"', 'type="date"'),
    # Last service
    ('placeholder="Last service date"', 'type="date"'),
    # Next service
    ('placeholder="Next service date"', 'type="date"'),
    # License
    ('placeholder="YYYY-MM-DD" value="{{ current_user.license_valid_until', 'type="date" value="{{ current_user.license_valid_until'),
    # Medical
    ('placeholder="YYYY-MM-DD" value="{{ current_user.medical_valid_until', 'type="date" value="{{ current_user.medical_valid_until'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"Rettet: {old[:40]}...")

print(f"Total: {count} felter rettet")

with open('app.py', 'w') as f:
    f.write(content)
