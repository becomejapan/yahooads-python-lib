"""Example code for
Service : CampaignSharedSetService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CampaignSharedSetService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignSharedSetService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "sharedListIds": [
    "1000", 
    "1001"
  ], 
  "paging": {
    "startIndex": "4", 
    "numberResults": "100"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "CampaignSharedSetPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaignSharedSet": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1000", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "sharedListName": "Sample SharedList No1", 
          "campaignName": "Sample Campaign No3"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignSharedSet": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1001", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "sharedListName": "Sample SharedList No2", 
          "campaignName": "Sample Campaign No2"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignSharedSet": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1001", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "sharedListName": "Sample SharedList No2", 
          "campaignName": "Sample Campaign No1"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignSharedSet": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1000", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "sharedListName": "Sample SharedList No1", 
          "campaignName": "Sample Campaign No1"
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
