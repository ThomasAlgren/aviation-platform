with open('app.py', 'r') as f:
    content = f.read()

old = '''    # Statistik for flytype
    model_query = aircraft["model"] if aircraft["model"] else ""
    if model_query:
        import psycopg2.extras
        conn_stat = get_pg_conn()
        cur_stat = conn_stat.cursor()
        cur_stat.execute("SELECT COUNT(*) FROM aircraft WHERE model = %s", (model_query,))
        total = cur_stat.fetchone()[0]
        cur_stat.execute("SELECT COUNT(*) FROM aircraft WHERE model = %s AND country = %s", (model_query, "DK"))
        in_country = cur_stat.fetchone()[0]
        conn_stat.close()
    else:
        total = 0
        in_country = 0'''

new = '''    # Statistik for flytype
    model_query = aircraft["model"] if aircraft["model"] else ""
    if model_query:
        conn_stat = get_pg_conn()
        cur_stat = conn_stat.cursor()
        model_clean = model_query.replace("-", "")
        cur_stat.execute("SELECT COUNT(*) FROM aircraft WHERE REPLACE(model, '-', '') ILIKE %s", (model_clean,))
        total = cur_stat.fetchone()[0]
        cur_stat.execute("SELECT COUNT(*) FROM aircraft WHERE REPLACE(model, '-', '') ILIKE %s AND country = %s", (model_clean, "DK"))
        in_country = cur_stat.fetchone()[0]
        conn_stat.close()
    else:
        total = 0
        in_country = 0'''

if old in content:
    content = content.replace(old, new)
    print("Fix stats: OK")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
