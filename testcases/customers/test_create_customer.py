import pytest
import testlib.helpers.customers_api as customers
from testlib.helpers import customers_db
from testlib import lib


@pytest.mark.smoke
class TestSmokeCreateCustomer:
    email = lib.get_random_email()
    password = lib.get_random_string()

    @pytest.fixture(scope="class")
    def response(self, logger):
        logger.info(f"Creating customer with email id: {self.email}")
        response = customers.create_customer(email=self.email, password=self.password)
        logger.debug(f'Response Status: {response.status_code}')
        logger.debug(f'Response Body:\n{response.text}')
        return response.json()

    def test_api_response(self, response, logger):
        assert response['email'] == self.email, f'Create customer api returned wrong email. ' + \
                                                f"Expected Email: {self.email}. Email returned: {response['email']}"
        assert response['first_name'] == ''

        logger.info(f"Success: Creating customer with email id: {self.email}")

    def test_db_entry(self, response):
        cust = customers_db.get_customer_by_email(self.email)
        assert len(cust) != 0, "Customer not created in database."
        assert len(cust) <= 1, "More than one customer with the same email!!!"

        id_in_api = response['id']
        id_in_db = cust[0]['ID']

        assert id_in_api == id_in_db, "ID mismatch between api and database"


@pytest.mark.smoke
def test_cannot_create_customer_with_existing_email(logger):
    # Create a customer with non-existing email
    email = lib.get_random_email()
    password = lib.get_random_string()
    logger.info(f"Creating customer with email id: {email}")
    response = customers.create_customer(email=email, password=password)
    logger.debug(f'Response Status: {response.status_code}')
    logger.debug(f'Response Body:\n{response.text}')
    assert response.status_code == 201

    # Attempt to create a new customer with the same email
    logger.info(f"Creating customer again with the same email id: {email}")
    response = customers.create_customer(email=email, password=password, expected_status=400)
    logger.debug(f'Response Status: {response.status_code}')
    logger.debug(f'Response Body:\n{response.text}')

    # Verify that database has only one customer with this email
    cust = customers_db.get_customer_by_email(email)
    assert len(cust) != 0, "Customer not created in database."
    assert len(cust) == 1, "More than one customer with the same email!!!"
