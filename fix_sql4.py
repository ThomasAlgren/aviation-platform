with open('app.py', 'r') as f:
    content = f.read()

old = '''    conn_s = sql.connect(DB)
    rows = conn_s.execute(
        "SELECT registration FROM aircraft LIMIT ? OFFSET ?", 
        (limit, offset)
    ).fetchall()
    conn_s.close()'''

new = '''    conn_s = get_pg_conn()
    cur_s = conn_s.cursor()
    cur_s.execute("SELECT registration FROM aircraft LIMIT %s OFFSET %s", (limit, offset))
    rows = cur_s.fetchall()
    conn_s.close()'''

if old in content:
    content = content.replace(old, new)
    print("Fix 4: OK")
else:
    print("Fix 4: IKKE FUNDET")

# Ret også row[0] til tuple index
old2 = '        reg = row[0]'
new2 = '        reg = row[0]'

with open('app.py', 'w') as f:
    f.write(content)
