import testlib.api_requests as api

endpoint = 'products'


def get_all_products(expected_status=None, **kwargs):
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


def get_product_by_id(id, expected_status=None, **kwargs):
    response = api.get(endpoint=endpoint + f'/{id}', expected_status=expected_status)

    return response


def create_product(name, expected_status=None, **kwargs):
    payload = {'name': name}
    payload.update(**kwargs)

    response = api.post(endpoint=endpoint, json=payload, expected_status=expected_status)

    return response


def update_product(id, expected_status=None, **kwargs):
    payload = {}
    payload.update(**kwargs)

    response = api.put(endpoint=endpoint + f'/{id}', json=payload, expected_status=expected_status)

    return response

def delete_product(id, expected_status=None):
    payload = {"force": "true"}
    response = api.delete(endpoint=endpoint + f'/{id}', json=payload, expected_status=expected_status)

    return response