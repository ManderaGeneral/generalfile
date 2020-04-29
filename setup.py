from setuptools import setup

setup(
    name = "generalfile",
    version = "0.1.1",
    description = (""
                   "New documented file structure, first try."
                   "Easily manage files."
                   ""),
    packages = ["generalfile", "test", "generalfile.base", "test.base"],
    install_requires = ['send2trash', 'pandas']
)

