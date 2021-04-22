import pytest
import testlib.helpers.products_api as products_api
from testlib.helpers import products_db
from testlib import lib


@pytest.mark.smoke
class TestSmokeUpdateProduct:

    name = 'Test Product ' + lib.get_random_string()
    price = '49.99'
    updated_price = '69.99'

    @pytest.fixture(scope="class")
    def response(self, logger):
        #Create a new product
        logger.info(f"Creating product with name: {self.name} and price: {self.price}")
        response = products_api.create_product(name=self.name, regular_price=self.price)
        logger.debug(f'Response Status: {response.status_code}')
        logger.debug(f'Response Body:\n{response.text}')
        product = response.json()

        #Update the product price:
        response = products_api.update_product(product['id'], regular_price=self.updated_price)
        yield response.json()

        products_api.delete_product(product['id'])

    def test_api_response(self, response, logger):
        assert response['name'] == self.name, f'Create product api returned wrong name(slug). ' + \
                                              f"Expected Name: {self.name}. Name returned: {response['name']}"
        assert response['price'] == self.updated_price

        logger.info(f"Success: Update product with new price: {self.updated_price}, id: {response['id']}")

    def test_db_entry(self, response):
        price_in_db = products_db.get_product_price(response['id'])

        assert price_in_db == float(self.updated_price), "Price didn't get updated in database"


@pytest.mark.smoke
class TestSmokeDeleteProduct:

    name = 'Test Product ' + lib.get_random_string()
    price = '49.99'

    @pytest.fixture(scope="class")
    def response(self, logger):
        #Create a new product
        logger.info(f"Creating product with name: {self.name} and price: {self.price}")
        response = products_api.create_product(name=self.name, regular_price=self.price)
        logger.debug(f'Response Status: {response.status_code}')
        logger.debug(f'Response Body:\n{response.text}')

        product = response.json()

        #Delete the newly created product
        logger.info(f"Deleting the product with id: {product['id']}")
        response = products_api.delete_product(product['id'])

        return response.json()

    def test_deleted_product_api(self, response):
        response = products_api.get_product_by_id(response['id'], expected_status=404)

    def test_deleted_product_db(self,response):
        result = products_db.get_product_by_id(response['id'])
        assert len(result) == 0