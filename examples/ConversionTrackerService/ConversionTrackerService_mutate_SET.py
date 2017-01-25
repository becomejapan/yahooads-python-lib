"""Example code for
Service : ConversionTrackerService
Operation: mutate (SET)
API Reference: https://github.com/yahoojp-marketing/sponsored-search-api-documents/blob/6.2/docs/en/api_reference/services/ConversionTrackerService.md

Generated api_reference_example_generator.py using code template 'sample_template.py.template'
"""

import logging
import json

from yahooads import promotionalads

logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


SERVICE = 'ConversionTrackerService'
OPERATION = 'mutate (SET)'
OPERAND = {
  "operator": "SET", 
  "accountId": "SAMPLE-ACCOUNT-ID", 
  "operand": [
    {
      "xsi_type": "WebConversion", 
      "conversionTrackerId": "1193194", 
      "conversionTrackerName": "WEB_CONVERSION_TRACKER_EDIT", 
      "status": "ENABLED", 
      "category": "PAGE_VIEW", 
      "conversionTrackerType": "WEB_CONVERSION", 
      "userRevenueValue": "100", 
      "markupLanguage": "HTML", 
      "trackingCodeType": "WEBPAGE"
    }, 
    {
      "xsi_type": "WebConversion", 
      "conversionTrackerId": "1193195", 
      "conversionTrackerName": "CALL_CONVERSION_TRACKER_EDIT", 
      "status": "DISABLED", 
      "category": "DEFAULT", 
      "conversionTrackerType": "WEB_CONVERSION", 
      "userRevenueValue": "200", 
      "countingType": "ONE_PER_CLICK", 
      "markupLanguage": "HTML", 
      "trackingCodeType": "CLICK_TO_CALL"
    }, 
    {
      "xsi_type": "AppConversion", 
      "conversionTrackerId": "1193196", 
      "conversionTrackerName": "APP_ANDROID_DOWNLOAD_CONVERSION_TRACKER_EDIT", 
      "status": "ENABLED", 
      "category": "DOWNLOAD", 
      "conversionTrackerType": "APP_CONVERSION", 
      "userRevenueValue": "100", 
      "countingType": "ONE_PER_CLICK", 
      "appId": "abc_1234"
    }, 
    {
      "xsi_type": "AppConversion", 
      "conversionTrackerId": "1193197", 
      "conversionTrackerName": "APP_ANDROID_FIRST_OPEN_CONVERSION_TRACKER_EDIT", 
      "status": "ENABLED", 
      "category": "DOWNLOAD", 
      "conversionTrackerType": "APP_CONVERSION", 
      "userRevenueValue": "100", 
      "excludeFromBidding": "FALSE", 
      "appId": "abc_1234", 
      "appPostbackUrl": {
        "clearFlag": "TRUE"
      }
    }, 
    {
      "xsi_type": "AppConversion", 
      "conversionTrackerId": "1193198", 
      "conversionTrackerName": "APP_ANDROID_IN_APP_PURCHASE_CONVERSION_TRACKER_EDIT", 
      "status": "ENABLED", 
      "category": "PURCHASE", 
      "conversionTrackerType": "APP_CONVERSION", 
      "userRevenueValue": "100", 
      "countingType": "MANY_PER_CLICK", 
      "measurementPeriod": "90"
    }
  ]
}

"""
SAMPLE RESPONSE = {
  "rval": {
    "ListReturnValue.Type": "ConversionTrackerReturnValue", 
    "Operation.Type": "SET", 
    "values": [
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "WebConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193194", 
          "conversionTrackerName": "WEB_CONVERSION_TRACKER_EDIT", 
          "status": "ENABLED", 
          "category": "PAGE_VIEW", 
          "conversionTrackerType": "WEB_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "MANY_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "30", 
          "snippet": "&lt;!-- Yahoo Code for your Conversion Page --&gt;\n&lt;script type=\"text/javascript\"&gt;\n    /* &lt;![CDATA[ */\n    var yahoo_conversion_id = 1000661;\n    var yahoo_conversion_label = \"XXXXXXXXXXXXXXXXXX\";\n    var yahoo_conversion_value = 100;\n    /* ]]&gt; */\n&lt;/script&gt;\n&lt;script type=\"text/javascript\" src=\"//s.yimg.jp/images/listing/tool/cv/conversion.js\"&gt;\n&lt;/script&gt;\n&lt;noscript&gt;\n    &lt;div style=\"display:inline;\"&gt;\n        &lt;img height=\"1\" width=\"1\" style=\"border-style:none;\" alt=\"\" src=\"//b91.yahoo.co.jp/pagead/conversion/1000661/?value=100&amp;label=XXXXXXXXXXXXXXXXXX&amp;guid=ON&amp;script=0&amp;disvt=true\"/&gt;\n    &lt;/div&gt;\n&lt;/noscript&gt;", 
          "markupLanguage": "HTML", 
          "trackingCodeType": "WEBPAGE"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "WebConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193195", 
          "conversionTrackerName": "CALL_CONVERSION_TRACKER_EDIT", 
          "status": "DISABLED", 
          "category": "DEFAULT", 
          "conversionTrackerType": "WEB_CONVERSION", 
          "userRevenueValue": "200", 
          "countingType": "ONE_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "30", 
          "snippet": "&lt;!-- Yahoo Code for your Conversion Page In your html page, add the snippet and call\nyahoo_report_conversion when someone clicks on the phone number link or button. --&gt;\n&lt;script type=\"text/javascript\"&gt;\n    /* &lt;![CDATA[ */\n    yahoo_snippet_vars = function() {\n        var w = window;\n        w.yahoo_conversion_id = 1000661;\n        w.yahoo_conversion_label = \"XXXXXXXXXXXXXXXXXX\";\n        w.yahoo_conversion_value = 200;\n        w.yahoo_remarketing_only = false;\n    }\n    // IF YOU CHANGE THE CODE BELOW, THIS CONVERSION TAG MAY NOT WORK.\n    yahoo_report_conversion = function(url) {\n        yahoo_snippet_vars();\n        window.yahoo_conversion_format = \"3\";\n        window.yahoo_is_call = true;\n        var opt = new Object();\n        opt.onload_callback = function() {\n            if (typeof(url) != 'undefined') {\n                window.location = url;\n            }\n        }\n        var conv_handler = window['yahoo_trackConversion'];\n        if (typeof(conv_handler) == 'function') {\n            conv_handler(opt);\n        }\n    }\n    /* ]]&gt; */\n&lt;/script&gt;\n&lt;script type=\"text/javascript\"\n        src=\"//s.yimg.jp/images/listing/tool/cv/conversion_async.js\"&gt;\n&lt;/script&gt;", 
          "markupLanguage": "HTML", 
          "trackingCodeType": "CLICK_TO_CALL"
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "AppConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193196", 
          "conversionTrackerName": "APP_ANDROID_DOWNLOAD_CONVERSION_TRACKER_EDIT", 
          "status": "ENABLED", 
          "category": "DOWNLOAD", 
          "conversionTrackerType": "APP_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "ONE_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "30", 
          "appId": "abc_1234", 
          "appPlatform": "ANDROID_MARKET", 
          "appConversionType": "DOWNLOAD", 
          "appPostbackUrl": ""
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "AppConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193197", 
          "conversionTrackerName": "APP_ANDROID_FIRST_OPEN_CONVERSION_TRACKER_EDIT", 
          "status": "ENABLED", 
          "category": "DOWNLOAD", 
          "conversionTrackerType": "APP_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "ONE_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "30", 
          "appId": "abc_1234", 
          "appPlatform": "ANDROID_MARKET", 
          "appConversionType": "FIRST_OPEN", 
          "snippetId": "1000661", 
          "snippetLabel": "XXXXXXXXXXXXXXXXXX", 
          "appPostbackUrl": ""
        }
      }, 
      {
        "operationSucceeded": "true", 
        "conversionTracker": {
          "xsi_type": "AppConversion", 
          "accountId": "SAMPLE-ACCOUNT-ID", 
          "conversionTrackerId": "1193198", 
          "conversionTrackerName": "APP_ANDROID_IN_APP_PURCHASE_CONVERSION_TRACKER_EDIT", 
          "status": "ENABLED", 
          "category": "PURCHASE", 
          "conversionTrackerType": "APP_CONVERSION", 
          "userRevenueValue": "100", 
          "countingType": "ONE_PER_CLICK", 
          "excludeFromBidding": "FALSE", 
          "measurementPeriod": "90", 
          "appPlatform": "ANDROID_MARKET", 
          "appConversionType": "IN_APP_PURCHASE", 
          "snippetId": "1000661", 
          "snippetLabel": "XXXXXXXXXXXXXXXXXX", 
          "appPostbackUrl": ""
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
