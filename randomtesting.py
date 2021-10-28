
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir


setup_workdir()

Path().open_folder()

class A:
    def __init__(self):
        self.x = 53

Path("hi.txt").pickle.write(A())

a = Path("hi.txt").pickle.read()

print(a.x)
