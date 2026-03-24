#!/bin/bash
mkdir -p instance
python3 build_db.py
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1
```

Gem med `Ctrl+X` → `Y` → Enter.

Derefter:
```
git add start.sh
git commit -m "Fix: wait for db before starting gunicorn"
git push
```

**Men** — `build_db.py` bygger en 152MB database. Det tager tid. Render har en **15 minutters timeout** på deploy. Kan du fortælle mig hvad der er i `build_db.py`?

Skriv:
```
cat build_db.py
#!/bin/bash
mkdir -p instance
python3 build_db.py
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1
