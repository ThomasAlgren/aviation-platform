with open('app.py', 'r') as f:
    content = f.read()

old = '''@app.route('/my-logbook')
@login_required
def my_logbook():
    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.flight_date.desc()).all()
    return render_template_string(LOGBOOK_HTML, entries=entries, current_user=current_user)'''

new = '''@app.route('/my-logbook')
@login_required
def my_logbook():
    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.flight_date.desc()).all()
    
    total_minutes = 0
    for e in entries:
        if e.total_time and e.total_time not in ['—', '-', '']:
            try:
                parts = e.total_time.replace(":", " ").replace(".", " ").split()
                if len(parts) == 2:
                    total_minutes += int(parts[0]) * 60 + int(parts[1])
            except:
                pass
    total_hours = total_minutes // 60
    total_mins = total_minutes % 60
    total_str = f"{total_hours}:{total_mins:02d}" if total_minutes > 0 else "0:00"
    
    return render_template_string(LOGBOOK_HTML, entries=entries, current_user=current_user, total_time=total_str, total_flights=len(entries))'''

if old in content:
    content = content.replace(old, new)
    print("Route opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
