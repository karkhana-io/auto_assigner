from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in auto_assigner/__init__.py
from auto_assigner import __version__ as version

setup(
	name="auto_assigner",
	version=version,
	description="App to auto assign users to documents upon creation.",
	author="Karkhana.io",
	author_email="admin@karkhana.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
