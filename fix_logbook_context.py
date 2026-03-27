with open('app.py', 'r') as f:
    content = f.read()

old = '''    content_parts = []
    if left_page:
        content_parts.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": left_page}})
    if right_page:
        content_parts.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": right_page}})'''

new = '''    # Hent brugerens tidligere registreringer som kontekst
    prev_entries = LogbookEntry.query.filter_by(user_id=current_user.id).order_by(LogbookEntry.created_at.desc()).limit(20).all()
    known_regs = list(set([e.registration for e in prev_entries if e.registration]))
    known_types = list(set([e.aircraft_type for e in prev_entries if e.aircraft_type]))
    
    content_parts = []
    if left_page:
        content_parts.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": left_page}})
    if right_page:
        content_parts.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": right_page}})'''

if old in content:
    content = content.replace(old, new)
    print("Kontekst tilføjet!")
else:
    print("IKKE FUNDET")

# Opdater prompten til at inkludere kontekst
old2 = '    content_parts.append({"type": "text", "text": """These are pages from a pilot logbook. Extract all flight entries carefully.\n\nIMPORTANT:'
new2 = '    context_hint = ""\n    if known_regs:\n        context_hint = f"\\n\\nThis pilot has previously flown these aircraft: {\', \'.join(known_regs)}. These aircraft types: {\', \'.join(known_types)}. Use these as reference when reading similar registrations - if unsure between two readings, prefer one of these known registrations."\n    content_parts.append({"type": "text", "text": """These are pages from a pilot logbook. Extract all flight entries carefully.\n\nIMPORTANT:'

if old2 in content:
    content = content.replace(old2, new2)
    print("Prompt kontekst tilføjet!")
else:
    print("Prompt IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
