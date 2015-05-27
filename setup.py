from setuptools import find_packages
from setuptools import setup

setup(
    name='pbs-zencoder',
    version='0.4.1',
    description='Integration library for Zencoder',
    author='Alex Schworer',
    author_email='alex.schworer@gmail.com',
    url='http://github.com/schworer/zencoder-py',
    license="MIT License",
    install_requires=['httplib2'],
    packages=find_packages(),
    include_package_data=True,
)
