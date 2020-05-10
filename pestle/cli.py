import sys

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def run_module(name):
    tool = import_from(name, 'sig_subtract_tool')
    tool(['--ds', 'input.txt'])

def run_tool(toolname, *argv):
    tool = import_from('.'.join('tools',toolname), toolname)
    tool(argv)


def main(argv=None):
    if len(sys.argv) < 2:
        print( "missing command" )

    if sys.argv[1] == 'pytool':
        print("foo")
    elif sys.argv[1] == 'toolify':
        print("toolify")
    else:
        print("Unknown command: {}".format(sys.argv[1]))

