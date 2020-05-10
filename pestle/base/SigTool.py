import os
from datetime import datetime

from pestle.base.SigClass import SigClass
from pestle.common.ArgParse.ArgParse import ArgParse
from utils.io import write_args


class SigTool(SigClass):
    def __init__(self, sigName, configFile, *argv):
        super().__init__(sigName, configFile, *argv)

    def getArgs(self, argv):
        self._getArgs(self.sigName, self.configFile, *argv)

    # Protected functions
    def _main(self, *argv):
        #call runAnalysis and saveResults routine, passing results between the two.
        #also calls demo/test if test and demo flags are called
        args = self.getArgs(argv)

        if args.runtests:
            self._runTests()
        elif args.rundemo:
            self._runDemo()
        else:
            raise NotImplementedError       #Doesn't seem to actually run in implementation

    def _getArgs(self, toolName, configFile, *argv):
        #parse Args
        arg_parse = ArgParse()
        arg_parse.addFile(configFile)

        self._args = arg_parse.parser.parse(argv) #parse arguments
        args = self._args

        self._checkArgs() #Validate arguments

        if not args.out:
            args.out = os.curdir()
        if args.create_subdir:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            wkdir = os.path.join(args.out, "{}_{}".format(toolName, timestamp))
        else:
            wkdir = args.out
        if os.path.exists(wkdir):
            print("Working directory exists: {}".format(wkdir))
        else:
            print("Creating working dir: {}".format(wkdir))
            os.mkdir(wkdir)

        args.out = wkdir
        self._args = args
        write_args(args, wkdir)
        return args
