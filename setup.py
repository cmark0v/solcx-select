from setuptools import setup

__version__ = "0.2.0"

setup(
    name="solcx-select",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "py-solc-x",
    ],
    packages=["solcx_select"],
    entry_points={
        "console_scripts": ["solcx-select=solcx_select:main"],
    },
    keywords=["solc", "solcx", "solidity", "ethereum"],
    description = "Console script to symlink py-solc-x installed solc binaries to allow access from the command line in the style of solc-select",
    license = "GPLv3",
        version = __version__,
)
