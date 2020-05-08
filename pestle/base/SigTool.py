import pestle.base.SigClass as SigClass
import pestle.common.ArgParse.ArgParse as ArgParse

class SigTool(SigClass):
    def _main(self, **kwargs):
        #call runAnalysis and saveResults routine, passing results between the two.
        #also calls demo/test if test and demo flags are called
        ...

    def _getArgs(self, toolName, configFile, **kwargs):
        #parse Args
        args = ArgParse()
        args.addFile(configFile)

        ... #Make output folder, record input parameters
