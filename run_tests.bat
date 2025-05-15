@echo off
REM Run pytest to execute all test cases and generate the Allure report
pytest tests/mainscript.py --alluredir="./report"

REM Serve the Allure report
"D:\Users\workspace.user4\Downloads\allure-2.30.0\allure-2.30.0\bin\allure" serve "./report"

REM Open the report folder in File Explorer
explorer .\report
