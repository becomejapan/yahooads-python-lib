
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
