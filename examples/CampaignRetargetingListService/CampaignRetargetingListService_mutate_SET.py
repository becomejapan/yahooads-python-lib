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
Service : CampaignRetargetingListService
Operation: mutate(SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.3/docs/en/api_reference/services/CampaignRetargetingListService.md

Generated by 'api_reference_example_generator.py' using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignRetargetingListService'
OPERATION = 'mutate(SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "criterionTargetList": {
        "targetListId": "100000003"
      }, 
      "bidMultiplier": "1.3"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "criterionTargetList": {
        "targetListId": "100000003"
      }, 
      "excludedType": "INCLUDED", 
      "bidMultiplier": "0.1"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "CampaignRetargetingListReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaignRetargetingList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "campaign name", 
          "criterionTargetList": {
            "targetListId": "1000000003", 
            "targetListName": "targetList 1000000003"
          }, 
          "excludedType": "INCLUDED", 
          "bidMultiplier": "1.3"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignRetargetingList": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "campaign name", 
          "criterionTargetList": {
            "targetListId": "1000000004", 
            "targetListName": "targetList 1000000004"
          }, 
          "excludedType": "INCLUDED", 
          "bidMultiplier": "0.1"
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
