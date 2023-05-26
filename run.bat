@echo off
pip install -r requirements.txt >nul
python -m flask run --host 0.0.0.0
