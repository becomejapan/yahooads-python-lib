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

"""Suds based Client library for the Yahoo PromotionalAds API."""
# noinspection PyPackageRequirements
import yaml
import os
import json
import logging

import common
import errors

# noinspection PyPackageRequirements
from suds.client import Client
# noinspection PyPackageRequirements
from suds.sax.element import Element

# API version supported by the this Client library
PROMOTIONALADS_API_VERSION = '6.5'

# Service Locations
DEFAULT_SERVICE_LOCATION = 'ss.yahooapis.jp'
SANDBOX_SERVICE_LOCATION = 'sandbox.ss.yahooapis.jp'

# URL formats for service end points and WSDL service definition files
ENDPOINT_URL = 'https://{location}/services/V{api_version}/{service_name}'
WSDL_URL = ENDPOINT_URL + '?wsdl'

# Parameters for API requests
REQUIRED_PARAMETERS = ('api_license', 'api_account_id', 'api_account_pass')
OPTIONAL_PARAMETERS = {
    # 'parameter': default-value
    'on_behalf_account_id': None,
    'on_behalf_account_pass': None,
    'account_id': None,             # optional only in non-production environments i.e. must provide if sandbox=False
                                    #   account_id is required to obtain the URL prefix for the co-location of account
    'sandbox': False,               # whether to use sandbox
    'location_cache': None,         # cache of service-locations for client-customer-id(s)
    'context': None,                # operating context of client defined by parameters
                                    # accountId, campaignId, adgroupId etc.
                                    # use for auto-filling operands in example code
}


class PromotionalAdsClient(object):
    """Class to hold credentials and generate web service clients for all API services
    Required Parameters: credential that goes into <RequestHeader>
        api_license :
        api_account_id:
        api_account_pass:
    Optional Parameters:
        on_behalf_account_id:
        on_behalf_account_pass:
        account_id:
        sandbox:
        location_cache:
    """
    # Default upload_config file & key where the parameters for instantiating the PromotionalAdsClient object resides
    _CONFIG_FILE = os.path.join(os.path.expanduser('~'), 'yahooads.yaml')
    _PARAMETERS_KEY = 'promotionalads'

    def __init__(self, api_license, api_account_id, api_account_pass, **kwargs):
        self.api_license = api_license
        self.api_account_id = api_account_id
        self.api_account_pass = api_account_pass
        # Flowing is to avoid pesky warnings (unresolved references) in PyCharm actual settings follows
        self.on_behalf_account_id = None
        self.on_behalf_account_pass = None
        self.account_id = None
        self.sandbox = False
        self.location_cache = None
        self.context = None
        for param, default_value in OPTIONAL_PARAMETERS.items():
            setattr(self, param, kwargs.get(param, default_value))

        # Parameter checks
        if not api_license or not api_account_id or not api_account_pass:
            raise errors.CredentialsError("Incomplete parameters: provide {}".format(REQUIRED_PARAMETERS))
        if bool(self.on_behalf_account_id) ^ bool(self.on_behalf_account_pass):
            raise errors.CredentialsError("Incomplete on-behalf parameters: "
                                          "provide [ on_behalf_account_id, on_behalf_account_pass ]")
        if self.on_behalf_account_id and self.sandbox:
            raise errors.CredentialsError("Cannot use on-behalf account with sandbox")
        if not self.account_id and not self.sandbox:
            raise errors.CredentialsError("Requires 'account_id' to obtain service end-point in production")
        extra_params = set(kwargs.keys()) - set(OPTIONAL_PARAMETERS.keys())
        if extra_params:
            logging.warn("Extra parameters ignored : {}".format(extra_params))
        # set service location
        self.service_location = self._get_service_location()

    def setAccountId(self, account_id):
        self.account_id = account_id
        self.service_location = self._get_service_location()  # Update service location for new account

    def GetService(self, service_name, version=PROMOTIONALADS_API_VERSION):
        try:
            header = self._get_soap_header()
            wsdl_url = WSDL_URL.format(location=DEFAULT_SERVICE_LOCATION, api_version=version,
                                       service_name=service_name)
            endpoint_url = ENDPOINT_URL.format(location=self.service_location, api_version=version,
                                               service_name=service_name)
            suds_client = Client(wsdl_url, soapheaders=[header], location=endpoint_url)
            # Pass optional parameters to suds_client
            for param in OPTIONAL_PARAMETERS.keys():
                setattr(suds_client, param, getattr(self, param))
            return common.SudsServiceProxy(suds_client)
        except Exception as e:
            raise errors.ServiceInitializationError(e)

    @classmethod
    def LoadFromConfiguration(cls, config_file=_CONFIG_FILE, key=_PARAMETERS_KEY):
        try:
            config_data = yaml.safe_load(open(config_file))
            parameters = config_data[key]
            if set(REQUIRED_PARAMETERS).issubset(parameters.keys()):
                api_license, api_account_id, api_account_pass = (parameters[c] for c in REQUIRED_PARAMETERS)
                map(parameters.pop, REQUIRED_PARAMETERS)  # Remove required parameters from kwargs
                return cls(api_license, api_account_id, api_account_pass, **parameters)
            else:
                raise errors.CredentialsError("Incomplete parameters: provide {}".format(REQUIRED_PARAMETERS))
        except Exception as e:
            raise errors.CredentialsError("Error loading parameters from file '{}' @ key '{}'\n"
                                          "Error {}".format(config_file, key, e))

    def _get_soap_header(self):
        header = Element('RequestHeader') \
            .append(Element('license').setText(self.api_license)) \
            .append(Element('apiAccountId').setText(self.api_account_id)) \
            .append(Element('apiAccountPassword').setText(self.api_account_pass))
        if self.on_behalf_account_id:
            header.append(Element('onBehalfOfAccountId').setText(self.on_behalf_account_id)) \
                .append(Element('onBehalfOfPassword').setText(self.on_behalf_account_pass))
        return header

    def _get_service_location(self):
        if self.sandbox:
            return SANDBOX_SERVICE_LOCATION
        else:
            if self.location_cache:  # get service location from cache (if present) or LocationService
                location_dict = {}
                try:
                    with open(self.location_cache) as cf:
                        location_dict = json.load(cf)
                    return location_dict[str(self.account_id)]
                except (KeyError, Exception):
                    # account co-location not in cache, empty cache, or error reading cache-file
                    # Get location from API and save in cache
                    location = self._get_service_location_from_API()
                    location_dict[self.account_id] = location
                    try:
                        with open(self.location_cache, 'w') as cf:
                            json.dump(location_dict, cf, indent=4)
                    except Exception as e:
                        raise errors.ServiceLocationError("Couldn't save service location in cache '{}'\n"""
                                                          "Error {}".format(self.location_cache, e))
                    return location
            else:  # No caching get location form API
                return self._get_service_location_from_API()

    def _get_service_location_from_API(self):
        try:
            header = self._get_soap_header()
            wsdl_url = WSDL_URL.format(location=DEFAULT_SERVICE_LOCATION, api_version=PROMOTIONALADS_API_VERSION,
                                       service_name='LocationService')
            suds_client = Client(wsdl_url, soapheaders=[header])
            res = suds_client.service.get(self.account_id)
            if res.rval.operationSucceeded:
                return res.rval.value
            else:
                raise Exception("Failed get service location for '{}'".format(self.account_id))
        except Exception as e:
            raise errors.ServiceLocationError(e)
