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

"""Suds utility functions from googleads-python-lib"""

import logging
import suds
from suds import sudsobject
from collections import OrderedDict

import util
import errors

# Log filters
logging.getLogger('suds.client').addFilter(util.SudsCredentialsFilter)
logging.getLogger('suds.transport.http').addFilter(util.TransportCredentialsFilter)

# version of this client library
VERSION = '0.0.1'


class SudsServiceProxy(object):
    def __init__(self, suds_client):
        self.suds_client = suds_client
        self._method_proxies = {}

    def __getattr__(self, attr):
        if attr in self.suds_client.wsdl.services[0].ports[0].methods:
            if attr not in self._method_proxies:
                self._method_proxies[attr] = self._CreateMethod(attr)
            return self._method_proxies[attr]
        else:
            return getattr(self.suds_client.service, attr)

    def _CreateMethod(self, method_name):
        soap_service_method = getattr(self.suds_client.service, method_name)

        def MakeSoapRequest(*args):
            """Perform a SOAP call."""
            # Don't set headers from each method
            # self._header_handler.SetHeaders(self.suds_client)
            try:
                return soap_service_method(*[_PackForSuds(arg, self.suds_client.factory) for arg in args])
            except Exception as e:
                raise errors.WebFaultError("Server raised fault in response.\n"
                                           "Failure response:\n{}".format(e))
        return MakeSoapRequest


def _PackForSuds(obj, factory):
    """Packs SOAP input into the format we want for suds.

    The main goal here is to pack dictionaries with an 'xsi_type' key into
    objects. This allows dictionary syntax to be used even with complex types
    extending other complex types. The contents of dictionaries and lists/tuples
    are recursively packed. Mutable types are copied - we don't mutate the input.

    Args:
    obj: A parameter for a SOAP request which will be packed. If this is
        a dictionary or list, the contents will recursively be packed. If this
        is not a dictionary or list, the contents will be recursively searched
        for instances of unpacked dictionaries or lists.
    factory: The suds.client.Factory object which can create instances of the
        classes generated from the WSDL.
    Returns:
        If the given obj was a dictionary that contained the 'xsi_type' key, this
        will be an instance of a class generated from the WSDL. Otherwise, this will
        be the same data type as the input obj was.
    """

    if obj in ({}, None):
        # Force suds to serialize empty objects. There are legitimate use cases for
        # this, for example passing in an empty SearchCriteria object to a DFA
        # search method in order to select everything.
        return suds.null()
    elif isinstance(obj, dict):
        if 'xsi_type' in obj:
            try:
                new_obj = factory.create(obj['xsi_type'])
            except suds.TypeNotFound:
                new_obj = factory.create(':'.join(['ns0', obj['xsi_type']]))
            # Suds sends an empty XML element for enum types which are not set. None
            # of Google's Ads APIs will accept this. Initializing all of the fields in
            # a suds object to None will ensure that they don't get serialized at all
            # unless the user sets a value. User values explicitly set to None will be
            # packed into a suds.null() object.
            for param, _ in new_obj:
                # Another problem is that the suds.mx.appender.ObjectAppender won't
                #  serialize object types with no fields set, but both AdWords and DFP
                # rely on sending objects with just the xsi:type set. The below "if"
                # statement is an ugly hack that gets this to work in all(?) situations
                # by taking advantage of the fact that these classes generally all have
                # a type field. The only other option is to monkey patch ObjectAppender.
                if param.endswith('.Type'):
                    setattr(new_obj, param, obj['xsi_type'])
                else:
                    setattr(new_obj, param, None)
            for key in obj:
                if key == 'xsi_type':
                    continue
                setattr(new_obj, key, _PackForSuds(obj[key], factory))
        else:
            new_obj = {}
            for key in obj:
                new_obj[key] = _PackForSuds(obj[key], factory)
        return new_obj
    elif isinstance(obj, (list, tuple)):
        return [_PackForSuds(item, factory) for item in obj]
    else:
        _RecurseOverObject(obj, factory)
        return obj


def _RecurseOverObject(obj, factory, parent=None):
    """Recurses over a nested structure to look for changes in Suds objects.

    Args:
      obj: A parameter for a SOAP request field which is to be inspected and
          will be packed for Suds if an xsi_type is specified, otherwise will be
          left unaltered.
      factory: The suds.client.Factory object which can create instances of the
          classes generated from the WSDL.
      parent: The parent object that contains the obj parameter to be inspected.
    """

    if _IsSudsIterable(obj):
        # Since in-place modification of the Suds object is taking place, the
        # iterator should be done over a frozen copy of the unpacked fields.
        copy_of_obj = tuple(obj)
        for item in copy_of_obj:
            if _IsSudsIterable(item):
                if 'xsi_type' in item:
                    if isinstance(obj, tuple):
                        parent[obj[0]] = _PackForSuds(obj[1], factory)
                    else:
                        obj.remove(item)
                        obj.append(_PackForSuds(item, factory))
                _RecurseOverObject(item, factory, obj)


def _IsSudsIterable(obj):
    """A short helper method to determine if a field is iterable for Suds."""
    return obj and not isinstance(obj, basestring) and hasattr(obj, '__iter__')


def _UnpackFromSuds(obj):
    """Packs SOAP responses from suds to dict (OrderedDict to preserve readability)
    Note: This method does NOT mirror the _PackForSuds() method. Especially handling of
          complex data object 'xsi_type' tagging. Only be expected to apply for SOAP
          responses received for testing purposes.
    """
    out = OrderedDict()
    for k, v in sudsobject.items(obj):
        if hasattr(v, '__keylist__'):
            out[k] = _UnpackFromSuds(v)
        elif isinstance(v, list):
            out[k] = []
            for item in v:
                if hasattr(item, '__keylist__'):
                    out[k].append(_UnpackFromSuds(item))
                else:
                    out[k].append(item)
        else:
            out[k] = v
    return out
