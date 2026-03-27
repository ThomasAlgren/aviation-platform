with open('app.py', 'r') as f:
    content = f.read()

old = '''IMPORTANT:
- Dates are DD/MM/YY or DD/MM/YYYY. Year 25 = 2025, 26 = 2026.
- Aircraft registrations: OY-XXX (Denmark), LN-XXX (Norway), N12345 (USA). Read carefully.
- Times are H:MM format. Space between hours and minutes is common.
- Only extract rows with actual flight data.'''

new = '''IMPORTANT:
- Dates are ALWAYS in DD/MM/YY format (European). Day first, then month, then 2-digit year.
- Examples: 02/10/25 = 02/10/2025, 20/01/26 = 20/01/2026, 04/03/26 = 04/03/2026.
- NEVER interpret dates as MM/DD/YY — this is a European logbook.
- Aircraft registrations: OY-XXX (Denmark), LN-XXX (Norway), N12345 (USA). 
- Danish registrations are always OY- followed by 3 letters. Read each letter carefully.
- Times are H:MM format. A space between digits means colon e.g. "1 55" = 1:55.
- Only extract rows with actual flight data — skip empty rows.'''

if old in content:
    content = content.replace(old, new)
    print("Dato prompt opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
