"""Example code for
Service : AdGroupFeedService
Operation: mutate(SET)
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
OPERATION = 'mutate(SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "QUICKLINK", 
      "adGroupFeed": [
        {
          "feedItemId": "123"
        }, 
        {
          "feedItemId": "125"
        }
      ]
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "CALLEXTENSION", 
      "adGroupFeed": {
        "feedItemId": "117"
      }
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "QUICKLINK"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "CALLEXTENSION"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "QUICKLINK", 
      "devicePlatform": "DESKTOP"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "QUICKLINK", 
      "devicePlatform": "SMART_PHONE"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "placeholderType": "QUICKLINK", 
      "devicePlatform": "NONE"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AdGroupFeedReturnValue", 
    "Operation.Type": "SET", 
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
          ]
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
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "CALLEXTENSION"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "QUICKLINK"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "QUICKLINK", 
          "adGroupFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "adGroupId": "SAMPLE-ADGROUP-ID", 
            "feedItemId": "123", 
            "placeholderType": "QUICKLINK"
          }, 
          "devicePlatform": "DESKTOP"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "QUICKLINK", 
          "adGroupFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "adGroupId": "SAMPLE-ADGROUP-ID", 
            "feedItemId": "123", 
            "placeholderType": "QUICKLINK"
          }, 
          "devicePlatform": "SMART_PHONE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "placeholderType": "QUICKLINK", 
          "adGroupFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "adGroupId": "SAMPLE-ADGROUP-ID", 
            "feedItemId": "123", 
            "placeholderType": "QUICKLINK"
          }, 
          "devicePlatform": "NONE"
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