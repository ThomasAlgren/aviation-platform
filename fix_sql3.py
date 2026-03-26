with open('app.py', 'r') as f:
    content = f.read()

old = '''        if tail:
            conn_r = sql.connect(DB)
            existing = conn_r.execute("SELECT registration FROM aircraft WHERE registration = ?", (tail,)).fetchone()
            if not existing:
                conn_r.execute("INSERT INTO aircraft (registration, manufacturer, model, year, serial, country, owner, city, state, source) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (tail, manufacturer, model, year, \'\', country, current_user.name, \'\', country, \'User registered\'))
                conn_r.commit()
            conn_r.close()
            return redirect(\'/claim/\' + tail)'''

new = '''        if tail:
            conn_r = get_pg_conn()
            cur_r = conn_r.cursor()
            cur_r.execute("SELECT registration FROM aircraft WHERE registration = %s", (tail,))
            existing = cur_r.fetchone()
            if not existing:
                cur_r.execute("INSERT INTO aircraft (registration, manufacturer, model, year, serial, country, owner, city, state, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (tail, manufacturer, model, year, \'\', country, current_user.name, \'\', country, \'User registered\'))
                conn_r.commit()
            conn_r.close()
            return redirect(\'/claim/\' + tail)'''

if old in content:
    content = content.replace(old, new)
    print("Fix 3: OK")
else:
    print("Fix 3: IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
