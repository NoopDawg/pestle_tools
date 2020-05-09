import pestle
import inspect

def pestlepath():
    return inspect.getabsfile(pestle).replace('pestle/__init__.py', '')
