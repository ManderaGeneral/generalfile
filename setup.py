from setuptools import setup

setup(
    name = "generalfile",
    version = "0.0.7",
    description = "Easily manage files",
    py_modules = ["generalfile"],
    install_requires = ['send2trash', 'pandas']
)

