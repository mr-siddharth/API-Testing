import testlib.api_requests as api

endpoint = 'customers'


def create_customer(email, password, **kwargs):
    payload = {'email': email, 'password': password}
    payload.update(**kwargs)

    response = api.post(endpoint=endpoint, json=payload)

    return response
