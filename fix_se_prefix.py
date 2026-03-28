with open('app.py', 'r') as f:
    content = f.read()

old = 'if tail and not any(tail.upper().startswith(p) for p in ["OY", "LN", "HB", "VH", "N", "C-", "G-", "D-", "F-", "OE"]):'
new = 'if tail and not any(tail.upper().startswith(p) for p in ["OY", "LN", "HB", "VH", "SE", "PH", "OO", "EI", "CS", "EC", "I-", "D-", "F-", "G-", "OE", "C-", "N", "ZK", "ZS"]):'

if old in content:
    content = content.replace(old, new)
    print("Præfikser opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
