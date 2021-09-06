
import logging
from subprocess import CalledProcessError, call, run, PIPE, Popen
from mypy_modules.cli import Command, Option, Flag
from mypy_modules.register import register
from commands.reused_funcs import get_calling_dir, list_venvs

def get_activate_cmd() -> Command:
    msg = """
    <venv_name> activates the virtual environment specified in another cmd window
    """
    activate = Command(
        'activate', description=msg,
        extra_arg=True, mandatory=True
    )
    
    return activate

activate_logger = logging.getLogger(__name__)
def activate(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    venv_name = args[0]
    v_dir = register.load('venvs_dir')
    if venv_name in list_venvs():
        try:
            cal_dir = get_calling_dir()
            Popen(
                f'start cmd /k ".\\{venv_name}\\Scripts\\activate & cd "{cal_dir}""', 
                shell=True, cwd=v_dir
            )
        except CalledProcessError as err:
            activate_logger.error(err)
        else:
            activate_logger.info(f" Virtual env '{venv_name}' has been activated")       
    else:
        activate_logger.error(f" The virtual env '{venv_name}' doesn't exist")
        