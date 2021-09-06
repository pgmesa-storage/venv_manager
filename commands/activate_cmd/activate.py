
import logging
from subprocess import run, PIPE, Popen
from mypy_modules.cli import Command, Option, Flag
from mypy_modules.register import register
from commands.reused_funcs import list_venvs

def get_activate_cmd() -> Command:
    msg = """
    <venv_name> activates the virtual enviroment specified
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
        process = run("", shell=True)
    else:
        ...
        