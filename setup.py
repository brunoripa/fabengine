#!/usr/bin/env python

from setuptools import setup

import os
def read(fname):
     return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='fabengine',
     version='0.0.11',
     description='Fabric commands for appengine.',
     long_description=read('README.md'),
     author='Chris Targett',
     author_email='chris@xlevus.net',
     url='http://github.com/xlevus/fabengine',
     py_modules = ['fabengine'],
     install_requires = [
          'Fabric>=1.4.3',
          'nose>=1.1.2',
          'NoseGAE>=0.2.0',
          'wheel>=0.22.0',
          'pip>=1.5.2',
     ],
     classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Environment :: Console",
          "Topic :: Software Development",
          "Topic :: System :: Software Distribution",
     ],
     keywords='fabric appengine deployment',
     license='',

)
