"""Example code for
Service : BiddingStrategyService
Operation: get
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
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "biddingStrategyIds": [
    "00000002", 
    "00000003", 
    "00000004", 
    "00000005", 
    "00000006"
  ], 
  "biddingStrategyTypes": [
    "PAGE_ONE_PROMOTED", 
    "ENHANCED_CPC", 
    "TARGET_CPA", 
    "TARGET_ROAS", 
    "TARGET_SPEND"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "500"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "Page.Type": "AdGroupPage", 
    "totalNumEntries": "30", 
    "values": [
      {
        "operationSucceeded": "true", 
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "campaign name", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupName": "ad group name 1", 
          "userStatus": "ACTIVE", 
          "biddingStrategyConfiguration": {
            "biddingStrategyType": "MANUAL_CPC", 
            "biddingStrategySource": "ADGROUP", 
            "biddingScheme": {
              "xsi_type": "ManualCpcBiddingScheme", 
              "biddingStrategyType": "MANUAL_CPC"
            }, 
            "initialBid": {
              "maxCpc": "120", 
              "bidSource": "ADGROUP"
            }, 
            "parentBiddingStrategyConfigurations": {
              "biddingStrategyType": "MANUAL_CPC", 
              "biddingStrategySource": "CAMPAIGN", 
              "biddingScheme": {
                "xsi_type": "ManualCpcBiddingScheme", 
                "biddingStrategyType": "MANUAL_CPC"
              }
            }
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "campaign name", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupName": "ad group name 2", 
          "userStatus": "ACTIVE", 
          "biddingStrategyConfiguration": {
            "biddingStrategyId": "00000001", 
            "biddingStrategyName": "Sample bidding EnhancedCpcBidding", 
            "biddingStrategyType": "ENHANCED_CPC", 
            "biddingStrategySource": "ADGROUP", 
            "biddingScheme": {
              "xsi_type": "EnhancedCpcBiddingScheme", 
              "biddingStrategyType": "ENHANCED_CPC"
            }, 
            "initialBid": {
              "maxCpc": "120", 
              "bidSource": "ADGROUP"
            }, 
            "parentBiddingStrategyConfigurations": {
              "biddingStrategyType": "MANUAL_CPC", 
              "biddingStrategySource": "CAMPAIGN", 
              "biddingScheme": {
                "xsi_type": "ManualCpcBiddingScheme", 
                "biddingStrategyType": "MANUAL_CPC"
              }
            }
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "campaign name", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupName": "ad group name 3", 
          "userStatus": "ACTIVE", 
          "biddingStrategyConfiguration": {
            "biddingStrategyType": "MANUAL_CPC", 
            "biddingStrategySource": "CAMPAIGN", 
            "biddingScheme": {
              "xsi_type": "ManualCpcBiddingScheme", 
              "biddingStrategyType": "MANUAL_CPC"
            }, 
            "initialBid": {
              "maxCpc": "120", 
              "bidSource": "ADGROUP"
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
