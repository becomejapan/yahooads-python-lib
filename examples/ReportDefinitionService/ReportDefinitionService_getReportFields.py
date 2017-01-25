"""Example code for
Service : ReportDefinitionService
Operation: getReportFields
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
OPERATION = 'getReportFields'
OPERAND = {
  "reportType": "LANDING_PAGE_URL"
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "operationSucceeded": "true", 
    "fields": [
      {
        "fieldName": "AVERAGECPC", 
        "displayFieldNameJA": "\u5e73\u5747CPC", 
        "displayFieldNameEN": "Avg. CPC", 
        "xmlAttributeName": "averageCpc", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "AVERAGECPM", 
        "displayFieldNameJA": "\u5e73\u5747CPM", 
        "displayFieldNameEN": "Avg. CPM", 
        "xmlAttributeName": "averageCpm", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "AVERAGEPOSITION", 
        "displayFieldNameJA": "\u5e73\u5747\u63b2\u8f09\u9806\u4f4d", 
        "displayFieldNameEN": "Avg. Position", 
        "xmlAttributeName": "averagePosition", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "CLICKS", 
        "displayFieldNameJA": "\u30af\u30ea\u30c3\u30af\u6570", 
        "displayFieldNameEN": "Clicks", 
        "xmlAttributeName": "clicks", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "UNIQUECONVERSIONRATE", 
        "displayFieldNameJA": "\u30e6\u30cb\u30fc\u30af\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u7387", 
        "displayFieldNameEN": "Unique Conversion Rate", 
        "xmlAttributeName": "uniqueConversionRate", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "TOTALCONVERSIONRATE", 
        "displayFieldNameJA": "\u7dcf\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u7387", 
        "displayFieldNameEN": "Total Conversion Rate", 
        "xmlAttributeName": "totalConversionRate", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "UNIQUECONVERSIONS", 
        "displayFieldNameJA": "\u30b3\u30b9\u30c8/\u30e6\u30cb\u30fc\u30af\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Unique Conversions", 
        "xmlAttributeName": "uniqueConversions", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "TOTALCONVERSIONS", 
        "displayFieldNameJA": "\u30b3\u30b9\u30c8/\u7dcf\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Total Conversions", 
        "xmlAttributeName": "totalConversions", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "TOTALREVENUE", 
        "displayFieldNameJA": "\u5408\u8a08\u58f2\u4e0a\u91d1\u984d", 
        "displayFieldNameEN": "Total Revenue", 
        "xmlAttributeName": "totalRevenue", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "COST", 
        "displayFieldNameJA": "\u30b3\u30b9\u30c8", 
        "displayFieldNameEN": "Cost", 
        "xmlAttributeName": "cost", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "COSTUNIQUECONVERSIONS", 
        "displayFieldNameJA": "\u30b3\u30b9\u30c8/\u30e6\u30cb\u30fc\u30af\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Cost / Unique Conversions", 
        "xmlAttributeName": "costUniqueConversions", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "COSTTOTALCONVERSIONS", 
        "displayFieldNameJA": "\u30b3\u30b9\u30c8/\u7dcf\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Cost / Total Conversions", 
        "xmlAttributeName": "costTotalConversions", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "CTR", 
        "displayFieldNameJA": "\u30af\u30ea\u30c3\u30af\u7387", 
        "displayFieldNameEN": "CTR", 
        "xmlAttributeName": "ctr", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "IMPRESSIONS", 
        "displayFieldNameJA": "\u30a4\u30f3\u30d7\u30ec\u30c3\u30b7\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Impressions", 
        "xmlAttributeName": "impressions", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "INVALIDCLICKRATE", 
        "displayFieldNameJA": "\u7121\u52b9\u306a\u30af\u30ea\u30c3\u30af\u7387", 
        "displayFieldNameEN": "Invalid Click Rate", 
        "xmlAttributeName": "invalidClickRate", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "INVALIDCLICKS", 
        "displayFieldNameJA": "\u7121\u52b9\u306a\u30af\u30ea\u30c3\u30af", 
        "displayFieldNameEN": "Invalid Clicks", 
        "xmlAttributeName": "invalidClicks", 
        "fieldType": "Long", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "REVENUEUNIQUECONVERSIONS", 
        "displayFieldNameJA": "\u58f2\u4e0a/\u30e6\u30cb\u30fc\u30af\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Revenue / Unique Conversions", 
        "xmlAttributeName": "revenueUniqueConversions", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "REVENUETOTALCONVERSIONS", 
        "displayFieldNameJA": "\u58f2\u4e0a/\u7dcf\u30b3\u30f3\u30d0\u30fc\u30b8\u30e7\u30f3\u6570", 
        "displayFieldNameEN": "Revenue / Total Conversions", 
        "xmlAttributeName": "revenueTotalConversions", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "EXACTMATCHIMPRESSIONSHARE", 
        "displayFieldNameJA": "\u5b8c\u5168\u4e00\u81f4\u306e\u30a4\u30f3\u30d7\u30ec\u30c3\u30b7\u30e7\u30f3\u30b7\u30a7\u30a2", 
        "displayFieldNameEN": "Exact Match Impression Share", 
        "xmlAttributeName": "exactMatchImpressionShare", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "BUDGETLOSTIMPRESSIONSHARE", 
        "displayFieldNameJA": "\u30a4\u30f3\u30d7\u30ec\u30c3\u30b7\u30e7\u30f3\u640d\u5931\u7387\uff08\u4e88\u7b97\uff09", 
        "displayFieldNameEN": "Budget Lost Impression Share", 
        "xmlAttributeName": "budgetLostImpressionShare", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "IMPRESSIONSHARE", 
        "displayFieldNameJA": "\u30a4\u30f3\u30d7\u30ec\u30c3\u30b7\u30e7\u30f3\u30b7\u30a7\u30a2", 
        "displayFieldNameEN": "Impression Share", 
        "xmlAttributeName": "impressionShare", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
      }, 
      {
        "fieldName": "QUALITYLOSTIMPRESSIONSHARE", 
        "displayFieldNameJA": "\u30a4\u30f3\u30d7\u30ec\u30c3\u30b7\u30e7\u30f3\u640d\u5931\u7387\uff08\u63b2\u8f09\u9806\u4f4d\uff09", 
        "displayFieldNameEN": "Quality Lost ImpressionShare", 
        "xmlAttributeName": "qualityLostImpressionShare", 
        "fieldType": "Double", 
        "canSelect": "true", 
        "canFilter": "true"
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