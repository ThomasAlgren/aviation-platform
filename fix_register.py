with open('app.py', 'r') as f:
    content = f.read()

old = '''                else:
                    user = User(name=name, email=email, country=country)
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect('/')'''

new = '''                else:
                    import secrets
                    token = secrets.token_urlsafe(32)
                    user = User(name=name, email=email, country=country)
                    user.set_password(password)
                    user.verification_token = token
                    user.email_verified = False
                    db.session.add(user)
                    db.session.commit()
                    try:
                        from emails import send_verification_email
                        send_verification_email(email, name, token)
                    except Exception as e:
                        print("Email fejl:", e)
                    login_user(user)
                    return redirect('/?welcome=1')'''

if old in content:
    content = content.replace(old, new)
    print("Register route opdateret!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
