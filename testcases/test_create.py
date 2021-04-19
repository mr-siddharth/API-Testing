import pytest
import testlib.helpers.customers as customers
from testlib.helpers import customers_db
from testlib import lib

class TestSmokeCreateCustomer:

    email = lib.get_random_email()
    password = lib.get_random_string()

    @pytest.fixture(scope="class")
    def response(self):
        response = customers.create_customer(email=self.email, password=self.password).json()
        return response

    def test_api_response(self, response):
        assert response['email'] == self.email, f'Create customer api returned wrong email. ' + \
                                           f"Expected Email: {self.email}. Email returned: {response['email']}"
        assert response['first_name'] == ''


    def test_db_entry(self, response):
        cust = customers_db.get_customer_by_email(self.email)
        assert len(cust) <= 1, "More than one customer with the same email!!!"
        cust = cust[0]

        id_in_api = response['id']
        id_in_db = cust['ID']

        assert id_in_api == id_in_db
