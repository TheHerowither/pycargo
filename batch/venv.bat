@echo off


set "root=%~1"
set "name=%~2"
cd %root%

goto :create

:create
    echo Creating venv in %root%/%name%
    python -m venv %name%

    echo Virtual environment created
    echo To activate the venv, please start the activate_venv.bat file in '%root%'
