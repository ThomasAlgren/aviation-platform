with open('app.py', 'r') as f:
    content = f.read()

old = '''    <script>
        var pages = {left: null, right: null};'''

new = '''    <!-- Edit modal -->
    <div id="edit-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:1000;overflow-y:auto">
        <div style="max-width:500px;margin:40px auto;background:#1a1a2e;border-radius:12px;padding:28px;position:relative">
            <button onclick="document.getElementById('edit-modal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;color:#aaa;font-size:20px;cursor:pointer">✕</button>
            <h3 style="margin-bottom:16px">Edit flight entry</h3>
            <form id="edit-form" method="POST">
                <label style="font-size:12px;color:#666">Date (DD/MM/YYYY)</label>
                <input type="text" name="flight_date" id="edit-date" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white;margin-bottom:10px">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
                    <div>
                        <label style="font-size:12px;color:#666">From</label>
                        <input type="text" name="dep_place" id="edit-dep" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">To</label>
                        <input type="text" name="arr_place" id="edit-arr" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px">
                    <div>
                        <label style="font-size:12px;color:#666">Aircraft type</label>
                        <input type="text" name="aircraft_type" id="edit-type" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">Registration</label>
                        <input type="text" name="registration" id="edit-reg" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:10px">
                    <div>
                        <label style="font-size:12px;color:#666">Total time</label>
                        <input type="text" name="total_time" id="edit-total" placeholder="H:MM" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">Dual</label>
                        <input type="text" name="dual" id="edit-dual" placeholder="H:MM" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                    <div>
                        <label style="font-size:12px;color:#666">Landings</label>
                        <input type="number" name="landings_day" id="edit-ldg" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                    </div>
                </div>
                <div style="margin-top:10px">
                    <label style="font-size:12px;color:#666">Remarks</label>
                    <input type="text" name="remarks" id="edit-remarks" style="width:100%;padding:10px;border:1px solid #333;border-radius:8px;background:#0d0d1a;color:white">
                </div>
                <button type="submit" style="background:#ff6b35;color:white;border:none;padding:14px;border-radius:8px;font-size:15px;cursor:pointer;font-weight:600;width:100%;margin-top:16px">Save changes</button>
            </form>
        </div>
    </div>

    <script>
        var pages = {left: null, right: null};'''

if old in content:
    content = content.replace(old, new)
    print("Edit modal tilføjet!")
else:
    print("IKKE FUNDET")

# Tilføj editEntry JavaScript funktion
old2 = '        function scanPages() {'
new2 = '''        function editEntry(id, date, dep, arr, type, reg, total, dual, ldg) {
            document.getElementById('edit-form').action = '/edit-logbook-entry/' + id;
            document.getElementById('edit-date').value = date;
            document.getElementById('edit-dep').value = dep;
            document.getElementById('edit-arr').value = arr;
            document.getElementById('edit-type').value = type;
            document.getElementById('edit-reg').value = reg;
            document.getElementById('edit-total').value = total;
            document.getElementById('edit-dual').value = dual;
            document.getElementById('edit-ldg').value = ldg;
            document.getElementById('edit-modal').style.display = 'block';
        }

        function scanPages() {'''

if old2 in content:
    content = content.replace(old2, new2)
    print("editEntry funktion tilføjet!")
else:
    print("JS IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
