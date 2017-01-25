"""Example code for
Service : AdGroupFeedService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AdGroupFeedService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupFeedService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "adGroupIds": [
    "SAMPLE-ADGROUP-ID"
  ], 
  "feedItemIds": [
    "12", 
    "13"
  ], 
  "placeholderTypes": [
    "QUICKLINK", 
    "CALLEXTENSION"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "20"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "AdGroupFeedPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "QUICKLINK", 
          "adGroupFeed": [
            {
              "accountId": "SAMPLE-ACCOUNT-ID", 
              "campaignId": "SAMPLE-CAMPAIN-ID", 
              "adGroupId": "SAMPLE-ADGROUP-ID", 
              "feedItemId": "123", 
              "placeholderType": "QUICKLINK"
            }, 
            {
              "accountId": "SAMPLE-ACCOUNT-ID", 
              "campaignId": "SAMPLE-CAMPAIN-ID", 
              "adGroupId": "SAMPLE-ADGROUP-ID", 
              "feedItemId": "125", 
              "placeholderType": "QUICKLINK"
            }
          ], 
          "devicePlatform": "DESKTOP"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "CALLEXTENSION", 
          "adGroupFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "adGroupId": "SAMPLE-ADGROUP-ID", 
            "feedItemId": "117", 
            "placeholderType": "CALLEXTENSION"
          }, 
          "devicePlatform": "SMART_PHONE"
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
