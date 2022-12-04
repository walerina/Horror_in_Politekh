@echo off

call %~dp0BOt\venv\Scripts\activate

cd %~dp0BOt

set TOKEN=5722443886:AAGZ6Wo8tywkMW5vKV65bT0TRqJBcjL-_Vc

python bot_telegramm.py

pause