with open('app.py', 'r') as f:
    content = f.read()

old = '''        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        @media (max-width: 600px) {
            table { font-size: 11px; }
            th, td { padding: 6px 4px; }
            .container { padding: 0 10px; }
            .header { padding: 16px 20px; }
            th:nth-child(4), td:nth-child(4) { display: none; }
            th:nth-child(7), td:nth-child(7) { display: none; }
        }
        th { text-align: left; padding: 10px 8px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; }
        td { padding: 10px 8px; border-bottom: 1px solid #1a1a2e; }
        tr:hover td { background: #1a1a2e; }
        .total-row { color: #ff6b35; font-weight: 600; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }
        .delete-btn:hover { color: #ff6b35; }'''

new = '''        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th { text-align: left; padding: 8px 6px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; white-space: nowrap; }
        td { padding: 8px 6px; border-bottom: 1px solid #1a1a2e; white-space: nowrap; }
        tr:hover td { background: #1a1a2e; cursor: pointer; }
        .total-row td { color: #ff6b35; font-weight: 600; border-top: 2px solid #2a2a3e; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }
        .delete-btn:hover { color: #ff6b35; }
        .desktop-col { display: table-cell; }
        @media (max-width: 768px) {
            .desktop-col { display: none; }
            .container { padding: 0 10px; }
            .header { padding: 16px 20px; }
            table { font-size: 12px; }
        }'''

if old in content:
    content = content.replace(old, new)
    print("CSS opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
