with open('app.py', 'r') as f:
    content = f.read()

# Tilføj My logbook til alle dropdown menuer
old = '<a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a>'
new = '<a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-logbook">My logbook</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a>'

count = content.count(old)
content = content.replace(old, new)
print(f"Fixed {count} menuer!")

with open('app.py', 'w') as f:
    f.write(content)
