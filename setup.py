from setuptools import setup

setup(
    name = "generalfile",
    version = "0.1.0",
    description = (""
                   "Working. Batch unit test works when targeting generalfile folder. Cannot right click test folder."
                   "Changed test folder structure. Changed mod and creation time to use time.time()."
                   "Easily manage files."
                   ""),
    py_modules = ["generalfile"],
    install_requires = ['send2trash', 'pandas']
)

