

from generallibrary import getLocalFeaturesAsMD

from generalfile import *


# getLocalFeaturesAsMD(locals(), "generalfile")
getLocalFeaturesAsMD({k: getattr(Path, k, None) for k in dir(Path)}, "generalfile")

