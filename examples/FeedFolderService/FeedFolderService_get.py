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
Service : FeedFolderService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/201901/docs/en/api_reference/services/FeedFolderService.md

Generated by 'api_reference_example_generator.py' using code template 'examples/sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'FeedFolderService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "feedFolderIds": [
    "10001", 
    "10002", 
    "10003", 
    "10004", 
    "10005"
  ], 
  "placeholderTypes": [
    "AD_CUSTOMIZER", 
    "DYNAMIC_AD_FOR_SEARCH_PAGE_FEEDS"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "1000"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "2", 
    "Page.Type": "FeedFolderPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "feedFolder": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedFolderId": "10001", 
          "feedFolderName": "test feedFolder.", 
          "placeholderType": "AD_CUSTOMIZER", 
          "feedAttribute": [
            {
              "feedAttributeId": "1", 
              "feedAttributeName": "integerFeedAttribute", 
              "placeholderField": "AD_CUSTOMIZER_INTEGER"
            }, 
            {
              "feedAttributeId": "2", 
              "feedAttributeName": "priceFeedAttribute", 
              "placeholderField": "AD_CUSTOMIZER_PRICE"
            }, 
            {
              "feedAttributeId": "3", 
              "feedAttributeName": "dateFeedAttribute", 
              "placeholderField": "AD_CUSTOMIZER_DATE"
            }, 
            {
              "feedAttributeId": "4", 
              "feedAttributeName": "stringFeedAttribute", 
              "placeholderField": "AD_CUSTOMIZER_STRING"
            }
          ]
        }
      }, 
      {
        "operationSucceeded": "true", 
        "feedFolder": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedFolderId": "10002", 
          "feedFolderName": "test dynamic ad for search page feed.", 
          "placeholderType": "DYNAMIC_AD_FOR_SEARCH_PAGE_FEEDS", 
          "domain": "https://www.yahoo.co.jp"
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
