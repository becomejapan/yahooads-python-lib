"""Example code for
Service : CampaignCriterionService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CampaignCriterionService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignCriterionService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "criterionIds": [
    "100000005", 
    "100000006", 
    "100000007"
  ], 
  "criterionUse": "NEGATIVE"
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "Page.Type": "CampaignCriterionPage", 
    "totalNumEntries": "2", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaignCriterion": {
          "xsi_type": "NegativeCampaignCriterion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "campaign name", 
          "criterionUse": "NEGATIVE", 
          "criterion": {
            "xsi_type": "Keyword", 
            "criterionId": "101010101", 
            "type": "KEYWORD", 
            "text": "keyword keyword2", 
            "matchType": "EXACT"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignCriterion": {
          "xsi_type": "NegativeCampaignCriterion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "criterionUse": "NEGATIVE", 
          "criterion": {
            "xsi_type": "Keyword", 
            "type": "KEYWORD", 
            "text": "yahoo bigkeyword2", 
            "matchType": "BROAD"
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
