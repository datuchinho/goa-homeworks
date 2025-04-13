@echo off
setlocal enabledelayedexpansion

for /D %%f in (Day*) do (
    set "folder=%%~nxf"
    set "name=%%~nxf"
    
    rem Extract number after "Day"
    set "num=!name:Day=!"

    rem Pad the number to 3 digits
    set /a padded=1000 + !num!
    set "newnum=!padded:~1!"

    ren "%%f" "day!newnum!"
    echo Renamed %%f → day!newnum!
)

pause
