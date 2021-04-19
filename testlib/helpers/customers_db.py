from testlib import db

def get_customer_by_email(email):
    query = f"SELECT * FROM wp_users WHERE user_email = '{email}'"
    return db.execute_select(query)
