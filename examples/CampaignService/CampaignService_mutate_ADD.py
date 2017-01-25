"""Example code for
Service : CampaignService
Operation: mutate (ADD)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CampaignService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignService'
OPERATION = 'mutate (ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "campaignName": "STANDARD_MANUAL_CPC_${__time(YMDHMS,rTime)}_${__Random(1000000,9999999)}", 
      "userStatus": "ACTIVE", 
      "startDate": "${__time(YMD,rTime)}", 
      "endDate": "20371231", 
      "budget": {
        "period": "DAILY", 
        "amount": "10000", 
        "deliveryMethod": "STANDARD"
      }, 
      "biddingStrategyConfiguration": {
        "biddingStrategyType": "MANUAL_CPC"
      }, 
      "adServingOptimizationStatus": "OPTIMIZE", 
      "settings": {
        "xsi_type": "GeoTargetTypeSetting", 
        "type": "GEO_TARGET_TYPE_SETTING", 
        "positiveGeoTargetType": "DONT_CARE", 
        "negativeGeoTargetType": "LOCATION_OF_PRESENCE"
      }, 
      "campaignType": "STANDARD", 
      "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}", 
      "customParameters": {
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
      }
    }, 
    {
      "campaignName": "IOS_MANUAL_CPC_${__time(YMDHMS,rTime)}_${__Random(1000000,9999999)}", 
      "userStatus": "ACTIVE", 
      "startDate": "${__time(YMD,rTime)}", 
      "endDate": "20371231", 
      "budget": {
        "period": "DAILY", 
        "amount": "10000", 
        "deliveryMethod": "STANDARD"
      }, 
      "biddingStrategyConfiguration": {
        "biddingStrategyType": "MANUAL_CPC"
      }, 
      "adServingOptimizationStatus": "OPTIMIZE", 
      "settings": {
        "xsi_type": "GeoTargetTypeSetting", 
        "type": "GEO_TARGET_TYPE_SETTING", 
        "positiveGeoTargetType": "DONT_CARE", 
        "negativeGeoTargetType": "LOCATION_OF_PRESENCE"
      }, 
      "campaignType": "MOBILE_APP", 
      "appStore": "IOS", 
      "appId": "${__time(YMD,rTime)}${__Random(1000000,9999999)}", 
      "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}", 
      "customParameters": {
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
      }
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "CampaignReturnValue", 
    "Operation.Type": "ADD", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "STANDARD_MANUAL_CPC_20151126-172421_8817360", 
          "userStatus": "ACTIVE", 
          "servingStatus": "SERVING", 
          "startDate": "20151126", 
          "endDate": "20371231", 
          "budget": {
            "period": "DAILY", 
            "amount": "10000", 
            "deliveryMethod": "STANDARD"
          }, 
          "biddingStrategyConfiguration": {
            "biddingStrategyType": "MANUAL_CPC", 
            "biddingStrategySource": "CAMPAIGN", 
            "biddingScheme": {
              "xsi_type": "ManualCpcBiddingScheme", 
              "biddingStrategyType": "MANUAL_CPC"
            }
          }, 
          "conversionOptimizerEligibility": "DISABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "LOCATION_OF_PRESENCE"
          }, 
          "campaignType": "STANDARD", 
          "urlReviewData": {
            "inReviewUrl": {
              "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}", 
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
            "urlApprovalStatus": "REVIEW"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "IOS_MANUAL_CPC_20151126-172425_2884194", 
          "userStatus": "ACTIVE", 
          "servingStatus": "SERVING", 
          "startDate": "20151126", 
          "endDate": "20371231", 
          "budget": {
            "period": "DAILY", 
            "amount": "10000", 
            "deliveryMethod": "STANDARD"
          }, 
          "biddingStrategyConfiguration": {
            "biddingStrategyType": "MANUAL_CPC", 
            "biddingStrategySource": "CAMPAIGN", 
            "biddingScheme": {
              "xsi_type": "ManualCpcBiddingScheme", 
              "biddingStrategyType": "MANUAL_CPC"
            }
          }, 
          "conversionOptimizerEligibility": "DISABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "LOCATION_OF_PRESENCE"
          }, 
          "campaignType": "MOBILE_APP", 
          "appStore": "IOS", 
          "appId": "201511261169467", 
          "urlReviewData": {
            "inReviewUrl": {
              "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}", 
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
            "urlApprovalStatus": "REVIEW"
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
