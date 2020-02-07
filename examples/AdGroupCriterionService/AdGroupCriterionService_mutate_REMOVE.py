# Copyright 2017 Become Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example code for
Service : AdGroupCriterionService
Operation: mutate (REMOVE)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/201901/docs/en/api_reference/services/AdGroupCriterionService.md

Generated by 'api_reference_example_generator.py' using code template 'examples/sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupCriterionService'
OPERATION = 'mutate (REMOVE)'
OPERAND = {
  "operator": "REMOVE", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "xsi_type": "NegativeAdGroupCriterion", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "criterionUse": "NEGATIVE", 
      "criterion": {
        "xsi_type": "Keyword", 
        "criterionId": "30001", 
        "type": "KEYWORD"
      }
    }, 
    {
      "xsi_type": "BiddableAdGroupCriterion", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "adGroupId": "SAMPLE-ADGROUP-ID", 
      "criterionUse": "BIDDABLE", 
      "criterion": {
        "xsi_type": "Keyword", 
        "criterionId": "30002", 
        "type": "KEYWORD"
      }
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "AdGroupCriterionReturnValue", 
    "Operation.Type": "REMOVE", 
    "values": [
      {
        "operationSucceeded": "true", 
        "adGroupCriterion": {
          "xsi_type": "NegativeAdGroupCriterion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "100000001", 
          "campaignName": "sample campaign.", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "200000001", 
          "adGroupName": "sample adgroup.", 
          "criterionUse": "NEGATIVE", 
          "criterion": {
            "xsi_type": "Keyword", 
            "criterionId": "30001", 
            "criterionTrackId": "0", 
            "type": "KEYWORD", 
            "text": "test keyword.", 
            "matchType": "PHRASE"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "adGroupCriterion": {
          "xsi_type": "BiddableAdGroupCriterion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignTrackId": "100000002", 
          "campaignName": "sample campaign.", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "adGroupTrackId": "200000002", 
          "adGroupName": "sample adgroup.", 
          "criterionUse": "BIDDABLE", 
          "criterion": {
            "xsi_type": "Keyword", 
            "criterionId": "30002", 
            "criterionTrackId": "0", 
            "type": "KEYWORD", 
            "text": "test keyword2.", 
            "matchType": "PHRASE"
          }, 
          "userStatus": "ACTIVE", 
          "approvalStatus": "APPROVED", 
          "bid": {
            "maxCpc": "100", 
            "bidSource": "CRITERION", 
            "adGroupMaxCpc": "1", 
            "keywordMaxCpc": "100"
          }, 
          "advancedUrl": "http://yahoo.co.jp", 
          "additionalAdvancedUrls": {
            "additionalAdvancedUrl": [
              {
                "url": "http://yahoo.co.jp/url1"
              }, 
              {
                "url": "http://yahoo.co.jp/url2"
              }, 
              {
                "url": "http://yahoo.co.jp/url3"
              }
            ]
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
          "trackingUrl": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={_site}&pid={_id1}&vid={_id2}", 
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
