with open('app.py', 'r') as f:
    content = f.read()

old = '''                <tr>
                    <th>Date</th>
                    <th>From</th>
                    <th>To</th>
                    <th>Aircraft</th>
                    <th>Reg</th>
                    <th>Total</th>
                    <th>Dual</th>
                    <th>Ldg</th>
                    <th></th>
                </tr>
                {% for e in entries %}
                <tr onclick="editEntry({{ e.id }}, \'{{ e.flight_date or \'\' }}\', \'{{ e.dep_place or \'\' }}\', \'{{ e.arr_place or \'\' }}\', \'{{ e.aircraft_type or \'\' }}\', \'{{ e.registration or \'\' }}\', \'{{ e.total_time or \'\' }}\', \'{{ e.dual or \'\' }}\', \'{{ e.landings_day or \'\' }}\')" style="cursor:pointer">
                    <td>{{ e.flight_date or \'—\' }}</td>
                    <td>{{ e.dep_place or \'—\' }}</td>
                    <td>{{ e.arr_place or \'—\' }}</td>
                    <td>{{ e.aircraft_type or \'—\' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or \'—\' }}</td>
                    <td>{{ e.total_time or \'—\' }}</td>
                    <td>{{ e.dual or \'—\' }}</td>
                    <td>{{ e.landings_day or \'—\' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="event.stopPropagation();return confirm(\'Delete?\')">✕</a></td>
                </tr>
                {% endfor %}'''

new = '''                <tr>
                    <th>Date</th>
                    <th>From</th>
                    <th>To</th>
                    <th class="desktop-col">Off</th>
                    <th class="desktop-col">On</th>
                    <th class="desktop-col">Type</th>
                    <th>Reg</th>
                    <th>Total</th>
                    <th class="desktop-col">Night</th>
                    <th class="desktop-col">SEP VFR</th>
                    <th class="desktop-col">SEP IFR</th>
                    <th class="desktop-col">MEP VFR</th>
                    <th class="desktop-col">MEP IFR</th>
                    <th class="desktop-col">PIC</th>
                    <th class="desktop-col">Dual</th>
                    <th class="desktop-col">FI</th>
                    <th>Ldg D</th>
                    <th class="desktop-col">Ldg N</th>
                    <th class="desktop-col">Remarks</th>
                    <th></th>
                </tr>
                {% for e in entries %}
                <tr onclick="editEntry({{ e.id }}, \'{{ e.flight_date or \'\' }}\', \'{{ e.dep_place or \'\' }}\', \'{{ e.arr_place or \'\' }}\', \'{{ e.aircraft_type or \'\' }}\', \'{{ e.registration or \'\' }}\', \'{{ e.total_time or \'\' }}\', \'{{ e.dual or \'\' }}\', \'{{ e.landings_day or \'\' }}\')">
                    <td>{{ e.flight_date or \'—\' }}</td>
                    <td>{{ e.dep_place or \'—\' }}</td>
                    <td>{{ e.arr_place or \'—\' }}</td>
                    <td class="desktop-col">{{ e.off_block or \'—\' }}</td>
                    <td class="desktop-col">{{ e.on_block or \'—\' }}</td>
                    <td class="desktop-col">{{ e.aircraft_type or \'—\' }}</td>
                    <td style="color:#ff6b35">{{ e.registration or \'—\' }}</td>
                    <td>{{ e.total_time or \'—\' }}</td>
                    <td class="desktop-col">{{ e.night_time or \'—\' }}</td>
                    <td class="desktop-col">{{ e.sep_vfr or \'—\' }}</td>
                    <td class="desktop-col">{{ e.sep_ifr or \'—\' }}</td>
                    <td class="desktop-col">{{ e.mep_vfr or \'—\' }}</td>
                    <td class="desktop-col">{{ e.mep_ifr or \'—\' }}</td>
                    <td class="desktop-col">{{ e.pic_time or \'—\' }}</td>
                    <td class="desktop-col">{{ e.dual or \'—\' }}</td>
                    <td class="desktop-col">{{ e.instructor_time or \'—\' }}</td>
                    <td>{{ e.landings_day or \'—\' }}</td>
                    <td class="desktop-col">{{ e.landings_night or \'—\' }}</td>
                    <td class="desktop-col" style="color:#666;font-size:12px">{{ e.remarks or \'\' }}</td>
                    <td><a href="/delete-logbook-entry/{{ e.id }}" class="delete-btn" onclick="event.stopPropagation();return confirm(\'Delete?\')">✕</a></td>
                </tr>
                {% endfor %}'''

if old in content:
    content = content.replace(old, new)
    print("Tabel opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
