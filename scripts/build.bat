@echo off


set project=%1
set path=%2

:build
    cd %path%
    mkdir build
    mkdir zippable
    robocopy ./resources zippable /E
    pyinstaller --onefile --workpath build --specpath %path% --distpath zippable --name project --add-data "./resources/lib/lib_%project%" main.py

