"""Example code for
Service : FeedFolderService
Operation: mutate(REMOVE)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/FeedFolderService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'FeedFolderService'
OPERATION = 'mutate(REMOVE)'
OPERAND = {
  "operator": "REMOVE", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": {
    "accountId": "SAMPLE-ACCOUNT-ID", 
    "feedFolderId": "100000001"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "FeedFolderReturnValue", 
    "Operation.Type": "REMOVE", 
    "values": {
      "operationSucceeded": "true", 
      "feedFolder": {
        "accountId": "SAMPLE-ACCOUNT-ID", 
        "feedFolderId": "113", 
        "feedFolderName": "myfeedname", 
        "placeholderType": "AD_CUSTOMIZER", 
        "feedAttribute": [
          {
            "feedAttributeId": "2000000001", 
            "feedAttributeName": "myfeedattname1", 
            "placeholderField": "AD_CUSTOMIZER_INTEGER"
          }, 
          {
            "feedAttributeId": "2000000002", 
            "feedAttributeName": "myfeedattname2", 
            "placeholderField": "AD_CUSTOMIZER_PRICE"
          }
        ]
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