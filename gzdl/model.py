import configparser
import hashlib
import os
from .iwad import IWADS


class GzdlModel:
    @staticmethod
    def from_config(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return GzdlModel(config["DEFAULT"]["gzdoom_path"], config["DEFAULT"]["iwad_directory"],
                         config["DEFAULT"]["command_line"])

    def __init__(self, gzdoom_path="", iwad_directory="", command_line=""):
        self.gzdoom_path = gzdoom_path
        self.iwad_directory = iwad_directory
        self.command_line = command_line
        self.available_iwads = []

    def load_iwads(self):
        if os.path.isdir(self.iwad_directory):
            files = os.listdir(self.iwad_directory)
            for file in files:
                if os.path.isfile(self.iwad_directory + "/" + file):
                    with open(self.iwad_directory + "/" + file, 'rb') as iwad_file:
                        md5 = hashlib.md5(iwad_file.read())
                        for iwad in IWADS:
                            if md5 == iwad["md5"] or str.lower(os.path.basename(iwad_file.name)) == iwad["filename"]:
                                self.available_iwads.append(iwad)
        else:
            raise Exception("IWAD directory does not exist")
