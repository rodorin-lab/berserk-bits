@echo off
setlocal

set /p "OLD_STRING=Enter the string you want to replace (old string): "
set /p "NEW_STRING=Enter the new replacement string: "

echo Running the Python script with:
echo   Old string: "%OLD_STRING%"
echo   New string: "%NEW_STRING%"
python script.py "%OLD_STRING%" "%NEW_STRING%"

pause
