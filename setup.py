#!/usr/local/bin python3
from setuptools import setup, find_packages
from ptl.__main__ import __version__ as version
import shutil
import os
setup(name='ptl',
      python_requires='>=3.6',
      version=version,
      description='Automatically log time in GitLab issue tracker for COMP23311 at UoM.',
      url='https://github.com/JossMoff/ptl',
      author='Joss Moffatt',
      author_email='joss.moffatt@student.manchester.ac.uk',
      license='MIT',
      packages=find_packages(),
      data_files=[('ptl', ['ptl/config.ini'])],
      entry_points={
        'console_scripts': [
            'ptl = ptl.__main__:main']},
      zip_safe=False)
