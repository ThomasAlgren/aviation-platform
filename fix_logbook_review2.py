"""
fix_logbook_review2.py — Forbedringer til logbog review flow:
1. Godkendte linjer sendes som kontekst til næste AI-scan
2. Block time max 5 timer — advarsel hvis over
3. Dato-kronologi — advarsel hvis dato er før forrige
4. Preferred aircraft — gemmes og bruges som forslag
"""

with open('app.py', 'r') as f:
    content = f.read()

# ─────────────────────────────────────────────
# FIX 1: Send godkendte linjer som kontekst til AI
# ─────────────────────────────────────────────
old_context = '''            if prev_entries:
                last = prev_entries[0]
                context += f"\\nLast approved entry: {last.flight_date}, {last.registration}, {last.total_time}"'''

new_context = '''            if prev_entries:
                last = prev_entries[0]
                context += f"\\nLast database entry: {last.flight_date}, {last.registration}, {last.total_time}"

            # Tilføj godkendte linjer fra denne session som kontekst
            approved = session.get('review_approved', [])
            if approved:
                context += f"\\nAlready approved in this session ({len(approved)} flights):"
                for a in approved[-3:]:  # Kun de 3 seneste
                    context += f"\\n  - {a.get('flight_date','?')} {a.get('registration','?')} {a.get('dep_place','?')}->{a.get('arr_place','?')} total={a.get('total_time','?')}"
                last_approved = approved[-1]
                context += f"\\nNext date must be >= {last_approved.get('flight_date','?')}. Registration is likely {last_approved.get('registration','?')} unless changed."'''

if old_context in content:
    content = content.replace(old_context, new_context)
    print("Fix 1 OK: Kontekst fra godkendte linjer")
else:
    print("Fix 1 FEJL: Kontekst ikke fundet")

# ─────────────────────────────────────────────
# FIX 2: Returner last_approved_date til frontend
# ─────────────────────────────────────────────
old_return_first = '''            return json.dumps({'ok': True, 'total': len(flights), 'first': flights[0] if flights else None})'''

new_return_first = '''            # Find sidst godkendte dato til kronologi-tjek i frontend
            last_date = None
            if approved:
                last_date = approved[-1].get('flight_date')
            elif prev_entries:
                last_date = prev_entries[0].flight_date

            return json.dumps({'ok': True, 'total': len(flights), 'first': flights[0] if flights else None, 'last_approved_date': last_date})'''

if old_return_first in content:
    content = content.replace(old_return_first, new_return_first)
    print("Fix 2 OK: last_approved_date returneres")
else:
    print("Fix 2 FEJL: return first ikke fundet")

# ─────────────────────────────────────────────
# FIX 3: Returner last_approved_date ved approve også
# ─────────────────────────────────────────────
old_return_next = '''            if index < len(flights):
                return json.dumps({'ok': True, 'done': False, 'next': flights[index], 'index': index, 'total': len(flights)})'''

new_return_next = '''            if index < len(flights):
                return json.dumps({'ok': True, 'done': False, 'next': flights[index], 'index': index, 'total': len(flights), 'last_approved_date': flight_data.get('flight_date')})'''

if old_return_next in content:
    content = content.replace(old_return_next, new_return_next)
    print("Fix 3 OK: last_approved_date ved approve")
else:
    print("Fix 3 FEJL: return next ikke fundet")

# ─────────────────────────────────────────────
# FIX 4: Frontend — block time max 5 timer + dato-kronologi
# ─────────────────────────────────────────────
old_vars = '''        var imageData = null;
        var currentFlight = null;
        var currentIndex = 0;
        var totalFlights = 0;'''

new_vars = '''        var imageData = null;
        var currentFlight = null;
        var currentIndex = 0;
        var totalFlights = 0;
        var lastApprovedDate = null;  // Til dato-kronologi tjek'''

if old_vars in content:
    content = content.replace(old_vars, new_vars)
    print("Fix 4a OK: lastApprovedDate variabel")
else:
    print("Fix 4a FEJL: vars ikke fundet")

# Gem last_approved_date fra scan-respons
old_then_first = '''            .then(result => {
                if (result.ok) {
                    totalFlights = result.total;
                    currentIndex = 0;
                    showFlight(result.first, 0, totalFlights);
                }
            });'''

new_then_first = '''            .then(result => {
                if (result.ok) {
                    totalFlights = result.total;
                    currentIndex = 0;
                    if (result.last_approved_date) lastApprovedDate = result.last_approved_date;
                    showFlight(result.first, 0, totalFlights);
                }
            });'''

if old_then_first in content:
    content = content.replace(old_then_first, new_then_first)
    print("Fix 4b OK: gem last_approved_date fra scan")
else:
    print("Fix 4b FEJL: then first ikke fundet")

# Gem last_approved_date fra approve-respons
old_then_approve = '''                } else {
                    showFlight(result.next, result.index, result.total);
                }
            });
        }

        function skipFlight()'''

new_then_approve = '''                } else {
                    if (result.last_approved_date) lastApprovedDate = result.last_approved_date;
                    showFlight(result.next, result.index, result.total);
                }
            });
        }

        function skipFlight()'''

if old_then_approve in content:
    content = content.replace(old_then_approve, new_then_approve)
    print("Fix 4c OK: gem last_approved_date fra approve")
else:
    print("Fix 4c FEJL: then approve ikke fundet")

# ─────────────────────────────────────────────
# FIX 5: validateTime — tilføj max 5 timer + dato-kronologi
# ─────────────────────────────────────────────
old_validate = '''        function validateTime() {
            var off = document.getElementById("f-off").value;
            var on = document.getElementById("f-on").value;
            var total = document.getElementById("f-total").value;
            
            if (off && on && total) {
                var offParts = off.split(":");
                var onParts = on.split(":");
                if (offParts.length == 2 && onParts.length == 2) {
                    var offMin = parseInt(offParts[0]) * 60 + parseInt(offParts[1]);
                    var onMin = parseInt(onParts[0]) * 60 + parseInt(onParts[1]);
                    var diffMin = onMin - offMin;
                    if (diffMin < 0) diffMin += 24 * 60;
                    var calcH = Math.floor(diffMin / 60);
                    var calcM = diffMin % 60;
                    var calcStr = calcH + ":" + (calcM < 10 ? "0" : "") + calcM;
                    
                    document.getElementById("f-total").value = calcStr;
                    document.getElementById("time-warning").style.display = 
                        (calcStr !== total) ? "block" : "none";
                }
            }
        }'''

new_validate = '''        function validateTime() {
            var off = document.getElementById("f-off").value;
            var on = document.getElementById("f-on").value;
            var total = document.getElementById("f-total").value;
            var warnings = [];

            if (off && on) {
                // Normaliser HHMM -> HH:MM
                if (off.length == 4 && !off.includes(":")) off = off.slice(0,2) + ":" + off.slice(2);
                if (on.length == 4 && !on.includes(":")) on = on.slice(0,2) + ":" + on.slice(2);
                document.getElementById("f-off").value = off;
                document.getElementById("f-on").value = on;

                var offParts = off.split(":");
                var onParts = on.split(":");
                if (offParts.length == 2 && onParts.length == 2) {
                    var offMin = parseInt(offParts[0]) * 60 + parseInt(offParts[1]);
                    var onMin = parseInt(onParts[0]) * 60 + parseInt(onParts[1]);
                    var diffMin = onMin - offMin;
                    if (diffMin < 0) diffMin += 24 * 60;
                    var calcH = Math.floor(diffMin / 60);
                    var calcM = diffMin % 60;
                    var calcStr = calcH + ":" + (calcM < 10 ? "0" : "") + calcM;
                    document.getElementById("f-total").value = calcStr;

                    // Max 5 timer
                    if (diffMin > 300) {
                        warnings.push("⚠ Block time er " + calcStr + " — over 5 timer. Er det korrekt?");
                    }
                }
            }

            // Dato-kronologi tjek
            var dateVal = document.getElementById("f-date").value;
            if (dateVal && lastApprovedDate) {
                var parseDMY = function(s) {
                    var p = s.split("/");
                    if (p.length == 3) return new Date(parseInt(p[2]), parseInt(p[1])-1, parseInt(p[0]));
                    return null;
                };
                var d1 = parseDMY(lastApprovedDate);
                var d2 = parseDMY(dateVal);
                if (d1 && d2 && d2 < d1) {
                    warnings.push("⚠ Dato " + dateVal + " er før forrige godkendte dato " + lastApprovedDate);
                }
            }

            var warnEl = document.getElementById("time-warning");
            if (warnings.length > 0) {
                warnEl.innerHTML = warnings.join("<br>");
                warnEl.style.display = "block";
            } else {
                warnEl.style.display = "none";
            }
        }'''

if old_validate in content:
    content = content.replace(old_validate, new_validate)
    print("Fix 5 OK: validateTime med max 5t + kronologi")
else:
    print("Fix 5 FEJL: validateTime ikke fundet")

# ─────────────────────────────────────────────
# Gem
# ─────────────────────────────────────────────
with open('app.py', 'w') as f:
    f.write(content)

print("\nFaerdig! Kør: git add app.py && git commit -m 'Logbog review: kontekst, max 5t, dato-kronologi' && git push")
