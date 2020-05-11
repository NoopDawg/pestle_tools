def _checkArgs(self):
    # Place sanity checks for arguments here
    args = self.getArgs()
    print("minuend is float")
    assert isinstance(args.minuend, float)
