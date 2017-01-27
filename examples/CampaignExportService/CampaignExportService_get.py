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
Service : CampaignExportService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CampaignExportService.md

Generated by 'api_reference_example_generator.py' using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignExportService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "jobIds": [
    "xxxxxxxxxxxxxx", 
    "xxxxxxxxxxxxxx", 
    "xxxxxxxxxxxxxx"
  ], 
  "statuses": [
    "COMPLETED", 
    "IN_PROGRESS"
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "1", 
    "Page.Type": "CampaignExportPage", 
    "values": {
      "operationSucceeded": "true", 
      "job": {
        "accountId": "SAMPLE-ACCOUNT-ID", 
        "jobId": "1", 
        "userName": "8983-5689-9971-5970", 
        "startDate": "2011-09-06T23:53:08+09:00", 
        "endDate": "2011-09-06T23:53:30+09:00", 
        "progress": "100", 
        "status": "COMPLETED", 
        "downloadUrl": "https ://colo05.ss.yahooapis.jp/bulkDownload/V6/download/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
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
