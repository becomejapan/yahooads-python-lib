"""Example code for
Service : SharedCriterionService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/SharedCriterionService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'SharedCriterionService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "sharedListIds": "1000", 
  "criterionIds": [
    "500", 
    "501"
  ], 
  "paging": {
    "startIndex": "500", 
    "numberResults": "2"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "SharedCriterionPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "sharedCriterion": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1000", 
          "criterionId": "501", 
          "text": "Sample Keyword", 
          "matchType": "EXACT", 
          "criterionUseType": "NEGATIVE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "sharedCriterion": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1000", 
          "criterionId": "500", 
          "text": "Sample Keyword", 
          "matchType": "PHRASE", 
          "criterionUseType": "NEGATIVE"
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
