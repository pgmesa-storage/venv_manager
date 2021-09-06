
import sys
import logging
import platform
from mypy_modules.cli import Cli, CmdLineError
from commands.venvm import get_venvm_cmd, venvm
from commands.reused_funcs import save_calling_dir

logging.basicConfig(level=logging.NOTSET)
main_logger = logging.getLogger(__name__)
def main():
    cli = Cli(get_venvm_cmd())
    try:
        sys_args = save_calling_dir(sys.argv)
        args_processed = cli.process_cmdline(sys_args)
        os = platform.system()
        if os != "Windows":
            err_msg = f" Este programa no soporta '{os}':OS"
            main_logger.critical(err_msg)
            exit(1)
        main_logger.info(" Programa iniciado")
        venvm(**args_processed)
    except CmdLineError as err:
        main_logger.error(f" {err}")
        exit(1)
    # except Exception as err:
    #     main_logger.error(f" Error Inesperado: '{err}'")
    #     exit(1)
    else:
        main_logger.info(" Programa finalizado correctamente")

if __name__ == "__main__":
    main()