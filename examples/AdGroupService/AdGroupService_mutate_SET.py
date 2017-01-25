"""Example code for
Service : AdGroupService
Operation: mutate (SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AdGroupService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupService'
OPERATION = 'mutate (SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": {
    "campaignId": "SAMPLE-CAMPAIN-ID", 
    "adGroupId": "SAMPLE-ADGROUP-ID", 
    "adGroupName": "sample adgroup", 
    "userStatus": "ACTIVE", 
    "biddingStrategyConfiguration": {
      "biddingStrategyType": "MANUAL_CPC", 
      "initialBid": {
        "maxCpc": "120"
      }
    }, 
    "settings": {
      "xsi_type": "TargetingSetting", 
      "criterionType": "TARGET_LIST", 
      "targetAll": "ACTIVE"
    }, 
    "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&uid={id1}&xid={id2}", 
    "customParameters": {
      "isRemove": "FALSE", 
      "parameters": [
        {
          "key": "site", 
          "value": "mysite"
        }, 
        {
          "key": "id1", 
          "value": "5678"
        }, 
        {
          "key": "id2", 
          "value": "jFj903Hng8e"
        }
      ]
    }
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AdGroupReturnValue", 
    "Operation.Type": "SET", 
    "values": {
      "operationSucceeded": "true", 
      "adGroup": {
        "accountId": "SAMPLE-ACCOUNT-ID", 
        "campaignId": "SAMPLE-CAMPAIN-ID", 
        "campaignTrackId": "1111111111", 
        "campaignName": "sample campaign", 
        "adGroupId": "SAMPLE-ADGROUP-ID", 
        "adGroupTrackId": "2222222221", 
        "adGroupName": "sample adgroup", 
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
        }, 
        "settings": {
          "xsi_type": "TargetingSetting", 
          "criterionType": "TARGET_LIST", 
          "targetAll": "ACTIVE"
        }, 
        "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}", 
        "customParameters": {
          "isRemove": "FALSE", 
          "parameters": [
            {
              "key": "site", 
              "value": "yahoo"
            }, 
            {
              "key": "id1", 
              "value": "1234"
            }, 
            {
              "key": "id2", 
              "value": "a7h59A98yu"
            }
          ]
        }, 
        "urlReviewData": {
          "inReviewUrl": {
            "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&uid={id1}&xid={id2}", 
            "parameters": [
              {
                "key": "site", 
                "value": "mysite"
              }, 
              {
                "key": "id1", 
                "value": "5678"
              }, 
              {
                "key": "id2", 
                "value": "jFj903Hng8e"
              }
            ]
          }, 
          "urlApprovalStatus": "APPROVED_WITH_REVIEW"
        }
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
