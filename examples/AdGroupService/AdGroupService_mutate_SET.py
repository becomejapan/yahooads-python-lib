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
Service : AdGroupService
Operation: mutate (SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.5/docs/en/api_reference/services/AdGroupService.md

Generated by 'api_reference_example_generator.py' using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'AdGroupService'
OPERATION = 'mutate (SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": {
    "campaignId": "SAMPLE-CAMPAIN-ID", 
    "adGroupId": "SAMPLE-ADGROUP-ID", 
    "adGroupName": "set test adGroup.", 
    "userStatus": "PAUSED", 
    "settings": {
      "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", 
      "xsi_type": "TargetingSetting", 
      "criterionType": "TARGET_LIST", 
      "targetAll": "DEACTIVE"
    }, 
    "adGroupAdRotationMode": {
      "adRotationMode": "OPTIMIZE"
    }
  }
}

"""
SAMPLE RESPONSE = {
  "@xmlns": "http://ss.yahooapis.jp/V6", 
  "rval": {
    "ListReturnValue.Type": "AdGroupReturnValue", 
    "Operation.Type": "SET", 
    "values": {
      "operationSucceeded": "true", 
      "adGroup": {
        "accountId": "SAMPLE-ACCOUNT-ID", 
        "campaignId": "SAMPLE-CAMPAIN-ID", 
        "campaignTrackId": "100000001", 
        "campaignName": "test campaign.", 
        "adGroupId": "SAMPLE-ADGROUP-ID", 
        "adGroupTrackId": "0", 
        "adGroupName": "test adGroup.", 
        "userStatus": "ACTIVE", 
        "settings": {
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", 
          "xsi_type": "TargetingSetting", 
          "criterionType": "TARGET_LIST", 
          "targetAll": "ACTIVE"
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
        }, 
        "urlReviewData": {
          "urlApprovalStatus": "APPROVED"
        }, 
        "adGroupAdRotationMode": {
          "adRotationMode": "OPTIMIZE"
        }
      }
    }
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
