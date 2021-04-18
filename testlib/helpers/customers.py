import testlib.requests as requests

endpoint = 'customers'


def create_customer(email, password, **kwargs):
    payload = {'email': email, 'password': password}
    payload.update(**kwargs)

    response = requests.post(endpoint=endpoint, json=payload)

    return response
