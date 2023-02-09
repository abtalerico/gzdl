import configparser


class GzdlModel:
    @staticmethod
    def from_config(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return GzdlModel(config["DEFAULT"]["gzdoom_path"], config["DEFAULT"]["iwad_directory"], config["DEFAULT"]["command_line"])

    def __init__(self, gzdoom_path="", iwad_directory="", command_line=""):
        self.gzdoom_path = gzdoom_path
        self.iwad_directory = iwad_directory
        self.command_line = command_line
