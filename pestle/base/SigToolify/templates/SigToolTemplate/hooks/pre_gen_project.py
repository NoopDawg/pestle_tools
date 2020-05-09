import re, sys

MODULE_REGEX = r'^Sig[a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.SigToolname }}'

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: %s is not a valid SigTool name!".format(module_name))

    # exits with status 1 to indicate failure
    sys.exit(1)
