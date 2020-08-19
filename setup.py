#!/usr/bin/env python
"""pyjenkins setup script"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

setup(name='pygit',
      version=__import__('pygit').__version__,
      description='pygit is a thiner wrapper around git to provide a custom git opprations',
      author='Chengkai Liang',
      author_email='chengkai.liang@bigfishgames.com',
      install_requires=['funcy', 'sh'],
      packages=find_packages(),
      entry_points = {
          'console_scripts': [
              'git-cmd = pygit.cli.main:git'
              ],
          },
      classifiers=[
           "Programming Language :: Python",
           "Development Status :: 1 - alpha",
           "Environment :: Console",
           "Intended Audience :: Developers",
           "License :: OSI Approved :: Apache Software License",
           "Operating System :: OS Independent",
           'Topic :: System :: Systems Administration',
      ]
)
