from typing import Literal

from generalfile import ConfigFile
from generallibrary import Ver


class Metadata(ConfigFile):
    enabled = True
    private = False
    name = None
    target: Literal["python", "node", "django", "exe"] = "python"
    version = Ver("0.0.1")
    description = "Missing description."
    topics = []
    manifest = []

