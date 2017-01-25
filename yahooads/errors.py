
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
