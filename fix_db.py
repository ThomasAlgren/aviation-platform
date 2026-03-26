with open('app.py', 'r') as f:
    content = f.read()

old = '''print("Loader FAA data...")
import sqlite3 as sql
DB = os.path.join(DB_PATH, 'panpanparts.db')

def search_aircraft(query, limit=50):
    conn = sql.connect(DB)
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute(\'\'\'
        SELECT * FROM aircraft 
        WHERE registration LIKE ? 
        OR manufacturer LIKE ? 
        OR model LIKE ?
        LIMIT ?
    \'\'\', (f\'%{query}%\', f\'%{query}%\', f\'%{query}%\', limit))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_aircraft(registration):
    conn = sql.connect(DB)
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute(\'SELECT * FROM aircraft WHERE registration = ?\', (registration,))
    row = cur.fetchone()
    conn.close()
    return row
print("Klar!")'''

new = '''print("Connecting to PostgreSQL...")
import psycopg2
import psycopg2.extras

def get_pg_conn():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def search_aircraft(query, limit=50):
    conn = get_pg_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""
        SELECT * FROM aircraft 
        WHERE registration ILIKE %s 
        OR manufacturer ILIKE %s 
        OR model ILIKE %s
        LIMIT %s
    """, (f"%{query}%", f"%{query}%", f"%{query}%", limit))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_aircraft(registration):
    conn = get_pg_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM aircraft WHERE registration = %s", (registration,))
    row = cur.fetchone()
    conn.close()
    return row
print("Klar!")'''

if old in content:
    content = content.replace(old, new)
    print("FUNDET OG ERSTATTET!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
