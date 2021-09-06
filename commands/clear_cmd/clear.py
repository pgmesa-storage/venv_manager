
import os
import logging
from mypy_modules.register import register
from mypy_modules.cli import Command, Option, Flag
from subprocess import CalledProcessError, Popen, run, PIPE
from commands.reused_funcs import list_venvs

def get_clear_cmd() -> Command:
    msg = """
    removes all virtual environments
    """
    clear = Command(
        'clear', description=msg
    )
    clear.add_flag(Flag(
        '-y', description="doesn't ask for confirmation"
    ))
    
    return clear

clear_logger = logging.getLogger(__name__)
def clear(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    v_dir = register.load('venvs_dir')
    venvs = list_venvs()
    if len(venvs) != 0:
        if "-y" not in flags:
            msg = f" + Are you sure you want to remove all virtualenvs? (y/n): "
            answer = str(input(msg))
            if answer.lower() != "y":
                clear_logger.info(" Operacion cancelada")
                return
        for venv in venvs:
            run(
                f'del /f/q/s "{venv}" & rmdir /q/s "{venv}"', 
                shell=True, check=True, cwd=v_dir, stdout=PIPE
            )
            if not os.path.exists(v_dir+f"\\{venv}"):
                clear_logger.info(f" Entorno virtual '{venv}' eliminado con exito")
            else:
                msg = f" '{venv}' no se han podido eliminar por completo"
                msg += "\n    -> Revisa que no este siendo usado en otro proceso"
                clear_logger.error(msg)   
    else:
        clear_logger.error(" The are no virtual environments to remove")