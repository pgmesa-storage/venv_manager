
import os
import logging
from subprocess import Popen
from mypy_modules.cli import Command, Option, Flag
from mypy_modules.register import register
from .add_cmd.add import get_add_cmd, add
from .activate_cmd.activate import activate, get_activate_cmd
from .list_cmd.list import list_, get_list_cmd
from .rm_cmd.rm import get_rm_cmd, rm
from .clear_cmd.clear import get_clear_cmd, clear
from commands.reused_funcs import sdbatch_append_task, sdbatch_init, venvm_bat_file


def get_venvm_cmd() -> Command:
    msg = """
    Allows to manage python virtual environments
    """
    venvm = Command(
        'venvm', description=msg
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
    # +++++++++++++++++++++++++
    clear_cmd = get_clear_cmd()
    venvm.nest_cmd(clear_cmd)
    # -------------------------
    dir_opt = def_dir_opt()
    venvm.add_option(dir_opt)
    # -------------------------
    cd_opt = def_cd_opt()
    venvm.add_option(cd_opt)
    # -------------------------
    reveal_opt = def_reveal_venvs_opt()
    venvm.add_option(reveal_opt)
    # -------------------------
    change_opt = def_change_dir_opt()
    venvm.add_option(change_opt)
    # -------------------------
    create_batch_opt = def_create_batch_opt()
    venvm.add_option(create_batch_opt)
    
    return venvm

def def_create_batch_opt() -> Option:
    msg = """
    <name or void> Creates a batch file for executing the program.
    By default the name is 'venvm.bat'
    """
    create_bat = Option (
        '--create-batch', description=msg,
        extra_arg=True
    )
    
    return create_bat

def def_cd_opt() -> Option:
    msg = """
    changes the cmd dir to the virtual enviroments dir
    """
    cd = Option(
        '--cd', description=msg
    )

    return cd

def def_dir_opt() -> Option:
    msg = """shows the directory where the virtual environments
    are located"""
    dir_ = Option(
        '--venvs-dir', description=msg
    )
    
    return dir_

def def_reveal_venvs_opt() -> Option:
    msg = """
    reveals the directory with the virtual environments
    """
    reveal_venvs = Option(
        '--reveal-venvs', description=msg
    )
    
    return reveal_venvs

def def_change_dir_opt() -> Option:
    msg = """
    <new_dir> changes the program working directory where the virtual
    environments will be created
    """
    change_dir = Option(
        '--change-dir', description=msg,
        extra_arg=True, mandatory=True
    )
    
    return change_dir

venvm_logger = logging.getLogger(__name__)
def venvm(args:list=[], options:dict={}, flags:list=[], nested_cmds:dict={}):
    if "--create-batch" in options:
        name = "venvm"
        opt_args = options["--create-batch"]
        if bool(opt_args):
            name = opt_args[0]
        name = f"{name}.bat"
        try:
            with open(name, 'w') as file:
                file.write(venvm_bat_file)
        except Exception as err:
            msg = f" No se pudo crear el archivo '{name}'"
            msg += f"\n      ERR MSG: {err}"
            venvm_logger.error()
        else:
            venvm_logger.info(f" Archivo '{name}' creado con exito")
        return
    sdbatch_init()
    venvs_dir = register.load('venvs_dir')
    if venvs_dir is None:
        valid_dir = False
        while not valid_dir:
            msg = ' + Add the directory where the '
            msg += 'virtual environments will be saved'
            print(msg)
            venvs_dir = str(input(" + Directory: "))
            if os.path.exists(venvs_dir):
                valid_dir = True
            else:       
                venvm_logger.error(f" The directory '{venvs_dir}' doesn't exist")
                print()
        register.add('venvs_dir', venvs_dir)
        venvm_logger.info(f" The directory '{venvs_dir}' has been saved")
    if "--venvs-dir" in options:
        print(f"     + Virtual Environments Location --> '{venvs_dir}'")
        return
    elif "--reveal-venvs" in options:
        Popen(f'start %windir%\explorer.exe "{venvs_dir}"', shell=True)
        venvm_logger.info(" File explorer window has been openned")
        return
    elif "--cd" in options:
        task = f'cd "{venvs_dir}" & exit /B'
        sdbatch_append_task(task, "change dir")
        # Popen(f'start cmd /k "cd {venvs_dir}"', shell=True)
        venvm_logger.info(f" Changing cmd dir to -> {venvs_dir}..")
        return
    elif "--change-dir" in options:
        new_dir = options["--change-dir"][0]
        if os.path.exists(new_dir):
            venvs_dir = new_dir
            register.update('venvs_dir', new_dir)
            venvm_logger.info(f" Directory '{new_dir}' has been saved")
        else:       
            venvm_logger.error(f" The directory '{venvs_dir}' doesn't exist")
        return
    
    openning_msg = f" --- VENVS DIRECTORY: '{venvs_dir}' ---"
    print("-"*len(openning_msg))
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
    elif "clear" in nested_cmds:
        cmd_info = nested_cmds.pop("clear")
        clear(**cmd_info)
    else:
        print(" + Program that manages python virtual environments with 'virtualenv' module")
    print()
    print("-"*len(openning_msg))
    
