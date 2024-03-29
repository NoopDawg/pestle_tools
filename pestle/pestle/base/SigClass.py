import time
from datetime import datetime
import os, sys
import traceback
import unittest

from pestle.pestle.common.ArgParse import ArgParse
from pestle.utils.io import write_args
from pestle.utils import pestlepath


class SigClass:

    # Public Methods
    def __init__(self, sigName, configFile, *argv):
        self._sigName = sigName
        self._toolname = "sig_{}_tool".format(sigName.replace("Sig", "").lower())
        self._configFile = configFile
        # Should be dict
        self._args = {}
        self._res = None
        self._wkdir = None
        self._state = None
        self._mode = None
        self._t0 = None
        self._tend = None
        self._testSuite = ".".join(["pestle", "tests", "test{}".format(sigName)])
        # self.parseArgs(*argv)

    def parseArgs(self, *argv):
        self._parseArgs(*argv)

    def run(self, *argv):
        try:
            self.parseArgs(*argv)
            self.runAnalysis()
            if (self._state == "SUCCESS") & (self.mode == "default"):
                self.saveResults()
            if os.path.exists(self._wkdir):
                out_stream = os.path.join(self._wkdir, "success.txt")
                print(
                    "# Completed in {:2.2f}".format(self._tend),
                    file=open(out_stream, "w"),
                )
        except Exception as e:
            self._state = "FAILURE"
            if os.path.exists(self._wkdir):
                out_stream = os.path.join(self._wkdir, "failure.txt")
                traceback.print_exc(file=open(out_stream, "w"))
            raise

    def runAnalysis(self):
        self._state = "RUNNING"
        self.tic()
        self._classMain()  # runs analysis, demo or test
        tend = self.toc()
        print("# Completed in {:2.2f}s".format(tend))
        self.state = "SUCCESS"

    def saveResults(self, *argv):
        wkdir = self.wkdir
        if not os.path.exists(wkdir):
            os.mkdir(wkdir)
            print("Creating working dir: {}".format(wkdir))
        else:
            # print("Working directory {} exists  ".format(wkdir))
            # print config
            self._saveResults(out_path=wkdir)

    def runTests(self):
        self._runTests()

    def runDemo(self):
        self._runDemo()

    def getArgs(self):
        return self._args

    def getResults(self):
        return self._res

    def setArg(self, key, value):
        if key in self._args:
            self._args[key] = value
        else:
            raise KeyError("Key: {} is not a valid argument".format(key))

    def setArgs(self, args):
        for key, val in args:
            self.setArg(key, val)

    @property
    def sigName(self):
        return self._sigName

    @property
    def configFile(self):
        return self._configFile

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def wkdir(self):
        return self._wkdir

    @wkdir.setter
    def wkdir(self, value):
        self._wkdir = value

    def tic(self):  # based off Matlab tic-toc functionality
        self._t0 = time.time()
        self._tend = -1

    def toc(self):
        if self._t0:
            self.tend_ = time.time()
            return time.time() - self._t0
        else:
            return self._tend

    # Protected methods
    def _classMain(self):
        if self.mode == "default":
            self._res = self._runAnalysis()
        elif self.mode == "test":
            self._runTests()
        elif self.mode == "demo":
            self._runDemo()
        else:
            assert False, "Unknown run mode"

    def _parseArgs(self, *argv):
        arg_parse = ArgParse()
        arg_parse.addFile(self.configFile)

        arg_parse.parser.prog = self._toolname
        if len(*argv) < 1:
            arg_parse.parser.print_help()
            sys.exit(0)
        args = arg_parse.parser.parse_args(*argv)  # parse arguments

        if args.rundemo:
            self.mode = "demo"
        elif args.runtests:
            self.mode = "test"
        else:
            self.mode = "default"

        self._args = args

        self._checkArgs()  # Validate arguments

        if not args.out:
            args.out = os.curdir
        if args.create_subdir:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            wkdir = os.path.join(args.out, "{}_{}".format(self.sigName, timestamp))
        else:
            wkdir = args.out
        if os.path.exists(wkdir):
            print("Working directory exists: {}".format(wkdir))
        else:
            print("Creating working dir: {}".format(wkdir))
            os.mkdir(wkdir)

        args.out = wkdir
        self.wkdir = wkdir
        self._args = args
        write_args(args, wkdir, to_console=False)
        return args

    def _runDemo(self):
        raise NotImplementedError("Demos not yet implemented")

    def _runTests(self):
        print("Running Teests")
        suite = unittest.TestLoader().loadTestsFromName(self._testSuite)
        unittest.TextTestRunner(verbosity=2).run(suite)

    # Protected, Abstract methods
    def _runAnalysis(self):
        raise NotImplementedError("Abstract")

    def _checkArgs(self):
        raise NotImplementedError("Abstract")

    def _saveResults(self, out_path):
        raise NotImplementedError("Abstract")
