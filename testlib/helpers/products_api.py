import testlib.api_requests as api

endpoint = 'products'


def get_all_products(expected_status=None, **kwargs):
    response = api.get(endpoint=endpoint + '?per_page=100', expected_status=expected_status)

    return response

def get_product_by_id(id, expected_status=None, **kwargs):
    response = api.get(endpoint=endpoint + f'/{id}', expected_status=expected_status)

    return response

def create_product(name, expected_status=None, **kwargs):
    payload = {'name': name}
    payload.update(**kwargs)

    response = api.post(endpoint=endpoint, json=payload, expected_status=expected_status)

    return response