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
Service : CampaignFeedService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.5/docs/en/api_reference/services/CampaignFeedService.md

Generated by 'api_reference_example_generator.py' using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignFeedService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignIds": [
    "SAMPLE-CAMPAIN-ID"
  ], 
  "feedItemIds": [
    "123", 
    "124", 
    "125"
  ], 
  "placeholderTypes": [
    "QUICKLINK", 
    "CALLEXTENSION"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "20"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "CampaignFeedPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "QUICKLINK", 
          "campaignFeed": [
            {
              "accountId": "SAMPLE-ACCOUNT-ID", 
              "campaignId": "SAMPLE-CAMPAIN-ID", 
              "feedItemId": "113", 
              "placeholderType": "QUICKLINK"
            }, 
            {
              "accountId": "SAMPLE-ACCOUNT-ID", 
              "campaignId": "SAMPLE-CAMPAIN-ID", 
              "feedItemId": "114", 
              "placeholderType": "QUICKLINK"
            }
          ], 
          "devicePlatform": "DESKTOP"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignFeedList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "placeholderType": "CALLEXTENSION", 
          "campaignFeed": {
            "accountId": "SAMPLE-ACCOUNT-ID", 
            "campaignId": "SAMPLE-CAMPAIN-ID", 
            "feedItemId": "115", 
            "placeholderType": "CALLEXTENSION"
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
