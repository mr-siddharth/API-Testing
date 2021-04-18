import requests
import json
import testlib.lib


def post(endpoint, json, expected_status=200, **kwargs):

    baseurl = testlib.lib.get_base_url()
    response = requests.post(baseurl + endpoint, json=json, **kwargs)

    if response.status_code != expected_status:
        raise Exception(f"Expected Status:{expected_status}. Actual Status:{response.status_code}")
