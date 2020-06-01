from setuptools import setup, find_packages

setup(
    name = "generalfile",
    version = "1.0.2",
    description = (""
                   "Added generallibrary.iterables.getRows()."
                   " Easily manage files."
                   ""),
    packages = find_packages(),
    install_requires = ['generallibrary', 'send2trash', 'pandas', 'wheel']
)

