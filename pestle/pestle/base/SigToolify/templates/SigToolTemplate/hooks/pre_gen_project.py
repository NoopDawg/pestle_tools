import re, sys, os

from pestle.utils import pestlepath

MODULE_REGEX = r'^Sig[a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.SigToolname }}'

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: {} is not a valid SigTool name!".format(module_name))

    # exits with status 1 to indicate failure
    sys.exit(1)

registry_file = os.path.join(pestlepath(), 'resources', 'tool_registry.txt')

with open(registry_file, 'r') as f:
    tools = f.read().splitlines()
    assert('{{ cookiecutter.toolname }}' not in tools),\
        "Sigtool with name {} already exists".format('{{cookiecutter.SigToolname}}')
