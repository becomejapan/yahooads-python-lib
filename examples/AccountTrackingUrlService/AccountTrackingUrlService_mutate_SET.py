"""Example code for
Service : AccountTrackingUrlService
Operation: mutate(SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AccountTrackingUrlService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AccountTrackingUrlService'
OPERATION = 'mutate(SET)'
OPERAND = {
  "operator": "SET", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "trackingUrl": "http://www.xxxxx.com/?url={lpurl}&id=2"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "trackingUrl": ""
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AccountTrackingUrlReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "operationSucceeded": "true", 
        "accountTrackingUrl": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "accountName": "XXXXXXXXXXXXXX", 
          "trackingUrl": "http://www.xxxxx.com/?url={lpurl}&id=1", 
          "inReviewUrl": "http://www.xxxxx.com/?url={lpurl}&id=2", 
          "urlApprovalStatus": "APPROVED_WITH_REVIEW"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "accountTrackingUrl": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "accountName": "XXXXXXXXXXXXXX"
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