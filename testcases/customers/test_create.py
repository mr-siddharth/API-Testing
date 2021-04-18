import testlib.helpers.customers as customers
from testlib import lib


class TestCreateCustomer:

    def test_create_customer(self):
        response = customers.create_customer(email=lib.get_random_email(), password=lib.get_random_string())
        print(response)
