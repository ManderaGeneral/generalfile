

import time
from generallibrary import getLocalFeaturesAsMD

from generalfile import Path

# Path.get_working_dir().open_folder()
# Path.get_lock_dir().open_folder()



# getLocalFeaturesAsMD(locals(), "generalfile")
# getLocalFeaturesAsMD({k: getattr(Path, k, None) for k in dir(Path)}, "generalfile")

import configparser
import json


class Cfg:  # I think we could actually use generalfile here instead, as we are doing that in lib already -> Add cfg as option dependency
    def __init__(self, path):
        self.config = configparser.RawConfigParser()
        self.config.read(path)

    def __call__(self, section, option):
        result = self.config.get(section, option)
        try:
            return json.loads(result)
        except json.decoder.JSONDecodeError:
            return result


cfg = Cfg("package_specific.cfg")


print(cfg("setup", "extras_require"))