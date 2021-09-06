
import os
import logging
from mypy_modules.cli import Command, Option, Flag
from mypy_modules.register import register
from .add_cmd.add import get_add_cmd, add
from .activate_cmd.activate import activate, get_activate_cmd
from .list_cmd.list import list_, get_list_cmd
from .rm_cmd.rm import get_rm_cmd, rm

def get_venvm_cmd() -> Command:
    msg = """
    Allows to manage python virtual enviroments
    """
    venvm = Command(
        'venvm', description=msg, 
        mandatory_nested_cmd=True
    )
    # +++++++++++++++++++++++++
    add_cmd = get_add_cmd()
    venvm.nest_cmd(add_cmd)
    # +++++++++++++++++++++++++
    activate_cmd = get_activate_cmd()
    venvm.nest_cmd(activate_cmd)
    # +++++++++++++++++++++++++
    list_cmd = get_list_cmd()
    venvm.nest_cmd(list_cmd)
    # +++++++++++++++++++++++++
    rm_cmd = get_rm_cmd()
    venvm.nest_cmd(rm_cmd)
    
    return venvm

venvm_logger = logging.getLogger(__name__)
def venvm(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    venvs_dir = register.load('venvs_dir')
    if venvs_dir is None:
        valid_dir = False
        while not valid_dir:
            msg = ' + Add the directory where the '
            msg += 'virtual enviroments will be saved'
            print(msg)
            venvs_dir = str(input(" + Directory: "))
            if os.path.exists(venvs_dir):
                valid_dir = True
            else:       
                venvm_logger.error(f" The directory '{venvs_dir}' doesn't exist")
                print()
        register.add('venvs_dir', venvs_dir)
        venvm_logger.info(f" The directory '{venvs_dir}' has been saved")
    openning_msg = f" --- VENVS DIRECTORY: '{venvs_dir}'"
    print(openning_msg)
    print()
    if "add" in nested_cmds:
        cmd_info = nested_cmds.pop("add")
        add(**cmd_info)
    elif "activate" in nested_cmds:
        cmd_info = nested_cmds.pop("activate")
        activate(**cmd_info)
    elif "list" in nested_cmds:
        cmd_info = nested_cmds.pop("list")
        list_(**cmd_info)
    elif "rm" in nested_cmds:
        cmd_info = nested_cmds.pop("rm")
        rm(**cmd_info)
    print()
    print("-"*len(openning_msg))