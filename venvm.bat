@echo off

@REM Checkeamos que python, pip y virtualenv estan instalados
@REM Ver si python esta instalado
call python --version > nul
if '%errorlevel%' NEQ '0' (
    echo ERROR: Python is not installed, please install it before continuing
    exit /B 1
)
@REM Ver si pip esta instalado
call pip --version > nul

if '%errorlevel%' NEQ '0' (
    echo ERROR: Python package module 'pip' is not installed, please install it before continuing
    exit /B 1
)

@REM  Ver si virtualenv esta instalado y si no lo instalamos
call pip show virtualenv > nul
if '%errorlevel%' NEQ '0' (
    echo Instalando virtualenv...
    call pip install virtualenv > nul
)

set calling_dir=%cd%
cd "C:\Users\pablo\Desktop\Pablo\Proyectos Python\venv_manager"
python main.py %*

if "%1" == "activate" (
    @REM FOR /F "tokens=*" %%a in ("python main.py __dir__") do SET v_dir=%%a
    @REM Otra forma de guardar la salida de un programa en una variable
    python main.py __dir__ > result
    set /p v_dir=<result
    del result
    echo %v_dir%
    cd %v_dir%"\%2\Scripts" nul 2>&1
    call activate > nul 2>&1
)

cd %calling_dir%


