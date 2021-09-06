
from mypy_modules.cli import Command, Option, Flag

def get_list_cmd() -> Command:
    msg = """
    lists the virtual enviroment created by the program
    """
    list_ = Command(
        'list', description=msg
    )
    
    return list_

def list_(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    ...