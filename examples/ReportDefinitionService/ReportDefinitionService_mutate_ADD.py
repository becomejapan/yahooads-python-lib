"""Example code for
Service : ReportDefinitionService
Operation: mutate (ADD)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/ReportDefinitionService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'ReportDefinitionService'
OPERATION = 'mutate (ADD)'
OPERAND = {
  "operator": "ADD", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": {
    "reportId": "111111", 
    "reportName": "Sample LANDING_PAGE_URL Report", 
    "reportType": "LANDING_PAGE_URL", 
    "dateRangeType": "CUSTOM_DATE", 
    "dateRange": {
      "startDate": "20160101", 
      "endDate": "20161231"
    }, 
    "fields": [
      "CAMPAIGN_ID", 
      "ADGROUP_ID", 
      "CAMPAIGN_NAME", 
      "ADGROUP_NAME", 
      "COST", 
      "IMPS", 
      "CLICKS", 
      "CLICK_RATE", 
      "AVG_CPM", 
      "AVG_CPC", 
      "AVG_DELIVER_RANK", 
      "REVENUE", 
      "UNIQUE_CONVERSION", 
      "UNIQUE_CONVERSION_RATE", 
      "REVENUE_UNIQUE_CONVERSION", 
      "TRACKING_URL", 
      "CUSTOM_PARAMETERS", 
      "LANDING_PAGE_URL", 
      "NETWORK", 
      "DEVICE", 
      "DAY", 
      "DAY_OF_WEEK", 
      "QUARTER", 
      "YEAR", 
      "MONTH", 
      "MONTH_OF_YEAR", 
      "WEEK", 
      "OBJECT_OF_CONVERSION_TRACKING", 
      "CONVERSION_NAME"
    ], 
    "sortFields": {
      "type": "ASC", 
      "field": "CLICKS"
    }, 
    "filters": [
      {
        "field": "TRACKING_URL", 
        "operator": "IN", 
        "value": [
          "http://yahoo.co.jp", 
          "http://marketing.yahoo.co.jp", 
          "http://promotionalads.yahoo.co.jp"
        ]
      }, 
      {
        "field": "CAMPAIGN_ID", 
        "operator": "IN", 
        "value": [
          "200000001", 
          "200000002", 
          "200000003", 
          "200000003", 
          "200000004", 
          "200000005"
        ]
      }
    ], 
    "isTemplate": "FALSE", 
    "intervalType": "SPECIFYDAY", 
    "specifyDay": "28", 
    "format": "CSV", 
    "encode": "UTF-8", 
    "language": "EN", 
    "compress": "NONE", 
    "includeZeroImpressions": "TRUE", 
    "includeDeleted": "FALSE"
  }
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "ReportDefinitionReturnValue", 
    "Operation.Type": "ADD", 
    "values": {
      "operationSucceeded": "true", 
      "reportDefinition": {
        "reportId": "111111", 
        "reportName": "Sample LANDING_PAGE_URL Report", 
        "reportType": "LANDING_PAGE_URL", 
        "dateRangeType": "CUSTOM_DATE", 
        "dateRange": {
          "startDate": "20160101", 
          "endDate": "20161231"
        }, 
        "fields": [
          "CAMPAIGN_ID", 
          "ADGROUP_ID", 
          "CAMPAIGN_NAME", 
          "ADGROUP_NAME", 
          "COST", 
          "IMPS", 
          "CLICKS", 
          "CLICK_RATE", 
          "AVG_CPM", 
          "AVG_CPC", 
          "AVG_DELIVER_RANK", 
          "REVENUE", 
          "UNIQUE_CONVERSION", 
          "UNIQUE_CONVERSION_RATE", 
          "REVENUE_UNIQUE_CONVERSION", 
          "TRACKING_URL", 
          "CUSTOM_PARAMETERS", 
          "LANDING_PAGE_URL", 
          "NETWORK", 
          "DEVICE", 
          "DAY", 
          "DAY_OF_WEEK", 
          "QUARTER", 
          "YEAR", 
          "MONTH", 
          "MONTH_OF_YEAR", 
          "WEEK", 
          "OBJECT_OF_CONVERSION_TRACKING", 
          "CONVERSION_NAME"
        ], 
        "sortFields": {
          "type": "ASC", 
          "field": "CLICKS"
        }, 
        "filters": [
          {
            "field": "TRACKING_URL", 
            "operator": "IN", 
            "value": [
              "http://yahoo.co.jp", 
              "http://marketing.yahoo.co.jp", 
              "http://promotionalads.yahoo.co.jp"
            ]
          }, 
          {
            "field": "IMPS", 
            "operator": "GREATER_THAN", 
            "value": "0"
          }, 
          {
            "field": "CAMPAIGN_ID", 
            "operator": "IN", 
            "value": [
              "200000001", 
              "200000002", 
              "200000003", 
              "200000003", 
              "200000004", 
              "200000005"
            ]
          }
        ], 
        "isTemplate": "FALSE", 
        "intervalType": "SPECIFYDAY", 
        "specifyDay": "28", 
        "format": "CSV", 
        "encode": "UTF-8", 
        "language": "EN", 
        "compress": "NONE", 
        "includeZeroImpressions": "TRUE", 
        "includeDeleted": "FALSE"
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
