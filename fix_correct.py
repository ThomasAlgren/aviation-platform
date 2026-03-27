with open('app.py', 'r') as f:
    content = f.read()

old = '''        <!-- Actions -->
        <div class="card">
            <h3>Actions</h3>
            <a href="/upload-arc/{{ aircraft.tail }}" class="action-btn">Upload & verify ARC with AI <span>→</span></a>
            <a href="/parts?q={{ aircraft.manufacturer }}" class="action-btn">Find parts for {{ aircraft.manufacturer }} {{ aircraft.model }} <span>→</span></a>
            <a href="/sell-aircraft/{{ aircraft.tail }}" class="action-btn">List this aircraft for sale <span>→</span></a>
        </div>'''

new = '''        <!-- Ret flydata -->
        <div class="card">
            <h3>Correct aircraft data
                <button class="edit-btn" onclick="document.getElementById(\'correct-form\').classList.toggle(\'hidden\')">Edit</button>
            </h3>
            <div class="date-item">
                <span class="date-label">Manufacturer</span>
                <span class="date-value">{{ aircraft.manufacturer or \'—\' }}</span>
            </div>
            <div class="date-item">
                <span class="date-label">Model</span>
                <span class="date-value">{{ aircraft.model or \'—\' }}</span>
            </div>
            <div class="date-item">
                <span class="date-label">Year</span>
                <span class="date-value">{{ aircraft.year or \'—\' }}</span>
            </div>
            <div id="correct-form" class="hidden" style="margin-top:16px">
                <p style="color:#666;font-size:13px;margin-bottom:12px">As the owner, you can correct incorrect data in our registry.</p>
                <form method="POST" action="/correct-aircraft/{{ aircraft.tail }}">
                    <input type="text" name="manufacturer" placeholder="Manufacturer (e.g. Cessna)" value="{{ aircraft.manufacturer or \'\' }}">
                    <input type="text" name="model" placeholder="Model (e.g. 172S Skyhawk)" value="{{ aircraft.model or \'\' }}">
                    <input type="text" name="year" placeholder="Year built" value="{{ aircraft.year or \'\' }}">
                    <button type="submit" class="save-btn">Save corrections</button>
                </form>
            </div>
        </div>

        <!-- Actions -->
        <div class="card">
            <h3>Actions</h3>
            <a href="/upload-arc/{{ aircraft.tail }}" class="action-btn">Upload & verify ARC with AI <span>→</span></a>
            <a href="/parts?q={{ aircraft.manufacturer }}" class="action-btn">Find parts for {{ aircraft.manufacturer }} {{ aircraft.model }} <span>→</span></a>
            <a href="/sell-aircraft/{{ aircraft.tail }}" class="action-btn">List this aircraft for sale <span>→</span></a>
        </div>'''

if old in content:
    content = content.replace(old, new)
    print("Rettelse formular tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
