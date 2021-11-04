import os

HOSTS = {
    "test": "http://localhost:8888/wordpress/wp-json/wc/v3/",
    "dev": "",
    "prod": "",
    "docker": "http://192.168.80.239:8888/wp-json/wc/v3/"
}

CONSUMER_KEYS = {
    "test": "ck_aca9c2457becf884ae63256150089d3c379822f0",
    "docker": "ck_aed107877c117d4ddc610b0c986af9e703e379a1",
    "prod": ""
}

CONSUMER_SECRETS = {
    "test": "cs_7c3c920508eff6ccc878ef2acf4bd9f7a7d23d5f",
    "docker": "cs_0035cd989fd9a84582f37f280528eb77443d0d3c",
    "prod": ""
}

DB_HOSTS = {
    "test_hostname": "localhost",
    "test_port": 8889,
    "docker_hostname": "host.docker.internal",
    "docker_port": 8889,
    "dev": "",
    "prod": ""
}

DB_USERS = {
    "test": "root",
    "docker": "root",
    "prod": ""
}

DB_PASSWORDS = {
    "test": "root",
    "docker": "root",
    "prod": ""
}

def get_db_config():
    env = os.environ.get('ENV')
    config = {}
    config['hostname'] = DB_HOSTS[f'{env}_hostname']
    config['port'] = DB_HOSTS[f'{env}_port']
    config['user'] = DB_USERS[env]
    config['password'] = DB_PASSWORDS[env]

    return config