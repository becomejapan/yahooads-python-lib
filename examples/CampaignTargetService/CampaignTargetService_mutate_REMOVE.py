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
Service : CampaignTargetService
Operation: mutate (REMOVE)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.3/docs/en/api_reference/services/CampaignTargetService.md

Generated by 'api_reference_example_generator.py' using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignTargetService'
OPERATION = 'mutate (REMOVE)'
OPERAND = {
  "operator": "REMOVE", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "target": {
        "xsi_type": "ScheduleTarget", 
        "targetId": "011112222", 
        "targetType": "SCHEDULE"
      }
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "target": {
        "xsi_type": "LocationTarget", 
        "targetId": "JP-0001-0010", 
        "targetType": "LOCATION"
      }
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "target": {
        "xsi_type": "NetworkTarget", 
        "targetId": "811112222", 
        "targetType": "NETWORK"
      }
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "CampaignTargetReturnValue", 
    "Operation.Type": "REMOVE", 
    "values": [
      {
        "operationSucceeded": "true", 
        "campaignTarget": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "Sample", 
          "target": {
            "xsi_type": "ScheduleTarget", 
            "targetId": "011112222", 
            "targetType": "SCHEDULE", 
            "dayOfWeek": "MONDAY", 
            "startHour": "21", 
            "startMinute": "ZERO", 
            "endHour": "24", 
            "endMinute": "ZERO"
          }, 
          "bidMultiplier": "1"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignTarget": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "Sample2", 
          "target": {
            "xsi_type": "LocationTarget", 
            "targetId": "JP-0001-0010", 
            "targetType": "LOCATION", 
            "provinceNameJA": "\u6771\u4eac\u90fd", 
            "provinceNameEN": "Tokyo", 
            "cityNameJA": "\u6e2f\u533a", 
            "cityNameEN": "Minatoku", 
            "excludedType": "INCLUDED", 
            "targetingStatus": "ACTIVE"
          }, 
          "bidMultiplier": "0.95"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "campaignTarget": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "campaignName": "Sample", 
          "target": {
            "xsi_type": "NetworkTarget", 
            "targetId": "811112222", 
            "targetType": "NETWORK", 
            "networkCoverageType": "YAHOO_SEARCH"
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
