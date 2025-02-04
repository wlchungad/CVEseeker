@echo off
REM python -m ensurepip
REM python -m pip install --upgrade --quiet pip 
python -m venv env
call "env/Scripts/activate.bat"
pip install --quiet -r requirements.txt
python main.py
pause