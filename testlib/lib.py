import random
import config.config as config
import os

def get_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def get_random_email(domain="gmail.com", prefix="testuser_"):

    if prefix is None:
        prefix = ''

    return prefix + get_random_string() + f'@{domain}'


def get_base_url():
    env = os.environ.get('env')
    return config.HOSTS['env']
