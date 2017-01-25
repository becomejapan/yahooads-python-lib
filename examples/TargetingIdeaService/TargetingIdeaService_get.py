"""Example code for
Service : TargetingIdeaService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/TargetingIdeaService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'TargetingIdeaService'
OPERATION = 'get'
OPERAND = {
  "searchParameter": [
    {
      "xsi_type": "RelatedToKeywordSearchParameter", 
      "searchParameterUse": "RELATED_TO_KEYWORD", 
      "keywords": [
        {
          "type": "KEYWORD", 
          "text": "\u30b9\u30dd\u30fc\u30c4", 
          "matchType": "PHRASE"
        }, 
        {
          "type": "KEYWORD", 
          "text": "\u590f", 
          "matchType": "PHRASE"
        }
      ]
    }, 
    {
      "xsi_type": "RelatedToUrlSearchParameter", 
      "searchParameterUse": "RELATED_TO_URL", 
      "url": "http://www.yahoo.co.jp/", 
      "includeSubUrls": "FALSE"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "3", 
    "Page.Type": "TargetingIdeaPage", 
    "values": [
      {
        "data": {
          "key": "KEYWORD", 
          "value": {
            "xsi_type": "KeywordAttribute", 
            "attributeType": "KEYWORD", 
            "value": {
              "type": "KEYWORD", 
              "text": "dummy keyword 0001", 
              "matchType": "EXACT"
            }
          }
        }
      }, 
      {
        "data": {
          "key": "KEYWORD", 
          "value": {
            "xsi_type": "KeywordAttribute", 
            "attributeType": "KEYWORD", 
            "value": {
              "type": "KEYWORD", 
              "text": "dummy keyword 0001", 
              "matchType": "PHRASE"
            }
          }
        }
      }, 
      {
        "data": {
          "key": "KEYWORD", 
          "value": {
            "xsi_type": "KeywordAttribute", 
            "attributeType": "KEYWORD", 
            "value": {
              "type": "KEYWORD", 
              "text": "dummy keyword 0001", 
              "matchType": "BROAD"
            }
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
