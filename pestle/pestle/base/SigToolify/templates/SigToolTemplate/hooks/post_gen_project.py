import os
from pestle.utils import pestlepath

MODULE_REGEX = r'^Sig[a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.SigToolname }}'

# Move args file
args_src= os.path.join(pestlepath(), 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}',
                       '.'.join(['pestle', 'sigtools', '{{ cookiecutter.SigToolname }}', 'arg']))

args_dest = os.path.join(pestlepath(), 'resources',
                        '.'.join(['pestle', 'sigtools', '{{ cookiecutter.SigToolname }}', 'arg']))

os.rename(args_src, args_dest)

# Move toolfile
tool_src = os.path.join(pestlepath(), 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}',
                       '{{cookiecutter.toolname}}.py')

tool_dest = os.path.join(pestlepath(), 'tools',
                       '{{cookiecutter.toolname}}.py')
os.rename(tool_src, tool_dest)

# Move tests
tests_src = os.path.join(pestlepath(), 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}',
                       'test{{cookiecutter.SigToolname}}.py')

tests_dest = os.path.join(pestlepath(), 'tests',
                         'test{{cookiecutter.SigToolname}}.py')

os.rename(tests_src, tests_dest)

registry_file = os.path.join(pestlepath(), 'resources', 'tool_registry.txt')

with open(registry_file, 'r') as f_in:
    tool_list = f_in.read().splitlines()
    tool_list.append('{{cookiecutter.toolname}}')
    with open(registry_file, 'w+') as f_out:
        for tool in tool_list:
            f_out.write("{}\n".format(tool))
