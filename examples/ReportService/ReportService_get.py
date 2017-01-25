"""Example code for
Service : ReportService
Operation: get
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/ReportService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'ReportService'
OPERATION = 'get'
OPERAND = {
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "reportIds": [
    "100000003", 
    "100000007", 
    "100000005"
  ], 
  "reportJobIds": [
    "100000003", 
    "100000007", 
    "100000005"
  ], 
  "reportTypes": [
    "AD_CUSTOMIZERS", 
    "TARGET_LIST", 
    "LANDING_PAGE_URL"
  ], 
  "reportJobStatuses": [
    "WAIT", 
    "COMPLETED", 
    "IN_PROGRESS", 
    "FAILED"
  ], 
  "paging": {
    "startIndex": "1", 
    "numberResults": "10"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "totalNumEntries": "4", 
    "Page.Type": "ReportPage", 
    "values": [
      {
        "operationSucceeded": "true", 
        "reportRecord": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "reportId": "2000000001", 
          "reportJobId": "3000000001", 
          "reportJobStatus": "COMPLETED", 
          "requestTime": "2015/11/30 22:22:30", 
          "completeTime": "2015/11/30 23:22:30", 
          "reportDownloadURL": "https://ss.yahooapis.jp/report/V6.0/download/3CRAGObSahcIylBoDZS5ftx7qS4VM5jSHqs77QZqmpBFnJFP2jvKe3Dy72UEX3InsUoShWXa3YcX3AmbtqxGco6B"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "reportRecord": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "reportId": "2000000002", 
          "reportJobId": "3000000002", 
          "reportJobStatus": "FAILED", 
          "reportJobErrorDetail": "INTERNAL_ERROR", 
          "requestTime": "2015/11/30 22:22:30"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "reportRecord": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "reportId": "2000000003", 
          "reportJobId": "3000000003", 
          "reportJobStatus": "IN_PROGRESS", 
          "requestTime": "2015/11/30 22:22:30"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "reportRecord": {
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "reportId": "2000000004", 
          "reportJobId": "3000000004", 
          "reportJobStatus": "WAIT", 
          "requestTime": "2015/11/30 22:22:30"
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
