import pytest
import testlib.helpers.products_api as products_api
from testlib.helpers import products_db
from testlib import lib

@pytest.mark.smoke
class TestSmokeCreateProduct:

    name = 'Test Product ' + lib.get_random_string()
    price = '49.99'

    @pytest.fixture(scope="class")
    def response(self, logger):
        logger.info(f"Creating product with name: {self.name} and price: {self.price}")
        response = products_api.create_product(name=self.name, regular_price=self.price)
        logger.debug(f'Response Status: {response.status_code}')
        logger.debug(f'Response Body:\n{response.text}')
        return response.json()

    def test_api_response(self, response, logger):
        assert response['name'] == self.name, f'Create product api returned wrong name(slug). ' + \
                                                f"Expected Name: {self.name}. Name returned: {response['name']}"
        assert response['price'] == self.price

        logger.info(f"Success: Creating product with name: {self.name} and id: {response['id']}")

    def test_db_entry(self, response):
        prod = products_db.get_product_by_id(response['id'])
        assert len(prod) != 0, "Product not created in database."
        assert len(prod) <= 1, "More than one product with the same id!!!"

        name_in_api = response['name']
        name_in_db = prod[0]['post_title']

        price_in_api = float(response['price'])
        price_in_db = float(products_db.get_product_price(response['id']))

        assert name_in_api == name_in_db, "Name mismatch between api and database"
        assert price_in_api == price_in_db, "Price mismatch between api and database"