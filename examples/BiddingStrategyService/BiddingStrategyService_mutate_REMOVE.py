"""Example code for
Service : BiddingStrategyService
Operation: mutate (REMOVE)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/BiddingStrategyService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'BiddingStrategyService'
OPERATION = 'mutate (REMOVE)'
OPERAND = {
  "operator": "REMOVE", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "biddingStrategyId": "00000002"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "biddingStrategyId": "00000003"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "biddingStrategyId": "00000004"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "biddingStrategyId": "00000005"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "biddingStrategyId": "00000006"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "BiddingStartegyReturnValue", 
    "Operation.Type": "REMOVE", 
    "values": [
      {
        "operationSucceeded": "true", 
        "biddingStrategy": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "biddingStrategyId": "00000002", 
          "biddingStrategyName": "MODIFY_ENHANCED_CPC_BiddingStartegy", 
          "biddingStrategyType": "ENHANCED_CPC", 
          "biddingScheme": {
            "xsi_type": "EnhancedCpcBiddingScheme", 
            "biddingStrategyType": "ENHANCED_CPC"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "biddingStrategy": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "biddingStrategyId": "00000003", 
          "biddingStrategyName": "PAGE_ONE_PROMOTED_BiddingStartegy", 
          "biddingStrategyType": "PAGE_ONE_PROMOTED", 
          "biddingScheme": {
            "xsi_type": "PageOnePromotedBiddingScheme", 
            "biddingStrategyType": "PAGE_ONE_PROMOTED", 
            "targetPositionType": "PAGE_ONE", 
            "bidCeiling": "10000", 
            "bidMultiplier": "50.00", 
            "bidChangesForRaisesOnly": "DEACTIVE", 
            "raiseBidWhenBudgetConstrained": "ACTIVE", 
            "raiseBidWhenLowQualityScore": "ACTIVE"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "biddingStrategy": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "biddingStrategyId": "00000004", 
          "biddingStrategyName": "TARGET_CPA_BiddingStartegy", 
          "biddingStrategyType": "TARGET_CPA", 
          "biddingScheme": {
            "xsi_type": "TargetCpaBiddingScheme", 
            "biddingStrategyType": "TARGET_CPA", 
            "targetCpa": "250", 
            "bidCeiling": "10000", 
            "bidFloor": "100"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "biddingStrategy": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "biddingStrategyId": "00000005", 
          "biddingStrategyName": "TARGET_SPEND_BiddingStartegy", 
          "biddingStrategyType": "TARGET_SPEND", 
          "biddingScheme": {
            "xsi_type": "TargetSpendBiddingScheme", 
            "biddingStrategyType": "TARGET_SPEND", 
            "bidCeiling": "3500"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "biddingStrategy": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "biddingStrategyId": "00000006", 
          "biddingStrategyName": "TARGET_ROAS_BiddingStartegy", 
          "biddingStrategyType": "TARGET_ROAS", 
          "biddingScheme": {
            "xsi_type": "TargetRoasBiddingScheme", 
            "biddingStrategyType": "TARGET_ROAS", 
            "targetRoas": "0.15", 
            "bidCeiling": "1000", 
            "bidFloor": "0"
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
