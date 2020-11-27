


from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir
setup_workdir()
Path.get_working_dir().open_folder()
# Path.get_lock_dir().open_folder()


import json


# print(json.loads('[1, 2, "a"]'))


Path("foo").cfg.write({'test': {'foo': 'bar', "hi": ["a", "b", 3]}})
print(Path("foo").cfg.read())
