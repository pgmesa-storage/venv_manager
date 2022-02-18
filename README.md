# Virtual Environment Manager (Only for Windows)

Minimalisitc tool that manages python virtual environments with 'virtualenv' module

## Requirements

The only dependency is to have 'virtualenv' module installed globally

## Run the program
Execute the following command in the program directory (I strongly recommend to add a .bat file that executes this file into PATH to run the program globally)
```
py main.py
```
## Program Functionalities

```
 venvm <parameters> <flags> <options> [command] <parameters> <flags> <options> [command] ...

  => venvm --> Allows to manage python virtual environments
     - commands:
        => add --> <venv_name> adds a new virtual environment
        => activate --> <venv_name> activates the virtual environment specified in another
                  cmd window
        => list --> lists the virtual environment created by the program
        => rm --> <venv_name> removes the virtual environment specified
        => clear --> removes all virtual environments
     - options:
        => --venvs-dir --> shows the directory where the virtual environments are located
        => --cd --> changes the cmd dir to the virtual enviroments dir
        => --reveal-venvs --> reveals the directory with the virtual environments
        => --change-dir --> <new_dir> changes the program working directory where the
                  virtual environments will be created
        => --create-batch --> <name or void> Creates a batch file for executing the
                  program. By default the name is 'venvm.bat'

 + Global Flags:
    -> -h --> shows overall information about a command or all of them if a valid one is
              not introduced
```
