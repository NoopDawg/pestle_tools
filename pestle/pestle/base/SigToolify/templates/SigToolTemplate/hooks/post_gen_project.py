import os, sys
import pandas as pd

MODULE_REGEX = r'^Sig[a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.SigToolname }}'
pestlepath = '{{ cookiecutter.pestlepath }}'

# Move args file
args_src= os.path.join(pestlepath, 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}',
                       '.'.join(['pestle', 'sigtools', '{{ cookiecutter.SigToolname }}', 'arg']))

args_dest = os.path.join(pestlepath, 'resources',
                        '.'.join(['pestle', 'sigtools', '{{ cookiecutter.SigToolname }}', 'arg']))

os.rename(args_src, args_dest)

# Move toolfile
tool_src = os.path.join(pestlepath, 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}',
                       '{{cookiecutter.toolname}}.py')

tool_dest = os.path.join(pestlepath, 'tools',
                       '{{cookiecutter.toolname}}.py')
os.rename(tool_src, tool_dest)

# Move tests
tests_src = os.path.join(pestlepath, 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}',
                       'test{{cookiecutter.SigToolname}}.py')

tests_dest = os.path.join(pestlepath, 'tests',
                         'test{{cookiecutter.SigToolname}}.py')

os.rename(tests_src, tests_dest)


"""
with open(registry_file, 'r') as f_in:
    tool_list = f_in.read().splitlines()
    tool_list.append('{{cookiecutter.toolname}}')
    with open(registry_file, 'w+') as f_out:
        for tool in tool_list:
            f_out.write("{}\n".format(tool))
"""

registry_file = os.path.join(pestlepath, 'resources', 'tool_registry.txt')

new_tool = {}
tool_dir = os.path.join(pestlepath, 'pestle', 'sigtools',
                       '{{ cookiecutter.SigToolname }}/')
new_tool['sigName'] = ["{{ cookiecutter.SigToolname }}"]
new_tool['toolname'] = ["{{ cookiecutter.toolname }}"]
new_tool['tool_location'] = [tool_dest]
new_tool['module_path'] = [tool_dir]
new_tool['args_file'] = [args_dest]
new_tool['test_file'] = [tests_dest]
new_tool = pd.DataFrame(data=new_tool)

if os.path.exists(registry_file):
    registry = pd.read_csv(registry_file, sep='\t')
    registry = registry.append(new_tool).sort(columns=['toolname'])
    registry.to_csv(registry_file, sep='\t', index=False)
else:
    new_tool.to_csv(registry_file, sep='\t', index=False)
