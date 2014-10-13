import os
import sys

import yaml

class Config(object):
    ENVIRONMENT_VARIABLE = "{0}_CONFIG_PATH".format(__name__.upper())
    DEFAULT_FILE = "config.yaml"
    DEFAULT_NIX_FILE = "~/.config"
    DEFAULT_WIN_FILE = os.environ.get('APPDATA')
    
    @classmethod
    def auto_load(cls):
        if os.environ.get(cls.ENVIRONMENT_VARIABLE):
            return cls.from_environment_variable()
        else:
            if 'win' in sys.platform:
                file_path = os.path.join(cls.DEFAULT_WIN_FILE, cls.DEFAULT_FILE)
                if os.path.exists(file_path):
                    return cls.from_file_path(file_path)
            else:
                file_path = os.path.join(cls.DEFAULT_NIX_FILE, cls.DEFAULT_FILE)
                if os.path.exists(file_path):
                    return cls.from_file_path(file_path)
        raise RuntimeError("Configuration file at '{0}' could not be found.".format(file_path))
    
    @classmethod
    def from_environment_variable(cls, environment_variable=None):
        if not environment_variable:
            environment_variable = cls.ENVIRONMENT_VARIABLE
        return cls.from_file(os.environ[environment_variable])
        
    @classmethod
    def from_file_path(cls, file_path=None):
        if not file_path:
            file_path = cls.DEFAULT_FILE
            
        with open(file_path, "r") as f:
            return cls.from_file(f)
            
    @classmethod
    def from_file(cls, file):
        return cls(**yaml.load(file))
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)
            else:
                print("WARNING: '{0}' skipped as it already exists in the config object".format(k))
