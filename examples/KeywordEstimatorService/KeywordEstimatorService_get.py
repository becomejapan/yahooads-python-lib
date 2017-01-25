"""Example code for
Service : KeywordEstimatorService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/KeywordEstimatorService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'KeywordEstimatorService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignEstimateRequest": {
    "campaignId": "SAMPLE-CAMPAIN-ID", 
    "adGroupEstimateRequests": [
      {
        "adGroupId": "SAMPLE-ADGROUP-ID", 
        "keywordEstimateRequests": {
          "keyword": {
            "text": "\u53e4\u7740", 
            "matchType": "PHRASE"
          }, 
          "isNegative": "FALSE", 
          "maxCpc": "5000"
        }, 
        "maxCpc": "800"
      }, 
      {
        "adGroupId": "SAMPLE-ADGROUP-ID", 
        "keywordEstimateRequests": {
          "keyword": {
            "text": "\u82b1\u706b\u3000\u590f", 
            "matchType": "EXACT"
          }, 
          "isNegative": "FALSE", 
          "maxCpc": "9000"
        }, 
        "maxCpc": "1000"
      }
    ], 
    "provinces": "JP-13", 
    "dailyBudget": "1000"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "1", 
    "Page.Type": "KeywordEstimatorPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "data": {
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "keyword": "\u53e4\u7740", 
          "min": {
            "clicks": "29.59", 
            "rank": "1", 
            "cpc": "32.11", 
            "cost": "1055.55", 
            "impressions": "3000", 
            "ctr": "0.0012"
          }, 
          "max": {
            "clicks": "36.16", 
            "rank": "1.1", 
            "cpc": "39.24", 
            "cost": "1290.12", 
            "impressions": "3100", 
            "ctr": "0.0022"
          }
        }
      }, 
      {
        "operationSucceeded": "true", 
        "data": {
          "campaignId": "SAMPLE-CAMPAIN-ID", 
          "adGroupId": "SAMPLE-ADGROUP-ID", 
          "keyword": "\u82b1\u706b\u3000\u590f", 
          "min": {
            "clicks": "11.59", 
            "rank": "1", 
            "cpc": "32.01", 
            "cost": "2055.55", 
            "impressions": "3000", 
            "ctr": "0.0012"
          }, 
          "max": {
            "clicks": "9999.16", 
            "rank": "1.1", 
            "cpc": "39.24", 
            "cost": "3290.12", 
            "impressions": "3100", 
            "ctr": "0.0022"
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
