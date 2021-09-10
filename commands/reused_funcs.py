
import os
from mypy_modules.register import register

def list_venvs() -> list:
    v_dir = register.load('venvs_dir')
    venvs = os.listdir(v_dir)
    valid_venvs = []
    for venv in venvs:
        if not os.path.isdir(v_dir+f"\\{venv}"): continue
        try:
            dirs = os.listdir(v_dir+f"\\{venv}")
            ac_bat_path = v_dir+f"\\{venv}\\Scripts\\activate.bat"
            exist_ac_bat = os.path.exists(ac_bat_path)
            if "Lib" in dirs and "Scripts" in dirs and exist_ac_bat:
                valid_venvs.append(venv)
        except:
            continue
    return valid_venvs

BATCH_NAME = 'shutdown.bat'
BATCH_LOCATION = ''
BATCH_PATH = BATCH_LOCATION+BATCH_NAME

def sdbatch_init():
    with open(BATCH_PATH, 'w') as file:
        comment = f"@REM ----- {BATCH_NAME.upper()} -----\n"
        file.write("@echo off\n\n" + comment)

def sdbatch_append_task(task_script:str, task_name:str):
    task_script = "\nset calling_dir=%cd%" + task_script +'\ncd %calling_dir%\n'
    with open(BATCH_PATH, 'a') as file:
        comment = f'\n@REM {task_name}'
        file.write(comment + task_script)

def sdbatch_override_with(task_script:str, task_name:str):
    sdbatch_init()
    sdbatch_append_task(task_script, task_name)

        
venvm_bat_file = f"""
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
call pip show virtualenv > nul 2>&1
if '%errorlevel%' NEQ '0' (
    echo ERR: Module 'virtualenv' is not installed
    set /p answer="Install 'virtualenv' module? (y/n): "
    if "%answer%" == "y" (
        echo Instalando virtualenv...
        call pip install virtualenv > nul
    ) else ( exit /B 1 )
)

set calling_dir=%cd%
cd "{os.getcwd()}"
python main.py %*

if exist "{os.getcwd()}\shutdown.bat" (
    call shutdown.bat 
    del /f/q/s shutdown.bat > nul 
)

cd %calling_dir%
"""