with open('app.py', 'r') as f:
    content = f.read()

old = '''                        <select name="cert_type">
                            <option value="">Select type...</option>
                            <option>PPL Theory</option>
                            <option>PPL Licence</option>
                            <option>CPL Licence</option>
                            <option>ATPL Licence</option>
                            <option>Medical Class 1</option>
                            <option>Medical Class 2</option>
                            <option>LAPL Medical</option>
                            <option>Radio Certificate — National</option>
                            <option>Radio Certificate — International (English)</option>
                            <option>Rating — Night VFR</option>
                            <option>Rating — IFR</option>
                            <option>Rating — Tailwheel</option>
                            <option>Rating — Retractable Gear</option>
                            <option>Rating — Multi Engine (MEP)</option>
                            <option>Rating — SEP</option>
                            <option>Other</option>
                        </select>'''

new = '''                        <select name="cert_type">
                            <option value="">Select type...</option>
                            <optgroup label="Licences">
                            <option>LAPL(A) — Light Aircraft Pilot Licence</option>
                            <option>PPL(A) — Private Pilot Licence</option>
                            <option>CPL(A) — Commercial Pilot Licence</option>
                            <option>ATPL(A) — Airline Transport Pilot Licence</option>
                            <option>MPL — Multi-crew Pilot Licence</option>
                            <option>PPL(H) — Helicopter Pilot Licence</option>
                            <option>SPL — Sailplane Pilot Licence</option>
                            <option>BPL — Balloon Pilot Licence</option>
                            <option>FAA PPL</option>
                            <option>FAA CPL</option>
                            <option>FAA ATPL</option>
                            </optgroup>
                            <optgroup label="Theory Exams">
                            <option>PPL Theory — Passed</option>
                            <option>ATPL Theory — Passed (Frozen)</option>
                            </optgroup>
                            <optgroup label="Ratings">
                            <option>IR(A) — Instrument Rating</option>
                            <option>EIR — En-route Instrument Rating</option>
                            <option>Night Rating</option>
                            <option>SEP(land) — Single Engine Piston</option>
                            <option>MEP(land) — Multi Engine Piston</option>
                            <option>TMG — Touring Motor Glider</option>
                            <option>HPA — High Performance Aircraft</option>
                            <option>Tailwheel Endorsement</option>
                            </optgroup>
                            <optgroup label="Medical">
                            <option>Medical Class 1</option>
                            <option>Medical Class 2</option>
                            <option>LAPL Medical</option>
                            </optgroup>
                            <optgroup label="Radio">
                            <option>Radio Certificate — National</option>
                            <option>Radio Certificate — ICAO/International (English)</option>
                            <option>ICAO English Language Proficiency</option>
                            </optgroup>
                            <optgroup label="Instructor">
                            <option>FI(A) — Flight Instructor</option>
                            <option>IRI(A) — Instrument Rating Instructor</option>
                            <option>CRI — Class Rating Instructor</option>
                            </optgroup>
                            <option>Other</option>
                        </select>'''

if old in content:
    content = content.replace(old, new)
    print("Certifikat liste opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
