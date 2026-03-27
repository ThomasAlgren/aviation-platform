with open('app.py', 'r') as f:
    content = f.read()

old = '''- CRITICAL: Preserve the EXACT order of rows as they appear on the page. Do NOT sort or reorder entries.
- Read rows strictly from top to bottom. Row 1 in the logbook must be row 1 in your output.
- Each row belongs to a specific line — do not mix data between rows.'''

new = '''- CRITICAL: Preserve the EXACT order of rows as they appear on the page. Do NOT sort or reorder entries.
- Read rows strictly from top to bottom. Row 1 in the logbook must be row 1 in your output.
- Each row belongs to a specific line — do not mix data between rows.
- At the bottom of the page there are totals: "Total This Page", "Total Previous Pages", "Total".
- Read these totals and include them in a "page_totals" field in your response.
- Calculate your own total of all flight times and compare with "Total This Page".
- If they differ, add a "validation_warning" field explaining the discrepancy.'''

if old in content:
    content = content.replace(old, new)
    print("Validering tilføjet!")
else:
    print("IKKE FUNDET")

# Opdater JSON format til at inkludere totals
old2 = '''Respond ONLY with a JSON array:
[{{'''
new2 = '''Respond ONLY with a JSON object:
{{
  "flights": [{{'''

if old2 in content:
    content = content.replace(old2, new2)
    print("JSON format opdateret!")
else:
    print("JSON format IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
