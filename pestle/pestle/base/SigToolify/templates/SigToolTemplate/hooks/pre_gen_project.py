import re, sys, os
import pandas as pd

MODULE_REGEX = r"^Sig[a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.SigToolname }}"

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: {} is not a valid SigTool name!".format(module_name))

    # exits with status 1 to indicate failure
    sys.exit(1)

registry_file = os.path.join(
    "{{ cookiecutter.pestlepath }}", "resources", "tool_registry.txt"
)

if os.path.exists(registry_file):
    registry = pd.read_csv(registry_file, sep="\t")
    tools = list(registry["toolname"])

    assert (
        "{{ cookiecutter.toolname }}" not in tools
    ), "Sigtool with name {} already exists".format("{{cookiecutter.SigToolname}}")
