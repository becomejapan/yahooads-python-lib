"""Utilities used by the client library."""

import logging
import re
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
