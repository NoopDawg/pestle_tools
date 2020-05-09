import yaml, argparse
import os

from utils.pestlepath import pestlepath

def get_input_type(type_str):
    if type_str == 'int':
        return int
    elif type_str == 'float':
        return float
    elif type_str == 'string':
        return str
    else:
        return None

class ArgParse:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.config_files = dict()

    def addFile(self, cfg_file):
        if os.path.exists(cfg_file):
            with open (cfg_file, 'r') as file:
                config = yaml.load(file, Loader=yaml.FullLoader)

            for arg in config:
                if 'ispreamble' in arg:
                    if arg['ispreamble']:
                        self.name = arg['name']
                        self.summary = arg['summary']
                        self.include = arg['include']
                        self.description = arg['description']

                        for fname in arg['include']:
                            full_path = os.path.join(pestlepath(), 'resources', fname)
                            assert (os.path.exists(full_path)),\
                                "Args include {} not found".format(full_path)
                            self.addFile(full_path)
                else:
                    self.add(arg)

        else:
            raise FileNotFoundError("File {} not found".format(cfg_file))

    def add(self, arg):
        assert ("name" in arg.keys()), "arg file \'name\' required"
        assert ("help" in arg.keys()), "arg file \'help\' required"

        #Flag arguments
        if "action" in arg.keys():
            if arg['action'] == 'store_true':
                self.parser.add_argument(arg['name'], action=arg['action'], help=arg['help'])
            elif arg['action'] == 'read_args':
                pass
            else:
                raise ValueError("Unknown action in arg name: {}\naction: {}\n"
                                 .format(arg['name'], arg['action']))
            return

        assert ("default" in arg.keys()), "arg file \'default\' required"
        if 'type' in arg.keys():
            self.parser.add_argument(arg['name'], help=arg['help'], default=arg['default'], type=get_input_type(arg['type']))
        else:
            self.parser.add_argument(arg['name'], help=arg['help'], default=arg['default'])
