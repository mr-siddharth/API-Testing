import pytest
import testlib.helpers.products_api as products_api
from testlib.helpers import products_db
from testlib import lib



class TestGetProduct:

    @pytest.mark.smoke
    def test_smoke_get_all_products_from_api(self, logger):
        response = products_api.get_all_products(expected_status=200)
        logger.info(f"Number of Products returned: {len(response)}")
        assert len(response) > 0

    @pytest.mark.smoke
    def test_match_id_email_in_db_and_api(self, logger):
        prod_in_db = products_db.get_random_product()
        logger.debug(f"Testing with product id:{prod_in_db['ID']}")
        prod_in_api = products_api.get_product_by_id(prod_in_db['ID']).json()
        assert prod_in_db['post_name'] == prod_in_api['slug']