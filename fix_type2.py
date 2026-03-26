with open('app.py', 'r') as f:
    content = f.read()

old = '        <a href="/" class="back">← Search</a>\n        <h1>{{ search }}</h1>'
new = '''        <form action="/" method="GET" class="search-bar">
            <input type="text" name="tail" placeholder="Search aircraft type, tail number..." value="{{ search }}">
            <button type="submit">Search</button>
        </form>
        <a href="/" class="back">← Search</a>
        <h1>{{ search }}</h1>'''

if old in content:
    content = content.replace(old, new)
    print("Søgebar tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
