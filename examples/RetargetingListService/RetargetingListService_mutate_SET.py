"""Example code for
Service : RetargetingListService
Operation: mutate(SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/RetargetingListService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'RetargetingListService'
OPERATION = 'mutate(SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "xsi_type": "DefaultTargetList", 
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "targetListId": "200000001", 
      "targetListType": "DEFAULT", 
      "targetListName": "\u30c7\u30d5\u30a9\u30eb\u30c8\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8", 
      "targetListDescription": "sample description", 
      "reachStorageStatus": "OPEN", 
      "reachStorageSpan": "1"
    }, 
    {
      "xsi_type": "RuleBaseTargetList", 
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "targetListId": "200000002", 
      "targetListType": "RULE", 
      "targetListName": "\u30eb\u30fc\u30eb\u30d9\u30fc\u30b9\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8(\u66f4\u65b0)", 
      "targetListDescription": "sample description", 
      "reachStorageStatus": "CLOSED", 
      "reachStorageSpan": "1", 
      "rules": {
        "ruleItems": {
          "xsi_type": "UrlRuleItem", 
          "ruleType": "URL_RULE", 
          "operator": "CONTAINS", 
          "value": "http://yahoo.com", 
          "urlKey": "REFFER_URL"
        }
      }, 
      "isAllVisitor": "TRUE", 
      "startDate": "20160701", 
      "endDate": "20161231"
    }, 
    {
      "xsi_type": "LogicalTargetList", 
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "targetListId": "200000003", 
      "targetListType": "LOGICAL", 
      "targetListName": "\u30ed\u30b8\u30ab\u30eb\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8(\u66f4\u65b0)", 
      "targetListDescription": "sample description", 
      "reachStorageStatus": "CLOSED", 
      "reachStorageSpan": "1", 
      "logicalGroup": {
        "logicalOperand": {
          "targetListId": "100000005"
        }
      }
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "RetargetingListReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "operationSucceeded": "true", 
        "targetList": {
          "xsi_type": "DefaultTargetList", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "retargetingAccountStatus": {
            "agreeDate": "20150626", 
            "reviewStatus": "APPROVED"
          }, 
          "targetListId": "200000001", 
          "targetListType": "DEFAULT", 
          "targetListName": "\u30c7\u30d5\u30a9\u30eb\u30c8\u30ea\u30b9\u30c8", 
          "targetListDescription": "sample description", 
          "reachStorageStatus": "OPEN", 
          "reachStorageSpan": "1", 
          "reach": "0", 
          "tag": ""
        }
      }, 
      {
        "operationSucceeded": "true", 
        "targetList": {
          "xsi_type": "RuleBaseTargetList", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "retargetingAccountStatus": {
            "agreeDate": "20150612", 
            "reviewStatus": "APPROVED"
          }, 
          "targetListId": "200000002", 
          "targetListType": "RULE", 
          "targetListName": "\u30eb\u30fc\u30eb\u30d9\u30fc\u30b9\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8(\u66f4\u65b0)", 
          "targetListDescription": "sample description", 
          "reachStorageStatus": "CLOSED", 
          "reachStorageSpan": "1", 
          "reach": "0", 
          "targetListTrackId": "1234567890", 
          "rules": {
            "ruleItems": {
              "xsi_type": "UrlRuleItem", 
              "ruleType": "URL_RULE", 
              "operator": "CONTAINS", 
              "value": "http://yahoo.com", 
              "urlKey": "REFFER_URL"
            }
          }, 
          "isAllVisitor": "TRUE", 
          "isDateSpecific": "TRUE", 
          "startDate": "20160701", 
          "endDate": "20161231"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "targetList": {
          "xsi_type": "LogicalTargetList", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "retargetingAccountStatus": {
            "agreeDate": "20150612", 
            "reviewStatus": "APPROVED"
          }, 
          "targetListId": "200000003", 
          "targetListType": "LOGICAL", 
          "targetListName": "\u30ed\u30b8\u30ab\u30eb\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8(\u66f4\u65b0)", 
          "targetListDescription": "sample description", 
          "reachStorageStatus": "CLOSED", 
          "reachStorageSpan": "1", 
          "reach": "0", 
          "targetListTrackId": "1234567890", 
          "logicalGroup": {
            "condition": "OR", 
            "logicalOperand": {
              "targetListId": "100000005"
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
