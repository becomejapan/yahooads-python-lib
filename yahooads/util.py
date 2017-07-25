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

"""Utilities used by the client library."""

import logging
import re
# noinspection PyPackageRequirements
import suds


class _CredentialsFilter(logging.Filter):
    """Filter credentials from SOAP message
    """
    _CREDENTIALS_PAT = re.compile(r"""(?<=<license>).*?(?=</license>)                        # match license
                                     |(?<=<apiAccountId>).*?(?=</apiAccountId>)              # match account id
                                     |(?<=<apiAccountPassword>).*?(?=</apiAccountPassword>)  # match account password
                               """, re.VERBOSE)
    _OMITTED = 'OMITTED'
    _SUDS_CLIENT_SOAP_MSG = 'sending to (%s)\nmessage:\n%s'

    def filter_str(self, msg_str):
        msg_str = self._CREDENTIALS_PAT.sub(self._OMITTED, msg_str)
        return msg_str


def singleton(cls):
    return cls()


@singleton
class SudsCredentialsFilter(_CredentialsFilter):
    """Filter credentials form suds client SOAP messages
    """
    def filter(self, record):
        if record.msg == self._SUDS_CLIENT_SOAP_MSG:
            args = record.args
            record.args = (args[0],  self.filter_str(args[1].str()))
        return True


@singleton
class TransportCredentialsFilter(_CredentialsFilter):
    """Filter credentials from suds transport messages
    """
    def filter(self, record):
        if record.args:
            arg = record.args[0]
            if isinstance(arg, suds.transport.Request):
                new_arg = suds.transport.Request(arg.url)
                new_arg.message = self.filter_str(arg.message.decode('utf-8'))
                record.args = (new_arg,)
        return True
