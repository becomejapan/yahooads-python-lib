"""Example code for
Service : CustomerSyncService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CustomerSyncService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CustomerSyncService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "entityType": [
    "FEED_FOLDER", 
    "NEGATIVE_CAMPAIGN_TARGET_LIST", 
    "AD_GROUP_TARGET_LIST", 
    "TARGET_LIST"
  ], 
  "eventTypes": [
    "ADD", 
    "SET", 
    "REMOVE"
  ], 
  "sourceTypes": [
    "API", 
    "CAMPAIGN_MANAGEMENT_TOOL"
  ], 
  "dateRange": {
    "startDate": "20140401", 
    "endDate": "20140430", 
    "includeUnset": "INCLUDED"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "1", 
    "Page.Type": "CustomerChangeData", 
    "values": [
      {
        "operationSucceeded": "true", 
        "auditlog": {
          "updatedTime": "2015/07/21 13:38:26", 
          "entityType": "FEED_FOLDER", 
          "eventType": "ADD", 
          "sourceType": "API", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "feedFolderId": "51963"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "auditlog": {
          "updatedTime": "2015/07/15 18:22:28", 
          "entityType": "NEGATIVE_CAMPAIGN_TARGET_LIST", 
          "eventType": "ADD", 
          "sourceType": "API", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "auditlog": {
          "updatedTime": "2015/07/23 11:19:13", 
          "entityType": "AD_GROUP_TARGET_LIST", 
          "eventType": "ADD", 
          "sourceType": "API", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "auditlog": {
          "updatedTime": "2015/07/15 17:07:49", 
          "entityType": "TARGET_LIST", 
          "eventType": "ADD", 
          "sourceType": "API", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "targetListId": "3279"
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