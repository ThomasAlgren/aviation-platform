with open('app.py', 'r') as f:
    content = f.read()

old = '        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }'
new = '''        .back { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-bottom: 24px; }
        .search-bar { display: flex; gap: 10px; margin-bottom: 32px; }
        .search-bar input { flex: 1; padding: 14px 16px; border: 1px solid #333; border-radius: 10px; font-size: 16px; background: #1a1a2e; color: white; }
        .search-bar button { background: #ff6b35; color: white; border: none; padding: 14px 24px; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: 600; }
        .ai-box { background: #1a1a2e; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 3px solid #ff6b35; color: #ccc; font-size: 15px; line-height: 1.6; }'''

content = content.replace(old, new)

old2 = '        <a href="/" class="back">← Back to search</a>\n        <h1>{{ search }}</h1>'
new2 = '''        <form action="/" method="GET" class="search-bar">
            <input type="text" name="tail" placeholder="Search aircraft type, tail number..." value="{{ search }}">
            <button type="submit">Search</button>
        </form>
        <a href="/" class="back">← Back to search</a>
        <h1>{{ search }}</h1>
        {% if ai_description %}
        <div class="ai-box">{{ ai_description }}</div>
        {% endif %}'''

if old2 in content:
    content = content.replace(old2, new2)
    print("Søgebar tilføjet!")
else:
    print("old2 IKKE FUNDET")

if old in content:
    print("FEJL: old1 ikke erstattet")
else:
    print("Styling tilføjet!")

with open('app.py', 'w') as f:
    f.write(content)
