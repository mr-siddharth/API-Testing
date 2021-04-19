import mysql.connector
import config.config as config

def create_connection():
    global conn
    global cursor
    db_config = config.get_db_config()
    conn = mysql.connector.connect(
        host=db_config['hostname'],
        port=db_config['port'],
        user=db_config['user'],
        password=db_config['password'],
        database='wordpress'
    )

    cursor = conn.cursor(dictionary=True)

def execute_select(sql):
    create_connection()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    finally:
        conn.close()

    return result