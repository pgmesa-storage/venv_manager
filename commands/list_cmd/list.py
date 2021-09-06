
from mypy_modules.cli import Command, Option, Flag
from commands.reused_funcs import list_venvs

def get_list_cmd() -> Command:
    msg = """
    lists the virtual environment created by the program
    """
    list_ = Command(
        'list', description=msg
    )
    
    return list_

def list_(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    venvs = list_venvs()
    print(" + VIRTUAL ENVIRONMENTS:")
    if len(venvs) != 0:
        for venv in venvs:
            print(f"     --> {venv}")
    else:
        print("     --> Empty: There are no virtual environments created")
        