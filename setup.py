from distutils.core import setup
from setuptools import find_namespace_packages

with open('README.md') as file: 
    readme = file.read()
    
with open('requirements.txt') as file: 
    install_requires = file.readlines()

setup( 
    name='watcher',
    version='0.1',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=install_requires,
    url='',
    license='LICENSE.txt',
    description='',
    long_description=readme,
    author='Perry',
    author_email='perryism@gmail.com'
)