with open('app.py', 'r') as f:
    content = f.read()

old = '''@app.route('/claim/<tail>')
def claim(tail):
    if not current_user.is_authenticated:
        return redirect('/register?next=/claim/' + tail)
    import json
    user = User.query.get(current_user.id)
    claimed = json.loads(user.claimed_aircraft or '[]')
    if tail.upper() not in claimed:
        claimed.append(tail.upper())
        user.claimed_aircraft = json.dumps(claimed)
        db.session.commit()
    return redirect('/aircraft/' + tail + '?claimed=1')'''

new = '''@app.route('/claim/<tail>')
def claim(tail):
    if not current_user.is_authenticated:
        return redirect('/register?next=/claim/' + tail)
    import json
    user = User.query.get(current_user.id)
    claimed = json.loads(user.claimed_aircraft or '[]')
    if tail.upper() not in claimed:
        claimed.append(tail.upper())
        user.claimed_aircraft = json.dumps(claimed)
        db.session.commit()
    
    # Opret ClaimedAircraft record hvis den ikke findes
    existing = ClaimedAircraft.query.filter_by(tail=tail.upper()).first()
    if not existing:
        ca = ClaimedAircraft(
            user_id=current_user.id,
            tail=tail.upper()
        )
        db.session.add(ca)
        db.session.commit()
    
    return redirect('/my-aircraft/' + tail.upper())'''

if old in content:
    content = content.replace(old, new)
    print("Claim route rettet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
