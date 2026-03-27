with open('app.py', 'r') as f:
    content = f.read()

# Fjern sortering - bevar indsættelses rækkefølge
old = '    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.created_at.desc()).all()\n    entries = sorted(entries, key=lambda e: e.flight_date or "", reverse=True)'
new = '    entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.id.asc()).all()'

if old in content:
    content = content.replace(old, new)
    print("Sortering fjernet!")
else:
    print("Sortering IKKE FUNDET")

# Opdater AI prompt - bevar rækkefølge
old2 = '- Only extract rows with actual flight data — skip empty rows.'
new2 = '''- Only extract rows with actual flight data — skip empty rows.
- CRITICAL: Preserve the EXACT order of rows as they appear on the page. Do NOT sort or reorder entries.
- Read rows strictly from top to bottom. Row 1 in the logbook must be row 1 in your output.
- Each row belongs to a specific line — do not mix data between rows.'''

if old2 in content:
    content = content.replace(old2, new2)
    print("Prompt rækkefølge tilføjet!")
else:
    print("Prompt IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
