# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='richstr',
    version='1.0.0',
    description='Various templated __str__ methods',
    long_description=long_description,
    url='https://github.com/Kerl13/richstr',
    author='Martin Pépin',
    author_email='kerl@wkerl.me',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ],
    packages=find_packages(),
    install_requires=[],
)
