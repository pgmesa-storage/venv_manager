
from mypy_modules.cli import Command, Option, Flag

def get_clear_cmd() -> Command:
    msg = """
    removes all virtual environments
    """
    clear = Command(
        'clear', description=msg
    )
    
    return clear

def clear(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    ...