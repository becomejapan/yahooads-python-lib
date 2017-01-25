"""Example code for
Service : RetargetingListService
Operation: get
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
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "targetListIds": [
    "100000002", 
    "100000003", 
    "100000004"
  ], 
  "targetListTypes": [
    "DEFAULT", 
    "RULE", 
    "LOGICAL"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "20"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "3", 
    "Page.Type": "RetargetingListPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "targetList": {
          "xsi_type": "DefaultTargetList", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "retargetingAccountStatus": {
            "agreeDate": "20150612", 
            "reviewStatus": "APPROVED"
          }, 
          "targetListId": "100000002", 
          "targetListType": "DEFAULT", 
          "targetListName": "\u30c7\u30d5\u30a9\u30eb\u30c8\u30ea\u30b9\u30c8", 
          "targetListDescription": "\u30c7\u30d5\u30a9\u30eb\u30c8\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8", 
          "reachStorageStatus": "OPEN", 
          "reachStorageSpan": "180", 
          "reach": "0", 
          "targetListTrackId": "1234567890", 
          "tag": {
            "snippet": "<!-- Yahoo Code for your Target List -->\n                <script type=\"text/javascript\">\n                /* <![CDATA[ */\n                var yahoo_ss_retargeting_id = 1000137350;\n                var yahoo_sstag_custom_params =\n                window.yahoo_sstag_params;\n                var yahoo_ss_retargeting = true;\n                /* ]]> */\n                </script>\n                <script type=\"text/javascript\" src=\"//s.yimg.jp/images/listing/tool/cv/conversion.js\">\n                </script>\n                <noscript>\n                <div style=\"display:inline;\">\n                <img height=\"1\" width=\"1\" style=\"border-style:none;\" alt=\"\"\n                src=\"//b97.yahoo.co.jp/pagead/conversion/1000137350/?guid=ON&amp;script=0&amp;disvt=false\"/>\n                </div>\n                </noscript>"
          }
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
          "targetListId": "100000003", 
          "targetListType": "RULE", 
          "targetListName": "\u30eb\u30fc\u30eb\u30d9\u30fc\u30b9\u30ea\u30b9\u30c8", 
          "targetListDescription": "\u30eb\u30fc\u30eb\u30d9\u30fc\u30b9\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8", 
          "reachStorageStatus": "OPEN", 
          "reachStorageSpan": "180", 
          "reach": "0", 
          "targetListTrackId": "1234567890", 
          "rules": [
            {
              "ruleItems": [
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "EQUALS", 
                  "value": "http://yahoo.co.jp", 
                  "urlKey": "URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "NOT_EQUAL", 
                  "value": "http://not.equal.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "CONTAINS", 
                  "value": "http://contains.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "NOT_CONTAIN", 
                  "value": "http://not.contain.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "STARTS_WITH", 
                  "value": "http://starts.with.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "NOT_START_WITH", 
                  "value": "http://not.start.with.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "ENDS_WITH", 
                  "value": "http://ends.with.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }, 
                {
                  "xsi_type": "UrlRuleItem", 
                  "ruleType": "URL_RULE", 
                  "operator": "NOT_END_WITH", 
                  "value": "http://not.end.with.yahoo.co.jp", 
                  "urlKey": "REFFER_URL"
                }
              ]
            }, 
            {
              "ruleItems": {
                "xsi_type": "UrlRuleItem", 
                "ruleType": "URL_RULE", 
                "operator": "EQUALS", 
                "value": "http://equals2.yahoo.co.jp", 
                "urlKey": "REFFER_URL"
              }
            }
          ], 
          "isAllVisitor": "TRUE", 
          "isDateSpecific": "TRUE", 
          "startDate": "20150701", 
          "endDate": "20151231"
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
          "targetListId": "100000004", 
          "targetListType": "LOGICAL", 
          "targetListName": "\u30ed\u30b8\u30ab\u30eb\u30ea\u30b9\u30c8", 
          "targetListDescription": "\u30ed\u30b8\u30ab\u30eb\u30bf\u30fc\u30b2\u30c3\u30c8\u30ea\u30b9\u30c8", 
          "reachStorageStatus": "OPEN", 
          "reachStorageSpan": "180", 
          "reach": "0", 
          "targetListTrackId": "1234567890", 
          "logicalGroup": [
            {
              "condition": "AND", 
              "logicalOperand": [
                {
                  "targetListId": "100000002"
                }, 
                {
                  "targetListId": "100000003"
                }, 
                {
                  "targetListId": "100000005"
                }
              ]
            }, 
            {
              "condition": "OR", 
              "logicalOperand": [
                {
                  "targetListId": "100000006"
                }, 
                {
                  "targetListId": "100000007"
                }, 
                {
                  "targetListId": "100000008"
                }
              ]
            }, 
            {
              "condition": "NOT", 
              "logicalOperand": {
                "targetListId": "100000009"
              }
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
