import sys
import traceback
from pestle.pestle.base.SigToolify import SigToolify
from pestle.utils import get_tool_list

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
    print("Pestle: Sigtool generator and runner\n")
    print("Avaliable commands:")
    print("\truntool\t\t Run tool from tool catalog. Running without args shows usage")
    print("\ttoolify\t\t Tool to manage creation of tools")

def print_tools():
    toollist = get_tool_list()
    for toolname in toollist:
        print("\t {}".format(toolname))
    print('')

def toolify_help():
    print("Toolify available commands:")
    print("new\t Make new SigTool using cookiecutter template\n")

def main(argv=None):
    if len(argv) < 2:
        pestle_help()
        sys.exit(0)

    if argv[1] == 'runtool':
        if len(argv) < 3:
            print("\nUsage: pestle runtool [toolname] [-h] [options]\n")
            print_tools()
        else:
            try:
                run_tool(argv[2], argv[3:])
            except ModuleNotFoundError as exc:
                traceback.print_exc()
                print(exc)
                print("No tool {} found".format(sys.argv[2]))
                print_tools()
                exit(1)

    elif argv[1] == 'toolify':
        if len(argv) < 3:
            toolify_help()
            sys.exit(0)

        toolify = SigToolify()
        if argv[2] == 'new':
            toolify.new()
        elif argv[2] == 'list_files':
            toolify.tool_files()
        elif argv[2] == 'help':
            toolify_help()
        else:
            toolify_help()
            print("Unknown toolify command: {}")
    else:
        print("Unknown command: {}".format(argv[1]))
