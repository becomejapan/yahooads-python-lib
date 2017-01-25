"""Example code for
Service : ConversionTrackerService
Operation: mutate (ADD)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/ConversionTrackerService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'ConversionTrackerService'
OPERATION = 'mutate (ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "xsi_type": "WebConversion", 
      "conversionTrackerName": "WEB_CONVERSION_TRACKER", 
      "status": "ENABLED", 
      "category": "PAGE_VIEW", 
      "conversionTrackerType": "WEB_CONVERSION", 
      "userRevenueValue": "100", 
      "countingType": "MANY_PER_CLICK", 
      "markupLanguage": "HTML", 
      "trackingCodeType": "WEBPAGE"
    }, 
    {
      "xsi_type": "WebConversion", 
      "conversionTrackerName": "CALL_CONVERSION_TRACKER", 
      "status": "DISABLED", 
      "category": "DEFAULT", 
      "conversionTrackerType": "WEB_CONVERSION", 
      "userRevenueValue": "200", 
      "countingType": "MANY_PER_CLICK", 
      "measurementPeriod": "10", 
      "markupLanguage": "HTML", 
      "trackingCodeType": "CLICK_TO_CALL"
    }, 
    {
      "xsi_type": "AppConversion", 
      "conversionTrackerName": "APP_ANDROID_DOWNLOAD_CONVERSION_TRACKER", 
      "status": "ENABLED", 
      "category": "DOWNLOAD", 
      "conversionTrackerType": "APP_CONVERSION", 
      "userRevenueValue": "100", 
      "countingType": "ONE_PER_CLICK", 
      "appId": "abc_1234", 
      "appPlatform": "ANDROID_MARKET", 
      "appConversionType": "DOWNLOAD"
    }, 
    {
      "xsi_type": "AppConversion", 
      "conversionTrackerName": "APP_ANDROID_FIRST_OPEN_CONVERSION_TRACKER", 
      "status": "ENABLED", 
      "category": "DOWNLOAD", 
      "conversionTrackerType": "APP_CONVERSION", 
      "userRevenueValue": "100", 
      "countingType": "ONE_PER_CLICK", 
      "excludeFromBidding": "TRUE", 
      "appId": "abc_1234", 
      "appPlatform": "ANDROID_MARKET", 
      "appConversionType": "FIRST_OPEN", 
      "appPostbackUrl": {
        "url": "http://yahoo.co.jp?advertising_id={adid}&lat={lat}"
      }
    }, 
    {
      "xsi_type": "AppConversion", 
      "conversionTrackerName": "APP_ANDROID_IN_APP_PURCHASE_CONVERSION_TRACKER", 
      "status": "ENABLED", 
      "category": "DEFAULT", 
      "conversionTrackerType": "APP_CONVERSION", 
      "userRevenueValue": "100", 
      "countingType": "MANY_PER_CLICK", 
      "measurementPeriod": "7", 
      "appPlatform": "ANDROID_MARKET", 
      "appConversionType": "IN_APP_PURCHASE"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "ConversionTrackerReturnValue", 
    "Operation.Type": "ADD", 
    "values": [
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "WebConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193194", 
          "conversionTrackerName": "WEB_CONVERSION_TRACKER", 
          "status": "ENABLED", 
          "category": "PAGE_VIEW", 
          "conversionTrackerType": "WEB_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "MANY_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "30", 
          "markupLanguage": "HTML", 
          "trackingCodeType": "WEBPAGE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "WebConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193195", 
          "conversionTrackerName": "CALL_CONVERSION_TRACKER", 
          "status": "DISABLED", 
          "category": "DEFAULT", 
          "conversionTrackerType": "WEB_CONVERSION", 
          "userRevenueValue": "200", 
          "countingType": "MANY_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "10", 
          "markupLanguage": "HTML", 
          "trackingCodeType": "CLICK_TO_CALL"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "AppConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193196", 
          "conversionTrackerName": "APP_ANDROID_DOWNLOAD_CONVERSION_TRACKER", 
          "status": "ENABLED", 
          "category": "DOWNLOAD", 
          "conversionTrackerType": "APP_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "ONE_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "30", 
          "appId": "abc_1234", 
          "appPlatform": "ANDROID_MARKET", 
          "appConversionType": "DOWNLOAD", 
          "appPostbackUrl": ""
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "AppConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193197", 
          "conversionTrackerName": "APP_ANDROID_FIRST_OPEN_CONVERSION_TRACKER", 
          "status": "ENABLED", 
          "category": "DOWNLOAD", 
          "conversionTrackerType": "APP_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "ONE_PER_CLICK", 
          "excludeFromBidding": "TRUE", 
          "measurementPeriod": "30", 
          "appId": "abc_1234", 
          "appPlatform": "ANDROID_MARKET", 
          "appConversionType": "FIRST_OPEN", 
          "appPostbackUrl": {
            "url": "http://yahoo.co.jp?advertising_id={adid}&lat={lat}"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "AppConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193198", 
          "conversionTrackerName": "APP_ANDROID_IN_APP_PURCHASE_CONVERSION_TRACKER", 
          "status": "ENABLED", 
          "category": "DEFAULT", 
          "conversionTrackerType": "APP_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "MANY_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "7", 
          "appPlatform": "ANDROID_MARKET", 
          "appConversionType": "IN_APP_PURCHASE", 
          "appPostbackUrl": ""
        }
      }
    ]
  }
}
"""


def main():
    client = promotionalads.PromotionalAdsClient.LoadFromConfiguration()
    service = client.GetService(SERVICE)
    print("REQUEST : {}.{}\n{}".format(SERVICE, OPERATION, json.dumps(OPERAND, indent=2)))
    try:
        if OPERATION == "get":
            response = service.get(OPERAND)
        elif OPERATION.startswith("get"):
            get_method = getattr(service, OPERATION)
            response = get_method(OPERAND)
        elif OPERATION.startswith("mutate"):
            response = service.mutate(OPERAND)
        else:
            raise("Unknown Operation '{}'".format(OPERATION))
        print("RESPONSE :\n{}".format(response))
    except Exception as e:
        print("Exception at '{}' operations \n{}".format(SERVICE, e))
        raise e


if __name__ == '__main__':
    main()