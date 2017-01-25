"""Example code for
Service : FeedItemService
Operation: mutate(ADD)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/FeedItemService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'FeedItemService'
OPERATION = 'mutate(ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "placeholderType": "QUICKLINK", 
  "operand": {
    "feedItemAttribute": [
      {
        "xsi_type": "SimpleFeedItemAttribute", 
        "placeholderField": "ADVANCED_URL", 
        "feedAttributeValue": "http://www.yahoo.co.jp"
      }, 
      {
        "xsi_type": "SimpleFeedItemAttribute", 
        "placeholderField": "ADVANCED_MOBILE_URL", 
        "feedAttributeValue": "http://portal.mobile.yahoo.co.jp"
      }, 
      {
        "xsi_type": "SimpleFeedItemAttribute", 
        "placeholderField": "TRACKING_URL", 
        "feedAttributeValue": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&uid={id1}&xid={id2}"
      }
    ], 
    "startDate": "20151231", 
    "endDate": "20200101", 
    "scheduling": {
      "schedules": {
        "dayOfWeek": "MONDAY", 
        "startHour": "14", 
        "startMinute": "ZERO", 
        "endHour": "15", 
        "endMinute": "FIFTEEN"
      }
    }, 
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
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "FeedItemReturnValue", 
    "Operation.Type": "ADD", 
    "values": {
      "operationSucceeded": "true", 
      "feedItem": {
        "accountId": "SAMPLE-ACCOUNT-ID", 
        "feedItemId": "200000001", 
        "approvalStatus": "REVIEW", 
        "feedItemAttribute": [
          {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "ADVANCED_URL", 
            "feedAttributeValue": "http://www.yahoo.co.jp"
          }, 
          {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "ADVANCED_MOBILE_URL", 
            "feedAttributeValue": "http://portal.mobile.yahoo.co.jp"
          }, 
          {
            "xsi_type": "SimpleFeedItemAttribute", 
            "placeholderField": "TRACKING_URL", 
            "reviewFeedAttributeValue": "http://yahoo.co.jp?url={lpurl}&c={campaignid}&g={adgroupid}&a={creative}&type={site}&pid={id1}&vid={id2}"
          }
        ], 
        "placeholderType": "QUICKLINK", 
        "startDate": "20120112", 
        "endDate": "20120113", 
        "scheduling": {
          "schedules": [
            {
              "dayOfWeek": "MONDAY", 
              "startHour": "12", 
              "startMinute": "ZERO", 
              "endHour": "13", 
              "endMinute": "FIFTEEN"
            }, 
            {
              "dayOfWeek": "MONDAY", 
              "startHour": "12", 
              "startMinute": "ZERO", 
              "endHour": "13", 
              "endMinute": "FIFTEEN"
            }, 
            {
              "dayOfWeek": "MONDAY", 
              "startHour": "12", 
              "startMinute": "ZERO", 
              "endHour": "13", 
              "endMinute": "FIFTEEN"
            }
          ]
        }, 
        "reviewCustomParameters": {
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
