with open('app.py', 'r') as f:
    content = f.read()

old = '''                <tr>
                    <td>{{ e.flight_date or '—' }}</td>
                    <td>{{ e.dep_place or '—' }}</td>
                    <td>{{ e.arr_place or '—' }}</td>
                    <td>{{ e.aircraft_type or '—' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or '—' }}</td>
                    <td>{{ e.total_time or '—' }}</td>
                    <td>{{ e.dual or '—' }}</td>
                    <td>{{ e.landings_day or '—' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="return confirm(\'Delete?\')">✕</a></td>
                </tr>'''

new = '''                <tr onclick="editEntry({{ e.id }}, '{{ e.flight_date or '' }}', '{{ e.dep_place or '' }}', '{{ e.arr_place or '' }}', '{{ e.aircraft_type or '' }}', '{{ e.registration or '' }}', '{{ e.total_time or '' }}', '{{ e.dual or '' }}', '{{ e.landings_day or '' }}')" style="cursor:pointer">
                    <td>{{ e.flight_date or '—' }}</td>
                    <td>{{ e.dep_place or '—' }}</td>
                    <td>{{ e.arr_place or '—' }}</td>
                    <td>{{ e.aircraft_type or '—' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or '—' }}</td>
                    <td>{{ e.total_time or '—' }}</td>
                    <td>{{ e.dual or '—' }}</td>
                    <td>{{ e.landings_day or '—' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="event.stopPropagation();return confirm(\'Delete?\')">✕</a></td>
                </tr>'''

if old in content:
    content = content.replace(old, new)
    print("Edit klik tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
