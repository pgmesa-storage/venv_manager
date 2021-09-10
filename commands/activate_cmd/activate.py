
import logging
from subprocess import CalledProcessError, call, run, PIPE, Popen
from mypy_modules.cli import Command, Option, Flag
from mypy_modules.register import register
from commands.reused_funcs import list_venvs

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
    if venv_name in list_venvs():
        activate_logger.info(f" Activating virtual env '{venv_name}'...")
        # The virtual env will be activated by the batch file     
    else:
        activate_logger.error(f" The virtual env '{venv_name}' doesn't exist")
        