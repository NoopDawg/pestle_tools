import os

import pestle.base.SigTool as SigTool
from utils.pestlepath import pestlepath

class {{cookiecutter.SigToolname}}(SigTool):
    from ._checkArgs import _checkArgs
    from ._runAnalysis import _runAnalysis
    from ._saveResults import _saveResults

    def __init__(self, sigName, configFile, **kwargs):
        sigName = __name__
        configFile = os.path.join(pestlepath(), 'resources', sigName + '.arg')
        super().__init__(sigName, configFile, **kwargs)
