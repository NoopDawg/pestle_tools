import os
import inspect
import pandas as pd
from pestle import pestle


def pestlepath():
    return inspect.getabsfile(pestle).replace("pestle/__init__.py", "")


def tool_registry_file():
    return os.path.join(pestlepath(), "resources", "tool_registry.txt")


def get_tool_list():
    file = os.path.join(pestlepath(), "resources", "tool_registry.txt")
    registry = pd.read_csv(file, sep="\t")
    return list(registry["toolname"])


def get_registry():
    file = os.path.join(pestlepath(), "resources", "tool_registry.txt")
    registry = pd.read_csv(file, sep="\t")
    return registry
