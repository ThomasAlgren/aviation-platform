with open('app.py', 'r') as f:
    content = f.read()

# Tilføj foto upload til formularen
old = '''                        <label>Valid until (leave blank if no expiry)</label>
                        <input type="text" name="valid_until" placeholder="YYYY-MM-DD">
                        <button type="submit" class="save-btn">Add certificate</button>
                    </form>'''

new = '''                        <label>Valid until (leave blank if no expiry)</label>
                        <input type="text" name="valid_until" placeholder="YYYY-MM-DD">
                        <label>Upload certificate photo (optional — AI will read dates automatically)</label>
                        <input type="file" id="cert-photo" accept="image/*" onchange="loadCertPhoto(this)" style="margin-bottom:10px">
                        <input type="hidden" name="document" id="cert-doc-data">
                        <img id="cert-preview" style="max-width:100%;border-radius:8px;margin-bottom:10px;display:none">
                        <button type="submit" class="save-btn">Add certificate</button>
                    </form>
                    <script>
                    function loadCertPhoto(input) {
                        var file = input.files[0];
                        if (!file) return;
                        var reader = new FileReader();
                        reader.onload = function(e) {
                            document.getElementById("cert-preview").src = e.target.result;
                            document.getElementById("cert-preview").style.display = "block";
                            document.getElementById("cert-doc-data").value = e.target.result.split(",")[1];
                        };
                        reader.readAsDataURL(file);
                    }
                    </script>'''

if old in content:
    content = content.replace(old, new)
    print("Foto upload tilføjet!")
else:
    print("IKKE FUNDET")

# Opdater add_certificate route til AI analyse
old2 = '''@app.route('/add-certificate', methods=['POST'])
@login_required
def add_certificate():
    cert_type = request.form.get('cert_type', '').strip()
    if not cert_type:
        return redirect('/my-profile')
    
    cert = PilotCertificate(
        user_id=current_user.id,
        cert_type=cert_type,
        cert_number=request.form.get('cert_number', '').strip() or None,
        issued_by=request.form.get('issued_by', '').strip() or None,
        issued_date=request.form.get('issued_date', '').strip() or None,
        valid_until=request.form.get('valid_until', '').strip() or None,
    )
    db.session.add(cert)
    db.session.commit()
    return redirect('/my-profile')'''

new2 = '''@app.route('/add-certificate', methods=['POST'])
@login_required
def add_certificate():
    cert_type = request.form.get('cert_type', '').strip()
    if not cert_type:
        return redirect('/my-profile')
    
    cert_number = request.form.get('cert_number', '').strip() or None
    issued_by = request.form.get('issued_by', '').strip() or None
    issued_date = request.form.get('issued_date', '').strip() or None
    valid_until = request.form.get('valid_until', '').strip() or None
    document = request.form.get('document', '').strip() or None

    # AI analyse hvis foto uploaded
    if document and not valid_until:
        try:
            import anthropic as ac
            import json
            client = ac.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=300,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": document}},
                        {"type": "text", "text": """Analyze this pilot certificate/licence image. Extract:
Respond ONLY with JSON:
{
  "cert_number": "certificate number or null",
  "issued_by": "issuing authority or null",
  "issued_date": "YYYY-MM-DD or null",
  "valid_until": "YYYY-MM-DD or null"
}"""}
                    ]
                }]
            )
            text = response.content[0].text
            clean = text.replace("```json", "").replace("```", "").strip()
            result = json.loads(clean)
            cert_number = cert_number or result.get("cert_number")
            issued_by = issued_by or result.get("issued_by")
            issued_date = issued_date or result.get("issued_date")
            valid_until = valid_until or result.get("valid_until")
        except Exception as e:
            print("AI fejl:", e)

    cert = PilotCertificate(
        user_id=current_user.id,
        cert_type=cert_type,
        cert_number=cert_number,
        issued_by=issued_by,
        issued_date=issued_date,
        valid_until=valid_until,
        document=document[:500] if document else None,
    )
    db.session.add(cert)
    db.session.commit()
    return redirect('/my-profile')'''

if old2 in content:
    content = content.replace(old2, new2)
    print("AI analyse tilføjet!")
else:
    print("Route IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
