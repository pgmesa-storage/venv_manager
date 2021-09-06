
import os
import logging
from subprocess import run, PIPE, Popen
from mypy_modules.register import register
from mypy_modules.cli import Command, Option, Flag
from commands.reused_funcs import list_venvs

def get_add_cmd() -> Command:
    msg = """
    <venv_name> adds a new virtual environment
    """
    add = Command(
        'add', description=msg,
        extra_arg=True, mandatory=True
    )
    
    return add

add_logger = logging.getLogger(__name__)
def add(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    v_dir = register.load('venvs_dir')
    name = args[0]
    if name in list_venvs():
        add_logger.error(f" Ya existe un entorno virtual con el nombre '{name}'")
        return
    if name in os.listdir(v_dir):
        msg = f" Ya existe una carpeta con el nombre '{name}' en el "
        msg += "directorio de entrornos virtuales"
        add_logger.error(msg)
        return
    process = run(f'python -m virtualenv {name}', stdout=PIPE, shell=True, cwd=v_dir)
    if process.returncode != 0:
        add_logger.error(f" Error al crear el entorno virtual '{name}'")
    else:
        add_logger.info(f" Entorno virtual '{name}' creado con exito")
