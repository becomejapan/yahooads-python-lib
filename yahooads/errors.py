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

"""Errors used by the Yahoo Promotional Ads Client Library."""


class YahooAdsError(Exception):
    """Base error class"""
    pass


class WebFaultError(YahooAdsError):
    """"Wrapper for error thrown by the web service"""
    pass

class ServiceLocationError(YahooAdsError):
    """"Error in LocationService when requesting service end-point"""
    pass


class CredentialsError(YahooAdsError):
    """"Error in Credentials"""
    pass


class ServiceInitializationError(YahooAdsError):
    """"Error in Initializing service client"""
    pass
