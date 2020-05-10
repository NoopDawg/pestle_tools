import os

from pestle.utils import pestlepath

class {{cookiecutter.SigToolname}}(SigTool):

    def __init__(self, *argv):
        sigName = '{{cookiecutter.SigToolname}}'
        configFile = os.path.join(pestlepath(), 'resources', '.'.join(['pestle', 'sigtools', sigName, 'arg']))
        super().__init__(sigName, configFile, *argv)
