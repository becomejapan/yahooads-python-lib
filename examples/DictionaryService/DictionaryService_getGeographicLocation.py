"""Example code for
Service : DictionaryService
Operation: getGeographicLocation
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/DictionaryService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'DictionaryService'
OPERATION = 'getGeographicLocation'
OPERAND = {
  "lang": "JA"
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "47", 
    "Page.Type": "GeographicLocationPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "geographicLocation": {
          "code": "JP-01", 
          "name": "\u5317\u6d77\u9053", 
          "fullName": "\u5317\u6d77\u9053", 
          "order": "0000000000", 
          "status": "ACTIVE", 
          "child": [
            {
              "code": "JP-01-0003", 
              "parent": "JP-01", 
              "name": "\u65ed\u5ddd\u5e02", 
              "fullName": "\u5317\u6d77\u9053 \u65ed\u5ddd\u5e02", 
              "order": "0000000100", 
              "status": "ACTIVE"
            }, 
            {
              "code": "JP-01-0005", 
              "parent": "JP-01", 
              "name": "\u82a6\u5225\u5e02", 
              "fullName": "\u5317\u6d77\u9053 \u82a6\u5225\u5e02", 
              "order": "0000000200", 
              "status": "ACTIVE"
            }, 
            {
              "code": "JP-01-0052", 
              "parent": "JP-01", 
              "name": "\u672d\u5e4c\u5e02", 
              "fullName": "\u5317\u6d77\u9053 \u672d\u5e4c\u5e02", 
              "order": "0000002500", 
              "status": "ACTIVE"
            }
          ]
        }
      }, 
      {
        "operationSucceeded": "true", 
        "geographicLocation": {
          "code": "JP-02", 
          "name": "\u9752\u68ee\u770c", 
          "fullName": "\u9752\u68ee\u770c", 
          "order": "0100000000", 
          "status": "ACTIVE", 
          "child": [
            {
              "code": "JP-02-0002", 
              "parent": "JP-02", 
              "name": "\u9752\u68ee\u5e02", 
              "fullName": "\u9752\u68ee\u770c \u9752\u68ee\u5e02", 
              "order": "0100000100", 
              "status": "ACTIVE"
            }, 
            {
              "code": "JP-02-0004", 
              "parent": "JP-02", 
              "name": "\u516b\u6238\u5e02", 
              "fullName": "\u9752\u68ee\u770c \u516b\u6238\u5e02", 
              "order": "0100000700", 
              "status": "ACTIVE"
            }
          ]
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