


from generalfile import Path
# from generalfile.test.setup_workdir import setup_workdir
# setup_workdir()
# Path.get_working_dir().open_folder()
# Path.get_lock_dir().open_folder()

from pprint import pprint


pprint(Path("generalfile").get_differing_files(Path("target/generalfile"), exist=False, content=True))
