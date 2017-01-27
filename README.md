# yahooads-python-lib
Client library for Yahoo Promotional Ads SOAP API. Implementation took inspiration from google's client library
counterpart [googleads-python-lib](https://github.com/googleads/googleads-python-lib). It is based on suds SOAP library
and provide access to Promotional Ads API using python.

## Installation

1. Clone or download this library

2. Install with [setuptools](https://pypi.python.org/pypi/setuptools)

   `$ python setup.py build install`

3. Copy the [yahooads.yaml](https://github.com/becomejapan/promotionalads-python-lib/blob/master/yahooads.yaml)
   file to your home directory and fill in the account access credentials.

## Getting Started

The library reads the API authentication information from the `yahooads.yaml` under the default key `promotionalads`
The default location to look for this file is your home directory. You can override the default file and the key
where the authentication information can be found.

```python
# Using the default configuration file in home directory
client = promotionalads.PromotionalAdsClient.LoadFromConfiguration()

# Using the specified YAML file with a key
client = promotionalads.PromotionalAdsClient.LoadFromConfiguration(config_file='my_folder/config.yaml',
                                                                   key='credentials')
```

The use of library is similar to the `googleads-python-lib`. A service object can be created using `client.GetService`
method of client and `get`, `mutate` operations can be performed by passing the appropriate operands composed in the form
of python dictionaries as illustrated in the following example.

```python
ACCOUNT_ID = "SAMPLE-ACCOUNT-ID"
CAMPAIGN_ID = "SAMPLE-CAMPAIGN-ID"

service = client.GetService('CampaignService')
selector = {'accountId': ACCOUNT_ID,
            'campaignIds': [CAMPAIGN_ID]}
response = service.get(selector)
```

The library provide access to the underlaying suds client object through `suds_client` attribute. You can use suds
features in constructing the API calls as follows.

```python
service = client.GetService('CampaignService')
suds_client = service.suds_client
selector = suds_client.factory.create("CampaignSelector")
selector.accountId = ACCOUNT_ID
selector.campaignIds = [CAMPAIGN_ID]
response = service.get(selector)
```

For production use, Promotional Ads account ID can be set using the YAML file by setting `account_id` field. The
account can be changed at runtime as follows.

```python
client = yahooads.PromotionalAdsClient.LoadFromConfiguration()
client.setAccountId(new_account_id)
```


## Examples

The examples found in [examples](https://github.com/becomejapan/promotionalads-python-lib/tree/master/examples) folder
are auto generated by `api_reference_example_generator.py` using sample SOAP messages in the official
[Promotional Ads Reference](https://github.com/yahoojp-marketing/sponsored-search-api-documents).
Example generator uses `sample_context.yaml` file to replace the representative Ids in API Reference examples
(like `accountId`, `campaignId` `adgroupId` etc.), hence to generate runnable example code
the context file can be updated with account context (preferably of a test account).

## Logging SOAP messages

The library uses `suds` SOAP library which uses Python logging framework. The SOAP messages can be logged at client
and transport levels adding following code.
```python
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
```


## Future Work

1. Add testing
2. Sanitize example code (some examples contains unsupported fields due to out-dated reference SOAP messages)
3. Support for YDN

