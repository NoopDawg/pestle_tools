from types import SimpleNamespace as Namespace  # for familiarity with MATLAB


def _runAnalysis(self):
    # Place bulk of analysis here
    args = self.getArgs()

    diff = args.minuend - args.subtrahend

    res = Namespace(difference=diff)
    print("Result: {} - {} = {}".format(args.minuend, args.subtrahend, diff))

    return res
