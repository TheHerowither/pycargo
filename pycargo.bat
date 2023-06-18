@echo off


set operation=%~1
set root=%~2
set name=%~3
set venv=%~4
set lib=
set installlib=

cd %CD%
goto :validate

:help
    echo:
    echo PYcargo, a version of cargo for python
    echo       made by The_Herowither
    echo:
    echo:
    echo ###### HOW TO USE ######
    echo Creating a new project:
    echo    pycargo new 'root folder' 'name of project' '0 or 1, if the project should be made in a venv'
    echo:
    echo    To add librarys, add the --AddLib flag, and put the library in a string
    echo    so for example to add pygame, it would be '--AddLib "pygame"'
    echo:
    echo    In case you want to preinstall the librarys, add the --PreInstall flag
    echo    However, if you are making a venv this flag will do nothing
    echo:
    goto :eof

:validate
    if "%~1"=="?" goto :help

    if "%~1"=="" echo Required field 'operation' at index '1' has not been filled in
    if "%~2"=="" echo Required field 'root' at index '2' has not been filled in
    if "%~3"=="" echo Required field 'name' at index '3' has not been filled in
    if "%~4"=="" echo Required field 'venv' at index '4' has not been filled in & goto :eof
    
    goto :parse
    
:install
    echo Installing librarys
    for %%a in (%lib%) do (
        python -m pip install %%a
        echo Library %%a installed
    )
    set installlib="0"
    goto :end

:end
    set /p p=< batch/path.txt
    echo p
    python main.py %operation% %root% %name% %venv% %lib%
    if %installlib%==1 if %venv%==0 goto :install
    exit \B

:parse
    if "%~5"=="--AddLib" set lib=%lib%%~6 & shift & shift & goto :parse
    if "%~5"=="--PreInstall" set installlib=1 & shift & goto :parse
    goto :end
:eof