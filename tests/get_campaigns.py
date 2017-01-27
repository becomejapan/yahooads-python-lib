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
from yahooads import promotionalads, util

ACCOUNT_ID = "SAMPLE-ACCOUNT-ID"
CAMPAIGN_ID = "SAMPLE-CAMPAIGN-ID"

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def main(client):
    service = client.GetService('CampaignService')
    # Example API use
    # 1. Using python dicts
    selector = {'accountId': ACCOUNT_ID,
                'campaignIds': [CAMPAIGN_ID]}
    response = service.get(selector)
    print response

    # 2. Using suds_client
    suds_client = service.suds_client
    selector = suds_client.factory.create("CampaignSelector")
    selector.accountId = ACCOUNT_ID
    selector.campaignIds = [CAMPAIGN_ID]
    response2 = service.get(selector)
    print response2

if __name__ == '__main__':
    promotionalads_client = promotionalads.PromotionalAdsClient.LoadFromConfiguration()
    logging.getLogger('suds.client').removeFilter(util.SudsCredentialsFilter)
    # logging.getLogger('suds.transport.http').removeFilter(util.TransportCredentialsFilter)
    main(promotionalads_client)
