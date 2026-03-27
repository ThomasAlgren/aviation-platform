with open('app.py', 'r') as f:
    content = f.read()

# Fix alle dropdown menuer der mangler My profile
old1 = '<a href="/my-aircraft">My aircraft</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a>'
new1 = '<a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a>'

count = content.count(old1)
content = content.replace(old1, new1)
print(f"Fixed {count} dropdowns!")

with open('app.py', 'w') as f:
    f.write(content)
