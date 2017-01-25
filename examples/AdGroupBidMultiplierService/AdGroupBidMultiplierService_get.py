"""Example code for
Service : AdGroupBidMultiplierService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AdGroupBidMultiplierService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupBidMultiplierService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "adGroupIds": [
    "SAMPLE-ADGROUP-ID"
  ], 
  "platformTypes": [
    "DESKTOP", 
    "TABLET", 
    "SMART_PHONE"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "20"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "6", 
    "Page.Type": "AdGroupBidMultiplierPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "adGroupBidMultiplier": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "platformType": "SMART_PHONE", 
          "bidMultiplier": "0.10"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupBidMultiplier": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "platformType": "TABLET", 
          "bidMultiplier": "0.50"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupBidMultiplier": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "platformType": "SMART_PHONE", 
          "bidMultiplier": "2"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupBidMultiplier": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "platformType": "DESKTOP", 
          "bidMultiplier": "1"
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