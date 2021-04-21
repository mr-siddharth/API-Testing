from testlib import db


def get_customer_by_email(email):
    query = f"SELECT * FROM wp_users WHERE user_email = '{email}'"
    return db.execute_select(query)


def get_all_customers(email, limit=None):
    query = 'SELECT * FROM wp_users'

    if limit:
        query += f' LIMIT {limit}'

    return db.execute_select(query)


def get_all_customer_count():
    return db.execute_select('SELECT COUNT(*) FROM wp_users')[0]['COUNT(*)']


def get_random_customer():
    return db.execute_select('SELECT * FROM wp_users ORDER BY RAND() LIMIT 1')[0]