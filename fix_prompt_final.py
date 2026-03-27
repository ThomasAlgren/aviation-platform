with open('app.py', 'r') as f:
    content = f.read()

old = '''    content_parts.append({"type": "text", "text": """These are pages from a pilot logbook. Extract all flight entries.
Respond ONLY with a JSON array of flights:
[{
  "flight_date": "DD/MM/YY format as written",
  "dep_place": "departure ICAO or place",
  "arr_place": "arrival ICAO or place",
  "off_block": "HH:MM or null",
  "on_block": "HH:MM or null",
  "aircraft_type": "type as written",
  "registration": "registration as written",
  "pilot_in_command": "name or null",
  "total_time": "H:MM format",
  "night_time": "H:MM or null",
  "sep_vfr": "H:MM or null",
  "dual": "H:MM or null",
  "landings_day": number or null,
  "landings_night": number or null,
  "remarks": "any remarks or null"
}]"""})'''

new = '''    context_hint = ""
    if known_regs:
        context_hint = f"\\n\\nThis pilot has previously flown: {', '.join(known_regs)}. Use these as reference when unsure about a registration."

    content_parts.append({"type": "text", "text": f"""These are pages from a pilot logbook. Extract all flight entries carefully.

IMPORTANT:
- Dates are DD/MM/YY or DD/MM/YYYY. Year 25 = 2025, 26 = 2026.
- Aircraft registrations: OY-XXX (Denmark), LN-XXX (Norway), N12345 (USA). Read carefully.
- Times are H:MM format. Space between hours and minutes is common.
- Only extract rows with actual flight data.{context_hint}

Respond ONLY with a JSON array:
[{{
  "flight_date": "DD/MM/YYYY",
  "dep_place": "ICAO code",
  "arr_place": "ICAO code",
  "off_block": "HH:MM or null",
  "on_block": "HH:MM or null",
  "aircraft_type": "type as written",
  "registration": "e.g. OY-BJM",
  "pilot_in_command": "name or null",
  "total_time": "H:MM",
  "night_time": "H:MM or null",
  "sep_vfr": "H:MM or null",
  "dual": "H:MM or null",
  "landings_day": number or null,
  "landings_night": number or null,
  "remarks": "any remarks or null"
}}]"""})'''

if old in content:
    content = content.replace(old, new)
    print("Prompt opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
