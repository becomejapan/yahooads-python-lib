"""Example code for
Service : CampaignTargetService
Operation: mutate (SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/CampaignTargetService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'CampaignTargetService'
OPERATION = 'mutate (SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "target": {
        "xsi_type": "ScheduleTarget", 
        "targetId": "00124534", 
        "targetType": "SCHEDULE"
      }, 
      "bidMultiplier": "1.5"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "target": {
        "xsi_type": "LocationTarget", 
        "targetId": "JP-0001-0010", 
        "targetType": "LOCATION"
      }, 
      "bidMultiplier": "0.95"
    }, 
    {
      "accountId": "SAMPLE-ACCOUNT-ID", 
      "campaignId": "SAMPLE-CAMPAIN-ID", 
      "target": {
        "xsi_type": "PlatformTarget", 
        "targetId": "0124534", 
        "targetType": "PLATFORM"
      }, 
      "bidMultiplier": "3"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "CampaignTargetReturnValue", 
    "Operation.Type": "SET", 
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
