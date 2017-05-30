import os
from configparser import ConfigParser

class Config():

    def __init__(self):
        config = ConfigParser()
        
        # Read configuration file
        lib_dir = os.path.dirname( os.path.realpath(__file__) )
        config.read(lib_dir + '/../config/facechecker.cfg')

        self.config = config 

    def getConfig(self):
        return self.config

