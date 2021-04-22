from testlib.helpers.customers_api import get_all_customers

result = get_all_customers()
print(f'{len(result)}\n{result}')