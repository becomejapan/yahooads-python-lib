"""Example code for
Service : AccountSharedService
Operation: mutate(SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AccountSharedService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AccountSharedService'
OPERATION = 'mutate(SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "sharedListId": "1000", 
      "name": "modify Sample Shared List No1"
    }, 
    {
      "sharedListId": "1001", 
      "name": "modify Sample Shared List No2"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AccountSharedReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "operationSucceeded": "true", 
        "accountShared": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1000", 
          "name": "modify Sample Shared List No1", 
          "memberCount": "1000", 
          "referenceCount": "0"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "accountShared": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "sharedListId": "1001", 
          "name": "modify Sample Shared List No2", 
          "memberCount": "200", 
          "referenceCount": "1"
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
