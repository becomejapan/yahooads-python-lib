"""Example code for
Service : AdGroupService
Operation: get
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
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "adGroupIds": [
    "SAMPLE-ADGROUP-ID"
  ], 
  "userStatuses": [
    "ACTIVE", 
    "PAUSED"
  ], 
  "biddingStrategyIds": [
    "100000001", 
    "100000002", 
    "100000003"
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "5", 
    "Page.Type": "AdGroupPage", 
    "values": [
      {
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
            "targetAll": "DEACTIVE"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "1111111112", 
          "campaignName": "sample campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "2222222222", 
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
            "targetAll": "DEACTIVE"
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
            "urlApprovalStatus": "REVIEW"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "1111111113", 
          "campaignName": "sample campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "2222222223", 
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
            "targetAll": "DEACTIVE"
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
            "urlApprovalStatus": "APPROVED"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "1111111114", 
          "campaignName": "sample campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "2222222224", 
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
            "targetAll": "DEACTIVE"
          }, 
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
        "adGroup": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "1111111115", 
          "campaignName": "sample campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "2222222225", 
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
            "targetAll": "DEACTIVE"
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