from cookiecutter.main import cookiecutter
import os
import datetime
from pestle.utils import pestlepath
from pestle.utils import get_tool_list, get_registry

class SigToolify():
    def __init__(self):
        SigToolPackage = 'pestle.sigtools'

    def new(self):
        print("Do not override change pestlepath")
        pestle_path = pestlepath()
        template_path = os.path.join(pestle_path, 'pestle/base/SigToolify/templates/SigToolTemplate/')
        print(template_path)
        today = datetime.datetime.today()
        date = today.date().isoformat()
        year = today.year

        extra_context = {
                'release_date': date,
                'pestlepath': pestle_path
                }

        cookiecutter(template_path,
                     output_dir=os.path.join(pestle_path, 'pestle', 'sigtools'),
                     extra_context=extra_context)

    def convert_toolname_to_sigName(self, sigName):
        return "Sig{}".format(sigName.split('_')[1].capitalize())

    def tool_files(self):
        registry = get_registry()
        print("Select tool to show filepaths")
        toollist = registry['toolname']
        for idx in range(0, len(registry)):
            print("{}. {}".format(idx+1, toollist[idx]))
        selection = int(input("Select tool with number:"))
        toolname = toollist[selection-1]
        print("Tool Location:\n {}".format(
                    registry.loc[registry['toolname'] == toolname, 'tool_location'].item()))
        mod_path = registry.loc[registry['toolname'] == toolname, 'module_path'].item()
        print("Module path:\n {}".format(mod_path))
        print("\t runAnalysis: {}".format(os.path.join(mod_path, '_runAnalysis.py')))
        print("\t checkArgs: {}".format(os.path.join(mod_path, '_checkArgs.py')))
        print("\t saveResults: {}".format(os.path.join(mod_path, '_saveResults.py')))
        print("Arguments path:\n {}".format(
           registry.loc[registry['toolname'] == toolname, 'args_file'].item()))
        print("Tests path:\n {}".format(
           registry.loc[registry['toolname'] == toolname, 'test_file'].item()))


