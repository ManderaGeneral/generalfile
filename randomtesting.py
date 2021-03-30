
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir


# Path().absolute().get_parent().view(spawn=True, filt=lambda x: not x.name().startswith("."))

Path().open_folder()
