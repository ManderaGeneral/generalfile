from setuptools import setup, find_packages

setup(
    name = "generalfile",
    version = "0.1.4",
    description = (""
                   "Trying new venv"
                   " Easily manage files."
                   ""),
    packages = find_packages(),
    install_requires = ['send2trash', 'pandas', 'wheel']
)

