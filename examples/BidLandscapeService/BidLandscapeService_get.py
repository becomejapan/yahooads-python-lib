"""Example code for
Service : BidLandscapeService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/BidLandscapeService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'BidLandscapeService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "campaignId": "SAMPLE-CAMPAIN-ID", 
  "adGroupId": "SAMPLE-ADGROUP-ID", 
  "criterionIds": [
    "447", 
    "448", 
    "449", 
    "450"
  ], 
  "simType": "ADGROUP"
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "1", 
    "Page.Type": "BidLandscapePage", 
    "values": {
      "operationSucceeded": "true", 
      "data": {
        "xsi_type": "AdGroupBidLandscape", 
        "campaignId": "SAMPLE-CAMPAIN-ID", 
        "adGroupId": "SAMPLE-ADGROUP-ID", 
        "landscapePoints": {
          "bid": "100", 
          "clicks": "400", 
          "cost": "200", 
          "marginalCpc": "300", 
          "impressions": "500"
        }, 
        "BidLandscape.Type": "AdGroupBidLandscape", 
        "type": "DEFAULT", 
        "landscapeCurrent": "true"
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
