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

