
from mypy_modules.cli import Command, Option, Flag

def get_rm_cmd() -> Command:
    msg = """
    <venv_name> removes the virtual enviroment specified
    """
    rm = Command(
        'rm', description=msg
    )
    
    return rm

def rm(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    ...