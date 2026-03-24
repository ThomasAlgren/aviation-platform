#!/bin/bash
mkdir -p instance
python3 build_db.py
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1
