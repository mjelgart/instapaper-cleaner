"""
setuptools based setup module for instapaper-cleaner.

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

desc = """\
Description
==============

Cleans out old unread instapaper articles from same website.
"""

setup(
    name='instapaper-cleaner',
    version='0.2.1',
    
    description = 'Cleans out old unread instapaper articles from same website.',
    long_description=long_description,
     
    author='Michael Elgart',
    url='https://github.com/mjelgart/instapaper-cleaner',

    license='Apache',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Hobbyists',
        'License :: OSI Approved :: Apache License',

        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='instapaper automation cleaning',

    py_modules=["cleaner"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['instapaper']
    
   )

