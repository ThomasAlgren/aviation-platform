with open('app.py', 'r') as f:
    content = f.read()

old = '''def run_daily_backup():
    try:'''

new = '''def run_daily_notifications():
    try:
        from notifications import check_and_notify
        check_and_notify(app, db, User, ClaimedAircraft, PilotCertificate)
    except Exception as e:
        print(f"Notification fejl: {e}")

def run_daily_backup():
    try:'''

if old in content:
    content = content.replace(old, new)
    print("Notifications funktion tilføjet!")
else:
    print("IKKE FUNDET")

old2 = "scheduler.add_job(run_daily_backup, 'cron', hour=2, minute=0)"
new2 = "scheduler.add_job(run_daily_backup, 'cron', hour=2, minute=0)\nscheduler.add_job(run_daily_notifications, 'cron', hour=2, minute=30)"

if old2 in content:
    content = content.replace(old2, new2)
    print("Scheduler tilføjet!")
else:
    print("Scheduler IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
