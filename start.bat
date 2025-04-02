@echo off
setlocal
REM Python environment: pip check and update
python -m ensurepip
python -m pip install --upgrade --quiet pip 

REM Python environment: create a virtual environment
python -m venv env
call "env/Scripts/activate.bat"
pip install --quiet -r requirements.txt

REM Python environment: run the main script
python main.py
REM --------------------------------------------------------

REM Get the current date in YYYY-MM-DD format
set datestr=%date:~10,4%-%date:~4,2%-%date:~7,2%

REM Set the folder path to the output directory
REM The %~dp0 variable contains the path of the batch file (the current directory)
REM The output directory is in the same directory as the batch file
set folderPath=%~dp0output\%datestr%

REM Open the output directory in Windows Explorer
explorer "%folderPath%"

endlocal
REM pause