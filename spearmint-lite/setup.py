
from setuptools import setup, find_packages
# you may need setuptools instead of distutils

packages = find_packages(exclude='scripts')
print(packages)

setup(
    # basic stuff here
    name = "spearmint-lite",
    version = "0.1",
    packages = packages,
    scripts = [
        'scripts/spearmint-lite.py'
    ]
)
