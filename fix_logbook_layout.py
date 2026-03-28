with open('app.py', 'r') as f:
    content = f.read()

old = '        table { width: 100%; border-collapse: collapse; font-size: 13px; }\n        th { text-align: left; padding: 10px 8px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; }\n        td { padding: 10px 8px; border-bottom: 1px solid #1a1a2e; }\n        tr:hover td { background: #1a1a2e; }\n        .total-row { color: #ff6b35; font-weight: 600; }\n        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }\n        .delete-btn:hover { color: #ff6b35; }\n        .user-menu { position: relative; margin-left: 8px; }'

new = '''        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th { text-align: left; padding: 10px 8px; color: #666; font-size: 11px; text-transform: uppercase; border-bottom: 1px solid #2a2a3e; white-space: nowrap; }
        td { padding: 10px 8px; border-bottom: 1px solid #1a1a2e; white-space: nowrap; }
        tr:hover td { background: #1a1a2e; }
        .total-row td { color: #ff6b35; font-weight: 600; border-top: 2px solid #2a2a3e; }
        .delete-btn { color: #444; text-decoration: none; font-size: 11px; }
        .delete-btn:hover { color: #ff6b35; }
        .desktop-only { display: table-cell; }
        .mobile-table { display: none; }
        @media (max-width: 768px) {
            .desktop-only { display: none; }
            .desktop-table { display: none; }
            .mobile-table { display: block; }
        }
        .user-menu { position: relative; margin-left: 8px; }'''

if old in content:
    content = content.replace(old, new)
    print("CSS opdateret!")
else:
    print("CSS IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
