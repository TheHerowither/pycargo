import os
import json
import sys
from scripts.prepare_build import *
def list_to_string(list_a : list[str], sep = ""):
    return_val = ""
    for i in list_a:
        return_val = return_val + i + sep
    return return_val
def new_project(root : str, name : str, venv : bool, libs = []):
    print()
    path = f"{root}\{name}"
    #Check if the project already exists
    if os.path.exists(path):
        print("project already exists\n")
    #If not create it and all the neccesary bits
    else:
        #Create the directory
        os.mkdir(path)
        #Create main.py file
        with open(f"{path}\main.py", "w") as main:
            lib_import_list = [f"from {i} import *" for i in libs]
            lib_import_str = list_to_string(lib_import_list, "\n")
            main.write(f"import resources.lib.lib_{name} as lib\n{lib_import_str}")

        #Create file structure
        resources = f"{path}\\resources"
        assets = f"{resources}\\assets"
        lib = f"{resources}\\lib"
        #   Make folders
        os.mkdir(resources)
        os.mkdir(assets)
        os.mkdir(lib)
        os.mkdir(f"{path}\\.prc")
        #   Make scripts
        open(f"{lib}\\lib_{name}.py", "w").close()

        #   Create saving file for projectcreator
        with open(f"{path}\\.prc\\config.json", "w") as config:
            unparsed = {"libs" : libs, "name" : name}
            parsed = json.dumps(unparsed)

            config.write(parsed)
        #   Create gitignore
        with open(f"{path}\\.gitignore", "w") as gitignore:
            gitignore.write("/.prc\n")

        print(f"New project '{name}' has been created in path '{os.getcwd()}\{name}'")
    if venv:
        tmp = [f" --AddLib {i}" for i in libs]
        os.system(f"scripts\\venv {root} {name} {list_to_string(tmp)}")
        #Make a batch file to install all specified librarys
        with open(f"{path}\\activate_venv.bat", "w") as batch:
            batch.write("@echo off\n")
            batch.write("call Scripts\\activate.bat\n")
            lib_install_list = [f"echo Installing library {i}\npip install {i}" for i in libs]
            lib_install_str = list_to_string(lib_install_list, "\n")
            batch.write(lib_install_str)

def to_bool(a):
    if (a == "true" or a == "True" or a == "1"):
        return True
    if (a == "false" or a == "False" or a == "0"):
        return False
if sys.argv[1] == "new":
    params = sys.argv
    print(f"Creating project in {params[2]}/{params[3]}")
    new_project(params[2], params[3], to_bool(params[4]), [params[i] for i in range(5, len(params))])
elif sys.argv[1] == "build":
    print("Building project")
    start_build(os.getcwd())
else:
    print("operation invalid")