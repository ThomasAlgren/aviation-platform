with open('app.py', 'r') as f:
    content = f.read()

old = '''    </div>
</body>
</html>"""

# Email verificering og password reset'''

new = '''    <!-- Certificate modal -->
    <div id="cert-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:1000;overflow-y:auto">
        <div style="max-width:500px;margin:40px auto;background:#1a1a2e;border-radius:12px;padding:28px;position:relative">
            <button onclick="document.getElementById('cert-modal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;color:#aaa;font-size:20px;cursor:pointer">✕</button>
            <h3 id="modal-type" style="margin-bottom:16px;font-size:18px"></h3>
            <div id="modal-details" style="color:#aaa;font-size:14px;margin-bottom:16px"></div>
            <img id="modal-img" style="width:100%;border-radius:8px;display:none">
        </div>
    </div>

    <script>
    function showCert(id) {
        fetch('/certificate/' + id)
            .then(r => r.json())
            .then(cert => {
                document.getElementById('modal-type').textContent = cert.cert_type;
                var details = '';
                if (cert.cert_number) details += '<div>Number: ' + cert.cert_number + '</div>';
                if (cert.issued_by) details += '<div>Issued by: ' + cert.issued_by + '</div>';
                if (cert.issued_date) details += '<div>Issue date: ' + cert.issued_date + '</div>';
                if (cert.valid_until) details += '<div>Valid until: <strong style="color:#ff6b35">' + cert.valid_until + '</strong></div>';
                document.getElementById('modal-details').innerHTML = details;
                if (cert.document) {
                    document.getElementById('modal-img').src = 'data:image/jpeg;base64,' + cert.document;
                    document.getElementById('modal-img').style.display = 'block';
                } else {
                    document.getElementById('modal-img').style.display = 'none';
                }
                document.getElementById('cert-modal').style.display = 'block';
            });
    }
    </script>
    </div>
</body>
</html>"""

# Email verificering og password reset'''

if old in content:
    content = content.replace(old, new)
    print("Modal tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
