"""Example code for
Service : AccountService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AccountService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AccountService'
OPERATION = 'get'
OPERAND = {
  "accountIds": [
    "SAMPLE-ACCOUNT-ID"
  ], 
  "accountTypes": "PREPAY", 
  "paging": {
    "startIndex": "0", 
    "numberResults": "1"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "AccountPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "account": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "accountName": "XXXXXXXXXXXXXX", 
          "accountType": "INVOICE", 
          "accountStatus": "SERVING", 
          "deliveryStatus": "ACTIVE", 
          "budget": {
            "amount": "1000000", 
            "limitChargeType": "SUM", 
            "startDate": "20091130", 
            "endDate": "20100120"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "account": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "accountName": "XXXXXXXXXXXXXX", 
          "accountType": "INVOICE", 
          "accountStatus": "SERVING", 
          "deliveryStatus": "ACTIVE", 
          "budget": {
            "amount": "2000000", 
            "limitChargeType": "SUM", 
            "startDate": "20091031", 
            "endDate": "20100320"
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
