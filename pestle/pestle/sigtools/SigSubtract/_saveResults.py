def _saveResults(self, out_path):
    # Place routines for saving, plotting etc. here
    res = self.getResults()

    print("Result is: {}".format(res.difference))
