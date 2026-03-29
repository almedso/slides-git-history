# Find the bug in this application below as fast as you can
# Hint: It is in the file that deviates from the other files in this exercise

import sys
import pkgutil
import importlib

def import_submodules(package_name):
    package = importlib.import_module(package_name)
    results = {}

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        full_name = f"{package_name}.{module_name}"
        results[module_name] = importlib.import_module(full_name)

    return results

verbose = True


def application():
    return_code = 0

    mods = import_submodules("modules")

    for name, mod in mods.items():
        mod_no = int(name[1:])  # Extract the number from the module name
        return_code +=  2 * mod.add() -  mod.subtract() - mod_no

    if verbose:
        if return_code == 0:
            print("Application executed successfully")
        else:
            print("Application failed with return code:", return_code)
    return return_code


if __name__ == "__main__":
    sys.exit(application())

