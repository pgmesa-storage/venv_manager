
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

        
        
# class BatchFileError(Exception):
#     pass

# def catch_error(func):
#     def _catch_error(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as err:
#             raise BatchFileError(err)
#     return _catch_error

# class BatchFile():
#     @catch_error
#     def __init__(self, name:str, location=None):
#         if '.bat' not in name:
#             raise BatchFileError("The name must end with .bat")
#         self.name = name
#         if location is not None:
#             if '/' in location and not location.endswith('/'):
#                 location += '/'
#             elif '\\' in location and not location.endswith('\\'):
#                 location += '\\'
#         else:
#             location = ''
#         self.location = location
#         self.path = location+name
#         with open(self.path, 'w') as file:
#             comment = f"@REM ----- {name.upper()} -----"
#             file.write("@echo off\n\n" + comment)
            
#     @catch_error
#     def append(self, script:str):
#         with open(self.path, 'a') as file:
#             file.write(script)
            
#     @catch_error
#     def override(self, script:str):
#         with open(self.path, 'w') as file:
#             file.write(script)
    