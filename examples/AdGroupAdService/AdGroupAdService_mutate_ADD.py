"""Example code for
Service : AdGroupAdService
Operation: mutate (ADD)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AdGroupAdService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupAdService'
OPERATION = 'mutate (ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "adName": "Text Ad", 
      "userStatus": "ACTIVE", 
      "ad": {
        "xsi_type": "TextAd2", 
        "type": "TEXT_AD2", 
        "advancedUrl": "http://aaaa.jp", 
        "advancedMobileUrl": "http://aaaa.jp/mb", 
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
        "advanced": "TRUE", 
        "displayUrl": "www.yahoo.co.jp", 
        "headline": "Title", 
        "description": "CountDown", 
        "description2": "{=COUNTDOWN(\"2016/01/01 00:00:00\",\"ja\")}"
      }
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "adName": "Mobile App Ad", 
      "userStatus": "ACTIVE", 
      "ad": {
        "xsi_type": "AppAd", 
        "type": "APP_AD", 
        "advancedUrl": "http://www.apple.com/jp/itunes/app/appname/appid1234567890", 
        "advancedMobileUrl": "http://www.apple.com/jp/itunes/app/appname/appid1234567890", 
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
        "advanced": "TRUE", 
        "headline": "Mobile App Ad Title", 
        "description": "Mobile App Ad Description1", 
        "description2": "Mobile App Ad Description2", 
        "appStore": "IOS", 
        "appId": "appid1234567890"
      }
    }, 
    {
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "adName": "Text Ad", 
      "userStatus": "ACTIVE", 
      "ad": {
        "xsi_type": "ExtendedTextAd", 
        "type": "EXTENDED_TEXT_AD", 
        "advancedUrl": "http://yahoo.co.jp/url", 
        "advancedMobileUrl": "http://yahoo.co.jp/mobile/url", 
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
        "displayUrl": "www.yahoo.co.jp", 
        "headline": "Title", 
        "description": "Descrption", 
        "headline2": "Title2", 
        "path1": "addtional displayUrl1", 
        "path2": "addtional displayUrl2"
      }
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AdGroupAdReturnValue", 
    "Operation.Type": "ADD", 
    "values": [
      {
        "operationSucceeded": "true", 
        "adGroupAd": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "111111", 
          "campaignName": "Campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "222222", 
          "adGroupName": "Text Ad Group", 
          "adId": "SAMPLE-AD-ID", 
          "adTrackId": "333333", 
          "adName": "Text Ad2", 
          "userStatus": "ACTIVE", 
          "approvalStatus": "REVIEW", 
          "ad": {
            "xsi_type": "TextAd2", 
            "type": "TEXT_AD2", 
            "advancedUrl": "http://aaaa.jp", 
            "advancedMobileUrl": "http://aaaa.jp/mb", 
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
            "advanced": "TRUE", 
            "displayUrl": "www.yahoo.co.jp", 
            "headline": "Title", 
            "description": "CountDown", 
            "description2": "{=COUNTDOWN(\"2016/01/01 00:00:00\",\"ja\")}"
          }, 
          "feedFolderId": "100000001"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupAd": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "111111", 
          "campaignName": "Campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "444444", 
          "adGroupName": "Mobile App Ad Group", 
          "adId": "SAMPLE-AD-ID", 
          "adTrackId": "555555", 
          "adName": "Mobile App Ad", 
          "userStatus": "ACTIVE", 
          "approvalStatus": "APPROVED", 
          "ad": {
            "xsi_type": "AppAd", 
            "type": "APP_AD", 
            "advancedUrl": "http://www.apple.com/jp/itunes/app/appname/appid1234567890", 
            "advancedMobileUrl": "http://www.apple.com/jp/itunes/app/appname/appid1234567890", 
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
            "advanced": "TRUE", 
            "headline": "Mobile App Ad Title", 
            "description": "Mobile App Ad Description1", 
            "devicePreference": "SMART_PHONE", 
            "description2": "Mobile App Ad Description2", 
            "appStore": "IOS", 
            "appId": "appid1234567890"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupAd": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "111111", 
          "campaignName": "Campaign", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "444444", 
          "adGroupName": "Ad Group", 
          "adId": "SAMPLE-AD-ID", 
          "adTrackId": "555555", 
          "adName": "Ad", 
          "userStatus": "ACTIVE", 
          "approvalStatus": "APPROVED", 
          "ad": {
            "xsi_type": "ExtendedTextAd", 
            "type": "EXTENDED_TEXT_AD", 
            "advancedUrl": "http://yahoo.co.jp/sample/lpo", 
            "advancedMobileUrl": "http://yahoo.co.jp/sample/mobile/lpo", 
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
            "advanced": "TRUE", 
            "headline": "Title1", 
            "description": "Description", 
            "headline2": "Title2", 
            "path1": "addtional displayUrl1", 
            "path2": "addtional displayUrl2"
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