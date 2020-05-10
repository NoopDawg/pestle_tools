import os
import inspect
from pestle import pestle

def pestlepath():
    return inspect.getabsfile(pestle).replace('pestle/__init__.py', '')

def get_tool_registry():
    return os.path.join(pestlepath(), 'resources', 'tool_registry.txt')
