from testlib import db


def get_all_products(email, limit=None):
    query = 'SELECT * FROM wp_posts WHERE post_type = "product" and post_status = "publish"'

    if limit:
        query += f' LIMIT {limit}'

    return db.execute_select(query)


def get_product_by_id(id):
    query = f"SELECT * FROM wp_posts WHERE post_type = 'product' AND ID = {id}"
    return db.execute_select(query)


def get_all_products_count():
    return db.execute_select(
        'SELECT COUNT(*) FROM wp_posts WHERE post_type = "product" and post_status = "publish"'
    )[0]['COUNT(*)']


def get_random_product():
    return db.execute_select(
        'SELECT * FROM wp_posts WHERE post_type = "product" and post_status = "publish" ORDER BY RAND() LIMIT 1'
    )[0]

def get_product_price(id):
    return float(db.execute_select(
        f'SELECT min_price FROM wp_wc_product_meta_lookup WHERE product_id = {id}'
    )[0]['min_price'])