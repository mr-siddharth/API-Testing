import os

HOSTS = {
    "test": "http://localhost:8888/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

CONSUMER_KEYS = {
    "test": "ck_aed107877c117d4ddc610b0c986af9e703e379a1",
    "dev": "",
    "prod": ""
}

CONSUMER_SECRETS = {
    "test": "cs_0035cd989fd9a84582f37f280528eb77443d0d3c",
    "dev": "",
    "prod": ""
}

DB_HOSTS = {
    "test_hostname": "localhost",
    "test_port": 8889,
    "dev": "",
    "prod": ""
}

DB_USERS = {
    "test": "root",
    "dev": "",
    "prod": ""
}

DB_PASSWORDS = {
    "test": "root",
    "dev": "",
    "prod": ""
}

def get_db_config():
    env = os.environ.get('env')
    config = {}
    config['hostname'] = DB_HOSTS[f'{env}_hostname']
    config['port'] = DB_HOSTS[f'{env}_port']
    config['user'] = DB_USERS[env]
    config['password'] = DB_PASSWORDS[env]

    return config