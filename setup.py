from setuptools import setup, find_packages

setup(
    name = "generalfile",
    version = "1.0.0",
    description = (""
                   "Finished TSV."
                   " Easily manage files."
                   ""),
    packages = find_packages(),
    install_requires = ['send2trash', 'pandas', 'wheel']
)

