"""Example code for
Service : FeedItemService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/FeedItemService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'FeedItemService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "feedItemIds": [
    "12", 
    "13"
  ], 
  "placeholderTypes": [
    "QUICKLINK", 
    "CALLEXTENSION", 
    "AD_CUSTOMIZER", 
    "CALLOUT"
  ], 
  "approvalStatuses": [
    "APPROVED", 
    "REVIEW"
  ], 
  "advanced": "TRUE", 
  "paging": {
    "startIndex": "1", 
    "numberResults": "20"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "7", 
    "Page.Type": "FeedItemPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedItemId": "113", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": [
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "ADVANCED_URL", 
              "feedAttributeValue": "http://www.yahoo.co.jp"
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "ADVANCED_MOBILE_URL", 
              "feedAttributeValue": "http://portal.mobile.yahoo.co.jp"
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "TRACKING_URL", 
              "reviewFeedAttributeValue": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}"
            }
          ], 
          "placeholderType": "QUICKLINK", 
          "startDate": "20120112", 
          "endDate": "20120113", 
          "scheduling": {
            "schedules": [
              {
                "dayOfWeek": "MONDAY", 
                "startHour": "12", 
                "startMinute": "ZERO", 
                "endHour": "13", 
                "endMinute": "FIFTEEN"
              }, 
              {
                "dayOfWeek": "MONDAY", 
                "startHour": "12", 
                "startMinute": "ZERO", 
                "endHour": "13", 
                "endMinute": "FIFTEEN"
              }, 
              {
                "dayOfWeek": "MONDAY", 
                "startHour": "12", 
                "startMinute": "ZERO", 
                "endHour": "13", 
                "endMinute": "FIFTEEN"
              }
            ]
          }, 
          "reviewCustomParameters": {
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
          "advanced": "TRUE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedItemId": "114", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": [
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "ADVANCED_URL", 
              "feedAttributeValue": "http://www.yahoo.co.jp"
            }, 
            {
              "xsi_type": "MultipleFeedItemAttribute", 
              "placeholderField": "ADDITIONAL_ADVANCED_URLS", 
              "feedAttributeValues": [
                {
                  "feedAttributeValue": "http://www.yahoo.co.jp/url1"
                }, 
                {
                  "feedAttributeValue": "http://www.yahoo.co.jp/url2"
                }
              ]
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "ADVANCED_MOBILE_URL", 
              "feedAttributeValue": "http://portal.mobile.yahoo.co.jp"
            }, 
            {
              "xsi_type": "MultipleFeedItemAttribute", 
              "placeholderField": "ADDITIONAL_ADVANCED_MOBILE_URLS", 
              "feedAttributeValues": [
                {
                  "feedAttributeValue": "http://portal.mobile.yahoo.co.jp/url1"
                }, 
                {
                  "feedAttributeValue": "http://portal.mobile.yahoo.co.jp/url2"
                }
              ]
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "TRACKING_URL", 
              "reviewFeedAttributeValue": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}"
            }
          ], 
          "placeholderType": "QUICKLINK", 
          "startDate": "20120112", 
          "endDate": "20120113", 
          "scheduling": {
            "schedules": [
              {
                "dayOfWeek": "MONDAY", 
                "startHour": "12", 
                "startMinute": "ZERO", 
                "endHour": "13", 
                "endMinute": "FIFTEEN"
              }, 
              {
                "dayOfWeek": "MONDAY", 
                "startHour": "12", 
                "startMinute": "ZERO", 
                "endHour": "13", 
                "endMinute": "FIFTEEN"
              }, 
              {
                "dayOfWeek": "MONDAY", 
                "startHour": "12", 
                "startMinute": "ZERO", 
                "endHour": "13", 
                "endMinute": "FIFTEEN"
              }
            ]
          }, 
          "reviewCustomParameters": {
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
          "advanced": "TRUE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedItemId": "115", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "CALL_PHONE_NUMBER", 
            "feedAttributeValue": "0120-111-222"
          }, 
          "placeholderType": "CALLEXTENSION", 
          "startDate": "20130910", 
          "endDate": "20130920", 
          "scheduling": {
            "schedules": {
              "dayOfWeek": "MONDAY", 
              "startHour": "14", 
              "startMinute": "ZERO", 
              "endHour": "15", 
              "endMinute": "FIFTEEN"
            }
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedItemId": "116", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "CALL_PHONE_NUMBER", 
            "feedAttributeValue": "0120-123-456"
          }, 
          "placeholderType": "CALLEXTENSION"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedFolderId": "999999", 
          "feedItemId": "100000", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": [
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "AD_CUSTOMIZER_INTEGER", 
              "feedAttributeId": "999999", 
              "feedAttributeValue": "1234567890"
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "AD_CUSTOMIZER_PRICE", 
              "feedAttributeId": "999999", 
              "feedAttributeValue": "9,999,999.99"
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "AD_CUSTOMIZER_DATE", 
              "feedAttributeId": "999999", 
              "feedAttributeValue": "20151231 235959"
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "AD_CUSTOMIZER_STRING", 
              "feedAttributeId": "999999", 
              "feedAttributeValue": "abcdefghijklmnopqrstuvwxyz"
            }, 
            {
              "xsi_type": "SimpleFeedItemAttribute", 
              "placeholderField": "LINK_TEXT", 
              "feedAttributeValue": "abcdefghijklmnopqrstuvwxyz"
            }
          ], 
          "placeholderType": "AD_CUSTOMIZER", 
          "startDate": "20150217", 
          "endDate": "20150217", 
          "scheduling": {
            "schedules": {
              "dayOfWeek": "MONDAY", 
              "startHour": "14", 
              "startMinute": "ZERO", 
              "endHour": "15", 
              "endMinute": "FIFTEEN"
            }
          }, 
          "targetingCampaign": {
            "targetingCampaignId": "999999"
          }, 
          "targetingAdGroup": {
            "targetingAdGroupId": "999999"
          }, 
          "targetingKeyword": {
            "text": "keyword keyword keyword keyword", 
            "matchType": "PHRASE"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedItemId": "100000", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "AD_CUSTOMIZER_INTEGER", 
            "feedAttributeId": "999999", 
            "feedAttributeValue": "1234567890"
          }, 
          "placeholderType": "AD_CUSTOMIZER"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedItem": {
          "feedItemId": "200000001", 
          "approvalStatus": "REVIEW", 
          "feedItemAttribute": {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "CALLOUT_TEXT", 
            "feedAttributeValue": "modify Text"
          }, 
          "placeholderType": "CALLOUT", 
          "startDate": "20151231", 
          "endDate": "20200101", 
          "scheduling": {
            "schedules": {
              "dayOfWeek": "MONDAY", 
              "startHour": "14", 
              "startMinute": "ZERO", 
              "endHour": "15", 
              "endMinute": "FIFTEEN"
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
