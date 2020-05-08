import yaml, argparse
import os


class ArgParse:
    def ArgParse(self):
        parser = argparse.ArgumentParser()
        config_files = dict()

    def addFile(self, cfg_file):
        if os.path.exists(cfg_file):
            with open (cfg_file) as file:
                config = yaml.load(cfg_file)

            for arg in config:
                if 'ispreamble' in arg:
                    if arg['preamble']:
                        self.name = arg['name']
                        self.summary = arg['summary']
                        self.include = arg['include']
                        self.description = arg['description']
                else:
                    self.add(arg)

        else:
            raise FileNotFoundError


    def add(self, arg):
        raise NotImplementedError
