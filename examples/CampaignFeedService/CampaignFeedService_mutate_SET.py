"""Example code for
Service : CampaignFeedService
Operation: mutate(SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CampaignFeedService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignFeedService'
OPERATION = 'mutate(SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "QUICKLINK", 
      "campaignFeed": [
        {
          "feedItemId": "113"
        }, 
        {
          "feedItemId": "115"
        }
      ]
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "CALLEXTENSION", 
      "campaignFeed": {
        "feedItemId": "113"
      }
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "QUICKLINK"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "CALLEXTENSION"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "QUICKLINK", 
      "campaignFeed": {
        "feedItemId": "113"
      }, 
      "devicePlatform": "DESKTOP"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "QUICKLINK", 
      "campaignFeed": {
        "feedItemId": "113"
      }, 
      "devicePlatform": "SMART_PHONE"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "placeholderType": "QUICKLINK", 
      "campaignFeed": {
        "feedItemId": "113"
      }, 
      "devicePlatform": "NONE"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "CampaignFeedReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "QUICKLINK", 
          "campaignFeed": [
            {
              "accountId": "SAMPLE-ACCOUNT-ID", 
              "campaignId": "SAMPLE-CAMPAIN-ID", 
              "feedItemId": "113", 
              "placeholderType": "QUICKLINK"
            }, 
            {
              "accountId": "SAMPLE-ACCOUNT-ID", 
              "campaignId": "SAMPLE-CAMPAIN-ID", 
              "feedItemId": "114", 
              "placeholderType": "QUICKLINK"
            }
          ], 
          "devicePlatform": "DESKTOP"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "CALLEXTENSION", 
          "campaignFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "feedItemId": "115", 
            "placeholderType": "CALLEXTENSION"
          }, 
          "devicePlatform": "DESKTOP"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "CALLEXTENSION", 
          "devicePlatform": "SMART_PHONE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "QUICKLINK", 
          "devicePlatform": "SMART_PHONE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "QUICKLINK", 
          "devicePlatform": "DESKTOP", 
          "campaignFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "feedItemId": "113", 
            "placeholderType": "QUICKLINK"
          }
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
