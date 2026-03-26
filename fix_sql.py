with open('app.py', 'r') as f:
    content = f.read()

# Fix 1: index route søgning
old1 = '''    if any([tail, model, state, year_from, year_to]):
        conn = sql.connect(DB)
        conn.row_factory = sql.Row
        cur = conn.cursor()
        query = "SELECT * FROM aircraft WHERE 1=1"
        params = []
        if tail:
            t = tail.upper()
            query += " AND registration LIKE ?"
            params.append(f\'%{t}%\')
        if model:
            query += " AND model LIKE ?"
            params.append(f\'%{model}%\')
        if state:
            query += " AND state = ?"
            params.append(state)
        if year_from:
            query += " AND CAST(year AS INTEGER) >= ?"
            params.append(int(year_from))
        if year_to:
            query += " AND CAST(year AS INTEGER) <= ?"
            params.append(int(year_to))
        query += " LIMIT 20"
        cur.execute(query, params)
        rows = cur.fetchall()
        conn.close()'''

new1 = '''    if any([tail, model, state, year_from, year_to]):
        import psycopg2.extras
        conn = get_pg_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM aircraft WHERE 1=1"
        params = []
        if tail:
            t = tail.upper()
            query += " AND registration ILIKE %s"
            params.append(f\'%{t}%\')
        if model:
            query += " AND model ILIKE %s"
            params.append(f\'%{model}%\')
        if state:
            query += " AND state = %s"
            params.append(state)
        if year_from:
            query += " AND CAST(year AS INTEGER) >= %s"
            params.append(int(year_from))
        if year_to:
            query += " AND CAST(year AS INTEGER) <= %s"
            params.append(int(year_to))
        query += " LIMIT 20"
        cur.execute(query, params)
        rows = cur.fetchall()
        conn.close()'''

if old1 in content:
    content = content.replace(old1, new1)
    print("Fix 1: OK")
else:
    print("Fix 1: IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
