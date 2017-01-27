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

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)

ACCOUNT_ID = "SAMPLE-ACCOUNT-ID"
CAMPAIGN_ID = "SAMPLE-CAMPAIGN-ID"
ADGROUP_ID = "SAMPLE-ADGROUP-ID"


def main(client):
    service = client.GetService('AdGroupAdService')
    operation = {
        "accountId": ACCOUNT_ID,
        "operator": "ADD",
        "operand": [{
            "campaignId": CAMPAIGN_ID,
            "adGroupId": ADGROUP_ID,
            "adName": "Text Ad",
            "userStatus": "ACTIVE",
            "ad": {
                "xsi_type": "ExtendedTextAd",
                "type": "EXTENDED_TEXT_AD",
                "advancedUrl": "http://yahoo.co.jp/url",
                "advancedMobileUrl": "http://yahoo.co.jp/mobile/url",
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
                "displayUrl": "www.yahoo.co.jp",
                "headline": "Title",
                "description": "Descrption",
                "headline2": "Title2",
                "path1": "path1",
                "path2": "path2"
            }
        }]
    }

    response = service.mutate(operation)
    print response

if __name__ == '__main__':
    promotionalads_client = promotionalads.PromotionalAdsClient.LoadFromConfiguration()
    main(promotionalads_client)
