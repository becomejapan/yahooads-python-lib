"""Example code for
Service : NegativeCampaignRetargetingListService
Operation: mutate(ADD)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/NegativeCampaignRetargetingListService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'NegativeCampaignRetargetingListService'
OPERATION = 'mutate(ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": {
    "accountId": "SAMPLE-ACCOUNT-ID", 
    "campaignId": "SAMPLE-CAMPAIN-ID", 
    "criterionTargetList": {
      "targetListId": "100000003"
    }
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "NegativeCampaignRetargetingListReturnValue", 
    "Operation.Type": "ADD", 
    "values": {
      "operationSucceeded": "true", 
      "negativeCampaignRetargetingList": {
        "accountId": "SAMPLE-ACCOUNT-ID", 
        "campaignId": "SAMPLE-CAMPAIN-ID", 
        "campaignName": "campaign name", 
        "criterionTargetList": {
          "targetListId": "1000000003", 
          "targetListName": "targetList name"
        }
      }
    }
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
