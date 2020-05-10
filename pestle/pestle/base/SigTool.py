import os
from datetime import datetime

from pestle.pestle.base.SigClass import SigClass
from pestle.pestle.common.ArgParse import ArgParse
from pestle.utils.io import write_args

class SigTool(SigClass):
    def __init__(self, sigName, configFile, *argv):
        super().__init__(sigName, configFile, *argv)

