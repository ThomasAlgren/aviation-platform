with open('app.py', 'r') as f:
    content = f.read()

old = '''        import sqlite3 as sql2
        conn2 = sql2.connect(DB)
        registry_count = conn2.execute("SELECT COUNT(*) FROM aircraft").fetchone()[0]
        conn2.close()'''

new = '''        conn2 = get_pg_conn()
        cur2 = conn2.cursor()
        cur2.execute("SELECT COUNT(*) FROM aircraft")
        registry_count = cur2.fetchone()[0]
        conn2.close()'''

if old in content:
    content = content.replace(old, new)
    print("Fix 5: OK")
else:
    print("Fix 5: IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
