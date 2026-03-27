with open('app.py', 'r') as f:
    content = f.read()

old = '        table { width: 100%; border-collapse: collapse; font-size: 13px; }'
new = '''        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        @media (max-width: 600px) {
            table { font-size: 11px; }
            th, td { padding: 6px 4px; }
            .container { padding: 0 10px; }
            .header { padding: 16px 20px; }
            th:nth-child(4), td:nth-child(4) { display: none; }
            th:nth-child(7), td:nth-child(7) { display: none; }
        }'''

if old in content:
    content = content.replace(old, new)
    print("Mobile fix tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
