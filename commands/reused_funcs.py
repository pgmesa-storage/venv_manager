
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