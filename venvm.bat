@echo off

set calling_dir=%cd%
cd "C:\Users\pablo\Desktop\Pablo\Proyectos Python\venv_manager"
python main.py %*
cd %calling_dir%


