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

import logging
from yahooads import promotionalads

ACCOUNT_ID = "SAMPLE-ACCOUNT-ID"

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def update_keywords(adgroup_criterion_service):
    operations = {
        "operator": "SET",
        "accountId": ACCOUNT_ID,
        "operand": [{
            "xsi_type": "BiddableAdGroupCriterion",
            "campaignId": "1000000001",
            "adGroupId": "1000000001",
            "criterionUse": "BIDDABLE",
            "criterion": {
                "xsi_type": "Keyword",
                "criterionId": "1000000002",
                "type": "KEYWORD"
            },
            "advancedUrl": "http://www.yahoo.co.jp",
            "additionalAdvancedUrls": {
                "isRemove": "TRUE"
            },
            "advancedMobileUrl": "http://mobile.yahoo.co.jp",
            "additionalAdvancedMobileUrls": {
                "additionalAdvancedMobileUrl": [
                    {
                        "url": "http://mobile.yahoo.co.jp/url1"
                    },
                    {
                        "url": "http://mobile.yahoo.co.jp/url2"
                    },
                    {
                        "url": "http://mobile.yahoo.co.jp/url3"
                    }
                ]
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
        },
            {
            "xsi_type": "BiddableAdGroupCriterion",
            "campaignId": "100000001",
            "adGroupId": "100000001",
            "criterionUse": "BIDDABLE",
            "criterion": {
                "xsi_type": "Keyword",
                "criterionId": "1000000003",
                "type": "KEYWORD"
            },
            "customParameters": {
                "isRemove": "TRUE"
            },
            "advanced": "TRUE"
        }]
    }

    response = adgroup_criterion_service.mutate(operations)
    print response


def get_keywords(adgroup_criterion_service):
    selector = {
        "accountId": ACCOUNT_ID,
        "criterionUse": "BIDDABLE",
        "paging": {
            "startIndex": 1,
            "numberResults": 100,
        },
    }
    response = adgroup_criterion_service.get(selector)
    print response


def main(client):
    service = client.GetService('AdGroupCriterionService')
    update_keywords(service)
    get_keywords(service)

if __name__ == '__main__':
    promotionalads_client = promotionalads.PromotionalAdsClient.LoadFromConfiguration()
    main(promotionalads_client)

