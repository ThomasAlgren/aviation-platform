with open('app.py', 'r') as f:
    content = f.read()

old = '''            .then(result => {
                if (result.ok) {
                    status.textContent = "✓ " + result.saved + " flights saved!";
                    setTimeout(() => location.reload(), 1500);
                } else {
                    status.textContent = "Error: " + (result.error || "Something went wrong");
                    btn.disabled = false;
                    btn.textContent = "Scan with AI";
                }
            })'''

new = '''            .then(result => {
                if (result.ok) {
                    var msg = "✓ " + result.saved + " flights saved!";
                    if (result.validation_warning) {
                        msg += "\\n⚠ " + result.validation_warning;
                        status.style.color = "#ffc107";
                    }
                    if (result.page_totals) {
                        msg += "\\nPage totals: " + JSON.stringify(result.page_totals);
                    }
                    status.textContent = msg;
                    setTimeout(() => location.reload(), 3000);
                } else {
                    status.textContent = "Error: " + (result.error || "Something went wrong");
                    btn.disabled = false;
                    btn.textContent = "Scan with AI";
                }
            })'''

if old in content:
    content = content.replace(old, new)
    print("JS opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
