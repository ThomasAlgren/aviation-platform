with open('app.py', 'r') as f:
    content = f.read()

old = "scheduler.add_job(run_daily_backup, 'cron', hour=2, minute=0)\nscheduler.add_job(run_daily_notifications, 'cron', hour=2, minute=30)"

new = """scheduler.add_job(run_daily_backup, 'cron', hour=2, minute=0)
scheduler.add_job(run_daily_notifications, 'cron', hour=2, minute=30)
scheduler.add_job(run_monthly_updates, 'cron', day=1, hour=3, minute=0)"""

if old in content:
    content = content.replace(old, new)
    print("Scheduler tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
