
import os
from mypy_modules.register import register

def list_venvs() -> list:
    v_dir = register.load('venvs_dir')
    venvs = os.listdir(v_dir)
    valid_venvs = []
    for venv in venvs:
        dirs = os.listdir(v_dir+f"\\{venv}")
        if "Lib" in dirs and "Scripts" in dirs:
            valid_venvs.append(venv)
    return valid_venvs

CALLING_DIR = os.getcwd()
    
def save_calling_dir(sys_argv:list):
    global CALLING_DIR
    if "C:" in sys_argv[0]:
        CALLING_DIR = sys_argv.pop(1)
    return sys_argv

def get_calling_dir():
    return CALLING_DIR