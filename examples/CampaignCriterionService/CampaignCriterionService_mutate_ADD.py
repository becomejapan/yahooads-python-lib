"""Example code for
Service : CampaignCriterionService
Operation: mutate (ADD)
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
OPERATION = 'mutate (ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignId": "SAMPLE-CAMPAIN-ID", 
  "criterionUse": "NEGATIVE", 
  "operand": [
    {
      "xsi_type": "NegativeCampaignCriterion", 
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "criterionUse": "NEGATIVE", 
      "criterion": {
        "xsi_type": "Keyword", 
        "type": "KEYWORD", 
        "text": "yahoo bigkeyword1", 
        "matchType": "BROAD"
      }
    }, 
    {
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
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "CampaignCriterionReturnValue", 
    "Operation.Type": "ADD", 
    "values": [
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
            "text": "yahoo bigkeyword1", 
            "matchType": "BROAD"
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
