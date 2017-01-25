"""Example code for
Service : AdGroupCriterionService
Operation: mutate (SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/AdGroupCriterionService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupCriterionService'
OPERATION = 'mutate (SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "xsi_type": "BiddableAdGroupCriterion", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "criterionUse": "BIDDABLE", 
      "criterion": {
        "xsi_type": "Keyword", 
        "criterionId": "1000000002", 
        "type": "KEYWORD"
      }, 
      "advancedUrl": "http://www.yahoo.co.jp", 
      "additionalAdvancedUrls": {
        "isRemove": "TRUE"
      }, 
      "advancedMobileUrl": "http://mobile.yahoo.co.jp", 
      "additionalAdvancedMobileUrls": {
        "additionalAdvancedMobileUrl": [
          {
            "url": "http://mobile.yahoo.co.jp/url1"
          }, 
          {
            "url": "http://mobile.yahoo.co.jp/url2"
          }, 
          {
            "url": "http://mobile.yahoo.co.jp/url3"
          }
        ]
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
      "advanced": "TRUE"
    }, 
    {
      "xsi_type": "BiddableAdGroupCriterion", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "criterionUse": "BIDDABLE", 
      "criterion": {
        "xsi_type": "Keyword", 
        "criterionId": "1000000003", 
        "type": "KEYWORD"
      }, 
      "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}", 
      "customParameters": {
        "isRemove": "TRUE"
      }, 
      "advanced": "TRUE"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AdGroupCriterionReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "adGroupCriterion": {
          "xsi_type": "BiddableAdGroupCriterion", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "criterionUse": "BIDDABLE", 
          "criterion": {
            "xsi_type": "Keyword", 
            "criterionId": "1000000002", 
            "criterionTrackId": "22222", 
            "type": "KEYWORD", 
            "text": "Keyword", 
            "matchType": "PHRASE"
          }, 
          "userStatus": "ACTIVE", 
          "approvalStatus": "REVIEW", 
          "biddingStrategyConfiguration": {
            "bid": {
              "maxCpc": "120"
            }
          }, 
          "advancedUrl": "http://www.yahoo.co.jp", 
          "advancedMobileUrl": "http://mobile.yahoo.co.jp", 
          "additionalAdvancedMobileUrls": {
            "additionalAdvancedMobileUrl": [
              {
                "url": "http://mobile.yahoo.co.jp/url1"
              }, 
              {
                "url": "http://mobile.yahoo.co.jp/url2"
              }, 
              {
                "reviewUrl": "http://mobile.yahoo.co.jp/url3"
              }
            ]
          }, 
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
          }, 
          "advanced": "TRUE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupCriterion": {
          "xsi_type": "BiddableAdGroupCriterion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "111111", 
          "campaignName": "campaign name", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "222222", 
          "adGroupName": "ad group name", 
          "criterionUse": "BIDDABLE", 
          "criterion": {
            "xsi_type": "Keyword", 
            "criterionId": "1000000002", 
            "criterionTrackId": "444444", 
            "type": "KEYWORD", 
            "text": "Keyword2", 
            "matchType": "PHRASE"
          }, 
          "userStatus": "ACTIVE", 
          "approvalStatus": "REVIEW", 
          "biddingStrategyConfiguration": {
            "biddingStrategyId": "1000000001", 
            "biddingStrategyName": "AutoBiddingName1", 
            "biddingStrategyType": "MANUAL_CPC", 
            "biddingStrategySource": "ADGROUP", 
            "biddingScheme": {
              "xsi_type": "ManualCpcBiddingScheme", 
              "biddingStrategyType": "MANUAL_CPC"
            }, 
            "bid": {
              "maxCpc": "0", 
              "bidSource": "CRITERION", 
              "adGroupMaxCpc": "120", 
              "keywordMaxCpc": "120"
            }, 
            "parentBiddingStrategyConfigurations": {
              "biddingStrategyId": "1000000003", 
              "biddingStrategyName": "AutoBiddingName2", 
              "biddingStrategyType": "MANUAL_CPC", 
              "biddingStrategySource": "CAMPAIGN", 
              "biddingScheme": {
                "xsi_type": "ManualCpcBiddingScheme", 
                "biddingStrategyType": "MANUAL_CPC"
              }
            }
          }, 
          "advancedUrl": "http://www.yahoo.co.jp", 
          "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}", 
          "reviewTrackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}", 
          "reviewCustomParameters": {
            "isRemove": "TRUE"
          }, 
          "advanced": "TRUE"
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