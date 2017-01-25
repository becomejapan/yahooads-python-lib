"""Example code for
Service : CampaignService
Operation: get
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
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "userStatuses": [
    "ACTIVE", 
    "PAUSED"
  ], 
  "biddingStrategyIds": [
    "10000000001", 
    "10000000002", 
    "10000000003", 
    "10000000004", 
    "10000000005"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "20"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "1", 
    "Page.Type": "CampaignPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "3000000001", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "STANDARD"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "3000000002", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "MOBILE_APP", 
          "appStore": "IOS", 
          "appId": "100000000000000"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "3000000003", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "MOBILE_APP", 
          "appStore": "ANDROID", 
          "appId": "jp.yahooapis.ss.V6.sampleApplication"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "3000000004", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "STANDARD", 
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
            "urlApprovalStatus": "APPROVED"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "3000000005", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "MOBILE_APP", 
          "appStore": "IOS", 
          "appId": "100000000000000", 
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
          "campaignTrackId": "3000000006", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "STANDARD", 
          "urlReviewData": {
            "disapprovalReviewUrl": {
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
            "urlApprovalStatus": "DISAPPROVED", 
            "disapprovalReasonCodes": [
              "1001", 
              "1002"
            ]
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaign": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "3000000005", 
          "campaignName": "campaign name", 
          "userStatus": "PAUSED", 
          "servingStatus": "PENDING", 
          "startDate": "20101201", 
          "endDate": "20141231", 
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
          "conversionOptimizerEligibility": "ENABLE", 
          "adServingOptimizationStatus": "OPTIMIZE", 
          "settings": {
            "xsi_type": "GeoTargetTypeSetting", 
            "type": "GEO_TARGET_TYPE_SETTING", 
            "positiveGeoTargetType": "DONT_CARE", 
            "negativeGeoTargetType": "DONT_CARE"
          }, 
          "campaignType": "MOBILE_APP", 
          "appStore": "IOS", 
          "appId": "100000000000000", 
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
            "urlApprovalStatus": "APPROVED_WITH_REVIEW"
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
