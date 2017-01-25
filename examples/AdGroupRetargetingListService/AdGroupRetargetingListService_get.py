"""Example code for
Service : AdGroupRetargetingListService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AdGroupRetargetingListService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupRetargetingListService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "targetListIds": "100000003", 
  "adGroupIds": [
    "SAMPLE-ADGROUP-ID"
  ], 
  "excludedType": "INCLUDED"
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "AdGroupRetargetingListPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "adGroupRetargetingList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "SampleCampaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupName": "SampleAdGroup1", 
          "criterionTargetList": {
            "targetListId": "100000005", 
            "targetListName": "Default List"
          }, 
          "excludedType": "EXCLUDED"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupRetargetingList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "SampleCampaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupName": "SampleAdGroup2", 
          "criterionTargetList": {
            "targetListId": "100000005", 
            "targetListName": "Default List"
          }, 
          "excludedType": "INCLUDED", 
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
