
import os
import logging
from subprocess import CalledProcessError, Popen, run, PIPE
from mypy_modules.register import register
from mypy_modules.cli import Command, Option, Flag
from commands.reused_funcs import list_venvs

def get_rm_cmd() -> Command:
    msg = """
    <venv_name> removes the virtual environment specified
    """
    rm = Command(
        'rm', description=msg,
        extra_arg=True, mandatory=True
    )
    rm.add_flag(Flag(
        '-y', description="doesn't ask for confirmation"
    ))
    
    return rm

rm_logger = logging.getLogger(__name__)
def rm(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    v_dir = register.load('venvs_dir')
    name = args[0]
    if not name in list_venvs():
        rm_logger.error(f" No existe el entorno virtual '{name}'")
        return
    else:
        if "-y" not in flags:
            msg = f" + Are you sure you want to delete '{name}' venv? (y/n): "
            answer = str(input(msg))
            if answer.lower() != "y":
                rm_logger.info(" Operacion cancelada")
                return
        run(
            f'del /f/q/s "{name}" & rmdir /q/s "{name}"', 
            shell=True, check=True, cwd=v_dir, stdout=PIPE
        )
        if not os.path.exists(v_dir+f"\\{name}"):
            rm_logger.info(f" Entorno virtual '{name}' eliminado con exito")
        else:
            msg = f" '{name}' no se han podido eliminar por completo"
            msg += "\n    -> Revisa que no este siendo usado en otro proceso"
            rm_logger.error(msg)
        