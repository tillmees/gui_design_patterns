@echo off

:: Activate the virtual environment
call "..\.venv\Scripts\activate.bat"

:: Install requirements via pip
pip install -r requirements.txt

pause