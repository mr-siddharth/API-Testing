import requests
import json
import testlib.lib
from requests_oauthlib import OAuth1
import config.config as config

def post(endpoint, json, expected_status=200, **kwargs):
    baseurl = testlib.lib.get_base_url()
    auth = OAuth1(config.CONSUMER_KEYS['test'], config.CONSUMER_SECRETS['test'])
    response = requests.post(baseurl + endpoint, json=json, timeout=10, auth=auth, **kwargs)
    return response

    # if response.status_code != expected_status:
    #     raise Exception(f"Expected Status:{expected_status}. Actual Status:{response.status_code}")
