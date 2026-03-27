with open('app.py', 'r') as f:
    content = f.read()

# Fix My Listings menu
old1 = '        <div class="nav"><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div>'
new1 = '        <div class="nav"><div class="user-menu"><button class="user-btn" onclick="this.nextElementSibling.classList.toggle(\'open\')">{{ current_user.name }} ▾</button><div class="dropdown"><a href="/my-aircraft">My aircraft</a><a href="/my-profile">My profile</a><a href="/my-logbook">My logbook</a><a href="/my-listings">My listings</a><a href="/logout">Log out</a></div></div></div>'

if old1 in content:
    content = content.replace(old1, new1)
    print("My Listings menu rettet!")
else:
    print("My Listings IKKE FUNDET")

# Fix cockpit template dropdown - mangler My Logbook
old2 = '<a href="/my-aircraft">My aircraft</a>\n                    <a href="/my-profile">My profile</a>\n                    <a href="/my-listings">My listings</a>\n                    <a href="/logout">Log out</a>'
new2 = '<a href="/my-aircraft">My aircraft</a>\n                    <a href="/my-profile">My profile</a>\n                    <a href="/my-logbook">My logbook</a>\n                    <a href="/my-listings">My listings</a>\n                    <a href="/logout">Log out</a>'

if old2 in content:
    content = content.replace(old2, new2)
    print("Cockpit menu rettet!")
else:
    print("Cockpit IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
