import pytest
import testlib.helpers.customers_api as customers_api
from testlib.helpers import customers_db
from testlib import lib

class TestGetCustomer:

    @pytest.mark.tcid30
    @pytest.mark.xfail
    def test_count_all_customers(self):
        # Get the count of customers returned by API
        response = customers_api.get_all_customers()
        customers_count_api = len(response)

        # Get the count of customers returned by DB
        customers_count_db = customers_db.get_all_customer_count() - 1

        assert customers_count_api == customers_count_db


    def test_match_id_email_in_db_and_api(self, logger):
        cust_in_db = customers_db.get_random_customer()
        logger.debug(f"Testing with user id:{cust_in_db['ID']}")
        cust_in_api = customers_api.get_customer_by_id(cust_in_db['ID']).json()
        assert cust_in_db['user_email'] == cust_in_api['email']
