@echo off
python -m venv env
call "env/Scripts/activate.bat"
pip install --quiet -r requirements.txt
python main.py
pause