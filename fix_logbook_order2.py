with open('app.py', 'r') as f:
    content = f.read()

old = '    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.flight_date.desc()).all()'
new = '    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.id.asc()).all()'

if old in content:
    content = content.replace(old, new)
    print("Sortering rettet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
