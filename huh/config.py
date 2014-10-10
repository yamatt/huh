import os
import yaml

class Config(object):
    ENVIRONMENT_VARIABLE = "{0}_CONFIG_PATH".format(__name__.upper())
    DEFAULT_FILE = "config.yaml"
    
    @classmethod
    def auto_load(cls):
        if os.environ.get(cls.ENVIRONMENT_VARIABLE):
            return cls.from_environment_variable()
        elif os.path.isfile(cls.DEFAULT_FILE):
            return cls.from_file_path()
        else:
            raise RuntimeError("Config file cannot be found.")
    
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
            return cls(**yaml.load(f))
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)
            else:
                print("WARNING: '{0}' skipped as it already exists in the config object".format(k))
