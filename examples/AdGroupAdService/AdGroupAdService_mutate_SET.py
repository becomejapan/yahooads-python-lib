"""Example code for
Service : AdGroupAdService
Operation: mutate (SET)
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
OPERATION = 'mutate (SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "adId": "SAMPLE-AD-ID", 
      "adName": "Text ad 2 update", 
      "userStatus": "PAUSED"
    }, 
    {
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "adId": "SAMPLE-AD-ID", 
      "adName": "Mobile ad update", 
      "userStatus": "PAUSED"
    }, 
    {
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "adId": "SAMPLE-AD-ID", 
      "adName": "App ad update", 
      "userStatus": "PAUSED"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AdGroupAdReturnValue", 
    "Operation.Type": "SET", 
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
          "adGroupName": "Text ad group", 
          "adId": "SAMPLE-AD-ID", 
          "adTrackId": "333333", 
          "adName": "Text ad update", 
          "userStatus": "PAUSED", 
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
            "headline": "Headline", 
            "description": "Count down", 
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
          "adGroupTrackId": "333333", 
          "adGroupName": "Mobile ad group", 
          "adId": "SAMPLE-AD-ID", 
          "adTrackId": "444444", 
          "adName": "Mobile ad update", 
          "userStatus": "PAUSED", 
          "approvalStatus": "REVIEW", 
          "ad": {
            "xsi_type": "MobileAd", 
            "type": "MOBILE_AD", 
            "advanced": "FALSE", 
            "url": "http://www.yahoo.co.jp", 
            "displayUrl": "www.yahoo.co.jp", 
            "headline": "Headline", 
            "description": "Test description", 
            "markupLanguages": [
              "HTML", 
              "CHTML", 
              "XHTML"
            ], 
            "mobileCarriers": [
              "DOCOMO", 
              "KDDI", 
              "SOFTBANK"
            ]
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
          "adGroupName": "App ad group", 
          "adId": "SAMPLE-AD-ID", 
          "adTrackId": "555555", 
          "adName": "App ad update", 
          "userStatus": "PAUSED", 
          "approvalStatus": "REVIEW", 
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
            "headline": "App ad headline", 
            "description": "App ad description1", 
            "description2": "App ad description2", 
            "appStore": "IOS", 
            "appId": "appid1234567890", 
            "devicePreference": "SMART_PHONE"
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
