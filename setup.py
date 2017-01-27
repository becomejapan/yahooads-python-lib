# Copyright 2017 Become Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
