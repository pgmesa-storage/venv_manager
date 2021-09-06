@echo off

set calling_dir=%cd%
cd "C:\Users\pablo\Desktop\Pablo\Proyectos Python\venv_manager"
python main.py "%calling_dir%" %* 
cd %calling_dir%


