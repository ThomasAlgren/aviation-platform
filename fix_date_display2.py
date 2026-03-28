with open('app.py', 'r') as f:
    content = f.read()

old = '                        {{ current_user.medical_valid_until }}'
new = '                        {{ current_user.medical_valid_until[:10] if current_user.medical_valid_until else "" }}'

if old in content:
    content = content.replace(old, new)
    print("Medical dato fix OK!")
else:
    print("IKKE FUNDET")

old2 = '                        {{ current_user.license_valid_until }}'
new2 = '                        {{ current_user.license_valid_until[:10] if current_user.license_valid_until else "" }}'

if old2 in content:
    content = content.replace(old2, new2)
    print("License dato fix OK!")
else:
    print("License IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
