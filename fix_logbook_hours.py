with open('app.py', 'r') as f:
    content = f.read()

old = '''    # Beregn total timer
    total_minutes = 0
    for e in entries:
        if e.total_time:
            try:
                parts = e.total_time.replace(":", " ").split()
                if len(parts) == 2:
                    total_minutes += int(parts[0]) * 60 + int(parts[1])
            except:
                pass
    total_hours = total_minutes // 60
    total_mins = total_minutes % 60
    total_str = f"{total_hours}:{total_mins:02d}"'''

new = '''    # Beregn total timer
    total_minutes = 0
    for e in entries:
        if e.total_time and e.total_time not in ['—', '-', '']:
            try:
                parts = e.total_time.replace(":", " ").replace(".", " ").split()
                if len(parts) == 2:
                    total_minutes += int(parts[0]) * 60 + int(parts[1])
            except:
                pass
    total_hours = total_minutes // 60
    total_mins = total_minutes % 60
    total_str = f"{total_hours}:{total_mins:02d}" if total_minutes > 0 else "0:00"'''

if old in content:
    content = content.replace(old, new)
    print("Total timer fix OK!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
