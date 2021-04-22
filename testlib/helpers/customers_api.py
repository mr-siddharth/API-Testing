import testlib.api_requests as api


endpoint = 'customers'


def create_customer(email, password, expected_status=None, **kwargs):
    payload = {'email': email, 'password': password}
    payload.update(**kwargs)

    response = api.post(endpoint=endpoint, json=payload, expected_status=expected_status)

    return response

def get_all_customers(expected_status=None, **kwargs):
    payload = {'per_page':'100'}
    page = 1
    result = []
    while True:
        payload['page'] = str(page)
        response = api.get(endpoint=endpoint, json=payload, expected_status=expected_status).json()
        result.extend(response)
        if len(response) < int(payload['per_page']):
            break;
        page += 1

    return result

def get_customer_by_id(id, expected_status=None, **kwargs):
    response = api.get(endpoint=endpoint + f'/{id}', expected_status=expected_status)

    return response

def get_customer_by_email(email, expected_status=None, **kwargs):
    response = api.get(endpoint=endpoint, json={'email': email}, expected_status=expected_status)

    return response