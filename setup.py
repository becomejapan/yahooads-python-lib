#!/usr/bin/python

import os
import re
import sys
from setuptools import setup

from yahooads import common

PACKAGES = ['yahooads']

DEPENDENCIES = ['httplib2>=0.9.2', 'suds-jurko>=0.6', 'PyYAML>=3.11',
                'xmltodict>=0.10.2', 'argparse>=1.1']

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 2.7',
]

extra_params = {}
if sys.version_info[0] == 3:
  extra_params['use_2to3'] = True

setup(name='yahooads',
      version=common.VERSION,
      description='Yahoo Promotional Ads Python Client Library',
      author='Chammika Mannakkara',
      author_email='chammika@become.co.jp',
      url='https://github.com/becomejapan/promotionalads-python-lib',
      license='Apache License 2.0',
      packages=PACKAGES,
      platforms='any',
      keywords='yahoo promotionalads API client',
      classifiers=CLASSIFIERS,
      install_requires=DEPENDENCIES,
      **extra_params)
