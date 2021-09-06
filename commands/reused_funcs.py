
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
    
