


from generalfile import Path
# from generalfile.test.setup_workdir import setup_workdir
# setup_workdir()
# Path.get_working_dir().open_folder()
# Path.get_lock_dir().open_folder()


print(Path.get_working_dir())

with Path("hello").as_working_dir():
    print(Path.get_working_dir())

print(Path.get_working_dir())


