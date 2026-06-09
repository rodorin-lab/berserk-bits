@echo off
setlocal

set /p "OLD_SUB=Enter the substring to replace in the filenames: "
set /p "NEW_SUB=Enter the new substring: "

echo.
echo Running the rename script with:
echo   Old substring: "%OLD_SUB%"
echo   New substring: "%NEW_SUB%"
echo.

python rename_jsons.py "%OLD_SUB%" "%NEW_SUB%"

pause
