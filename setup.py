from setuptools import setup, find_packages

setup(
    # this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name='snakeParser',
    # some version number you may wish to add - increment this after every update
    version='1.10',

    # this approach automatically finds out all directories (packages) - those must contain a file named __init__.py
    packages=find_packages(include='*'),  # include/exclude arguments take * as wildcard, . for any sub-package names
)