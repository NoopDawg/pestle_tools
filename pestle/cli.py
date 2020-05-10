import sys
import traceback
from pestle.pestle.base.SigToolify import SigToolify
from pestle.utils import get_tool_registry

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def run_module(name):
    tool = import_from(name, 'sig_subtract_tool')
    tool(['--ds', 'input.txt'])

def run_tool(toolname, *argv):
    tool = import_from('.'.join(['pestle','tools',toolname]), toolname)
    tool(*argv)

def pestle_help():
    print("Pestle: Sigtool generator and runner )

def print_tools():
    registry_file = get_tool_registry()
    with open(registry_file, 'r') as f:
        toollist = f.read().splitlines()
        print("Available tools:")
        for toolname in toollist:
            print("\t {}".format(toolname))
        print('')

def toolify_help():
    print("Toolify available commands:")
    print("new\t Make new SigTool using cookiecutter template\n")



def main(argv=None):
    if len(sys.argv) < 2:
        print( "missing command" )
        sys.exit(0)

    if sys.argv[1] == 'runtool':
        if len(sys.argv) < 3:
            print("\nUsage: pestle runtool [toolname] [-h] [options]\n")
            print_tools()
        else:
            try:
                run_tool(sys.argv[2], sys.argv[3:])
            except ModuleNotFoundError as exc:
                traceback.print_exc()
                print(exc)
                print("No tool {} found".format(sys.argv[2]))
                print_tools()
                exit(1)

    elif sys.argv[1] == 'toolify':
        if len(sys.argv) < 3:
            toolify_help()
            sys.exit(0)

        toolify = SigToolify()
        if sys.argv[2] == 'new':
            toolify.new()
        if sys.argv[2] == 'help':
            toolify_help()
        else:
            toolify_help()
            print("Unknown toolify command: {}")
    else:
        print("Unknown command: {}".format(sys.argv[1]))
