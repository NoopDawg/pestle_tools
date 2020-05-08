import time
import os
import traceback

class SigClass:

# Public Methods
    def __init__(self, sigName, configFile,**kwargs):
        self._sigName = sigName
        self._configFile = configFile
        self._args = {}
        self._res = None
        self._wkdir = None
        self._state = None
        self._mode = None
        self._t0 = None
        self._tend = None
        self.parseArgs(**kwargs)

    def parseArgs(self, **kwargs):
        self._parseArgs(**kwargs)

    def run(self, **kwargs):
        try:
            self.parseArgs(**kwargs)
            self.runAnalysis()
            if (self._state == 'SUCCESS') & (self.mode == 'default'):
                self.saveResults()
            if os.path.exists(self._wkdir):
                out_stream = os.path.join(self._wkdir, "success.txt")
                print("# Completed in {:2.2f}".format(self._tend),
                      file=open(out_stream, "w"))
        except Exception as e:
            self._state = 'FAILURE'
            if os.path.exists(self._wkdir):
                out_stream = os.path.join(self._wkdir, "failure.txt")
                traceback.print_exc(file=open(out_stream, "w"))
            raise

    def runAnalysis(self):
        self._state = "RUNNING"
        self.tic()
        self._classMain()

    def saveResults(self, **kwargs):
        raise NotImplementedError

    def runTests(self):
        self._runTests()

    def runDemo(self):
        self._runDemo()

    def getArgs(self):
        return self._args

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

    @property
    def mode(self):
        return self._mode

    @property
    def wkdir(self):
        return self._wkdir

    def tic(self): #based off Matlab tic-toc functionality
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
        if (self.mode == "default"):
            self._runAnalysis()

    def _parseArgs(self, **kwargs):
        raise NotImplementedError

    def _runDemo(self):
        raise NotImplementedError

    def _runTests(self):
        raise NotImplementedError

    #Protected, Abstract methods
    def _runAnalysis(self):
        raise NotImplementedError('Abstract')

    def _checkArgs(self):
        raise NotImplementedError('Abstract')

    def _saveResults(self, out_path):
        raise NotImplementedError('Abstract')
