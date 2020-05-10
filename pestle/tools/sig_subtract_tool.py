from pestle.pestle.sigtools.SigSubtract import SigSubtract

def sig_subtract_tool(*argv):
    obj = SigSubtract(*argv)
    obj.run(*argv)
