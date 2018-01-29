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

"""Generates code samples which produce given SOAP request in documentation"""

import re
import xmltodict
import urllib2
import argparse
import json
import os
# noinspection PyPackageRequirements
# for PyCharm to ignore this
import yaml

from collections import OrderedDict
from datetime import datetime
from string import Template

from yahooads import promotionalads

config = {
    "API_VERSION": promotionalads.PROMOTIONALADS_API_VERSION,
    "RAW_DOC_URL": "https://raw.githubusercontent.com/yahoojp-marketing/sponsored-search-api-documents"
                   "/{version}/docs/en/api_reference/services/{service}.md",
    "DOC_URL": "https://github.com/yahoojp-marketing/sponsored-search-api-documents"
               "/blob/{version}/docs/en/api_reference/services/{service}.md",
    "SAMPLE_CODE_TEMPLATE": "sample_template.py.template",
    "SAMPLE_CONTEXT": "sample_context.yaml",
    "SAMPLE_OUT_DIR": "./",                   # Output file format SAMPLE_OUT_DIR/{service}/{service}_{operation}.py
    "API_SERVICES": [
        "AccountService",
        "AccountSharedService",
        "AccountTrackingUrlService",
        "AdGroupAdService",
        "AdGroupBidMultiplierService",
        "AdGroupCriterionService",
        "AdGroupFeedService",
        "AdGroupRetargetingListService",
        "AdGroupService",
        "BalanceService",
        "BidLandscapeService",
        "BiddingStrategyService",
        "CampaignCriterionService",
        "CampaignExportService",
        "CampaignFeedService",
        "CampaignRetargetingListService",
        "CampaignService",
        "CampaignSharedSetService",
        "CampaignTargetService",
        "ConversionTrackerService",
        "CustomerSyncService",
        "DictionaryService",
        "FeedFolderService",
        "FeedItemService",
        "KeywordEstimatorService",
        "LocationService",
        "ReportDefinitionService",
        "ReportService",
        "RetargetingListService",
        "SharedCriterionService",
        "TargetingIdeaService",
    ],
}


def extract_soap_messages(md_str, service):
    """
    Extract SOAP request/response pairs for each operation from <SERVICE>.md files in on-line documentation
    This relies on the format of the documentation:
        - ALL operations are listed under second-level headings (ie. ## <operation> )
        - xml segment immediately following the operation is a request (ignore the on-behalf request here)
        - ALL Response are proceeded by "Response Sample" text
        - xml segment immediately following "Response Sample" is the response for above request
    :param md_str:
    :param service:
    :return: returns list of operations [ { operation: "get", operand: OrderedDict(), response: OrderedDict() }, ... ]
    """
    pat = re.compile(r"""^\#\#\s+                     # starting with a ## - second headline in .md file
                        (?P<operation>.*?)$           # operation name matches to the end of line => operation
                        .*?                           # skip until ...
                        ```xml                        # The Request sample's xml portion is found
                        (?P<request_xml>.*?)          # match everything in xml => request_xml
                        ```                           # until the closing delimiter is found
                        .*?                           # skip until ...
                        Response                      # Response Sample section found
                        .*?                           # skip until ...
                        ```xml                        # The Response sample's xml portion is found
                        (?P<response_xml>.*?)         # match everything in xml => response_xml
                        ```                           # until the closing delimiter is found
                    """, re.VERBOSE | re.DOTALL | re.MULTILINE)
    operations = []
    try:
        xml_extract = [g.groupdict() for g in pat.finditer(md_str)]
        print "Extracting operand/response from\t{}:[{}]".format(service,
                                                                 "| ".join(p["operation"].strip() for p in xml_extract))
        for p in xml_extract:
            # perform some cleaning after pattern match
            op, req_xml, resp_xml = (p[label].strip() for label in ["operation", "request_xml", "response_xml"])
            operand = extract_operand(req_xml, op, service)
            if not operand:  # Skip operation if operand was not parsed
                continue
            response = extract_operand(resp_xml, op, service, request=False)
            operations.append({"operation": op,
                               "operand": operand,
                               "response": response})
        return operations
    except Exception as e:
        print "\tCouldn't extract operations from .md file exception {}".format(e)
        return operations


def extract_operand(soap_xml, operation, service, request=True):
    """
    Convert SOAP XML to dict and extract operand corresponding to the operation
    :param soap_xml:
    :param operation: get | mutate (ADD | SET | REMOVE)
    :param service:
    :param request: True => request message, False => Response message
    :return: dict containing :
                 request - the selector (for get) or the operations (ADD | SET | REMOVE)
                 response - getResponse (for get) or mutateResponse for (ADD | SET | REMOVE)
    """
    # Clean up known issues with documentation XML files, so that the xmltodict.parse() won't fail
    # 1. remove ns1: => xmltodict.parse() will have "ns1:" prefix for all tags/keys otherwise. Attempt to rectify this
    #    with namespace aware parsing doesn't work well yet.
    # 2. some SOAP messages have "soapenv" instead of "SOAP-ENV" expected in extracting soap_body
    # 3. Erroneous spaces in some attributes (/feedAttributeName /placeholdeType) throws off the xmltodict.parse()
    soap_xml = soap_xml.replace("soapenv", "SOAP-ENV") \
                       .replace(":feed AttributeName", ":feedAttributeName") \
                       .replace(":placeholde Type", ":placeholderType")
    # 5. Correct some ill-formed request header tags in SOAP messages
    #    <ns1:RequestHeader> ... <ns1:RequestHeader>  => <ns1:RequestHeader> ... </ns1:RequestHeader>
    soap_xml = re.sub(r"<(ns[1-9]:)RequestHeader>(\s+</SOAP-ENV:Header>)", r"</\1RequestHeader>\2", soap_xml)

    def fix_xsi_type(_, key, value):
        """replace @xsi:type keys created by xmltodict with xsi_type expected by promotionalads-python-lib"""
        if key == "@xsi:type":
            return "xsi_type", re.sub("^ns\d+:", "", value)  # stip-off namespaces from value
        elif key.startswith("@xmlns"):  # Remove node attributes if any
            return None
        else:
            return key, value
    namespaces = {'ns1': '', 'ns2': ''}  # Remove any namespace references from Keys
    try:
        operation_dict = xmltodict.parse(soap_xml, postprocessor=fix_xsi_type, namespaces=namespaces)
    except Exception as e:
        print "\tCouldn't parse XML '{}:{}' exception {}".format(service, operation, e)
        return {}
    soap_body = operation_dict["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]

    try:
        if operation.startswith("mutate"):
            return soap_body["mutate"]["operations"] if request else soap_body["mutateResponse"]
        elif operation.startswith("get"):
            # res = soap_body["get"]["selector"]
            # in case of DictionaryService op = [ getDisapprovalReason | getGeographicLocation]
            return soap_body[operation]["selector"] if request else soap_body[operation+"Response"]
        else:
            print "\tUnrecognized operation {}".format(operation)
            return {}
    except Exception as e:
        # Handle MORE oddities in the documentation here!
        if (service == "ReportDefinitionService" and operation == "getReportFields") or \
                (service == "LocationService" and operation == "get"):  # has no selector
            return soap_body[operation]
        elif service == "CampaignTargetService" and operation == "get":
            return soap_body["mutateResponse"]
        else:
            print "\tCouldn't extract operation '{}:{}' exception {}".format(service, operation, e)
            return {}


def get_operations_from_md_file(service, version="master"):
    """
    Use online API documentation file(s) to extract operations and corresponding operands to generate sample API code
    :param service:
    :param version:
    :return:
    """
    raw_url = config["RAW_DOC_URL"].format(version=version, service=service)
    try:
        print "Reading SOAP messages from API reference : {}\n{}".format(service, raw_url)
        md_txt = urllib2.urlopen(raw_url).read()
        operations = extract_soap_messages(md_txt, service)
        return operations
    except Exception as e:
        print "Couldn't read from {} : {}".format(raw_url, e)
        return []


def generate_samples(service, operation, version, code_template, output):
    params = {  # following fields are expected in the code template
        "service": service,
        "operation": operation["operation"],
        "operand": json.dumps(operation["operand"], indent=2),
        "response": json.dumps(operation["response"], indent=2),
        "generator": os.path.basename(__file__),
        "template": code_template,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "url": config["DOC_URL"].format(version=version, service=service)
    }

    # get code template to generate the code sample
    template = Template(open(code_template).read())
    ex = template.substitute(params)
    of_name = "{}_{}.py".format(service, operation["operation"].replace(" ", "").replace(")", "").replace("(", "_"))
    of = open(os.path.join(output, of_name), "w")
    of.write(ex)


def update_operand_from_context(operand, context):
    """Updates and operand with example context parameters accountId, campaignId, adgroupId in the operand are
    replaced with the values in the context. Use OrderedDict to preserve the dict ordering for readable sample code.
    :param operand:
    :param context:
    :return:
    """
    if isinstance(operand, (dict, OrderedDict)):
        new_operand = OrderedDict()
        for k, v in operand.items():
            if k in context.keys():
                new_operand[k] = context[k]
            else:
                new_operand[k] = update_operand_from_context(v, context)
        return new_operand
    elif isinstance(operand, list):
        new_operand = []
        for v in operand:
            new_operand.append(update_operand_from_context(v, context))
        return new_operand
    elif not operand:
        return ""   # return empty string for None operand
    else:
        return operand


def read_context(context_file, context_key="example_context"):
    """
    Read Example context from YAML file
    :param context_file:
    :param context_key:
    :return:
    """
    try:
        context_data = yaml.safe_load(open(context_file))
        return context_data[context_key]
    except Exception as e:
        print("Error loading context parameters from file '{}' @ key '{}'\n"
              "Error {}".format(context_file, context_key, e))
        return {}


def main():
    cmd_parser = argparse.ArgumentParser()
    cmd_parser.add_argument('-s', '--services', help='API services to generate code', required=False, nargs='+',
                            default=config["API_SERVICES"])
    cmd_parser.add_argument('-v', '--api-version', help='API version to use', required=False,
                            default=config["API_VERSION"])
    cmd_parser.add_argument('-t', '--template', help='Sample code template', required=False,
                            default=config["SAMPLE_CODE_TEMPLATE"])
    cmd_parser.add_argument('-c', '--context', help='Sample code context file', required=False,
                            default=config["SAMPLE_CONTEXT"])
    cmd_parser.add_argument('-o', '--output-dir', help='Output directory for samples', required=False,
                            default=config["SAMPLE_OUT_DIR"])
    args = cmd_parser.parse_args()

    context = read_context(args.context)
    for service in args.services:
        try:
            if not os.path.exists(service):
                os.makedirs(service)
            output = os.path.join(args.output_dir, service)
            operations = get_operations_from_md_file(service, args.api_version)
            print "Generating code sample(s)\t\t\t{}:[{}]".format(service,
                                                                  "| ".join(p["operation"] for p in operations))
            for operation in operations:
                if context:
                    operation["operand"] = update_operand_from_context(operation["operand"], context)
                    operation["response"] = update_operand_from_context(operation["response"], context)
                generate_samples(service, operation, args.api_version, args.template, output)
        except Exception as e:
            print("Failed to generate example sample code for service '{}'\nError {}".format(service, e))

if __name__ == '__main__':
    main()
