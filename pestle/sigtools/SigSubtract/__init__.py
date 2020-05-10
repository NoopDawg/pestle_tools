import os

from pestle.base.SigTool import SigTool
from utils.pestlepath import pestlepath

class SigSubtract(SigTool):
    from ._checkArgs import _checkArgs
    from ._runAnalysis import _runAnalysis
    from ._saveResults import _saveResults

    def __init__(self, *argv):
        sigName = 'SigSubtract'
        configFile = os.path.join(pestlepath(), 'resources', '.'.join(['pestle', 'sigtools', sigName, 'arg']))
        super().__init__(sigName, configFile, *argv)