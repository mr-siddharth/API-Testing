import random
import config.config as config
import os
import string


def get_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def get_random_email(domain="gmail.com", prefix="testuser_"):
    if prefix is None:
        prefix = ''

    return prefix + get_random_string() + f'@{domain}'


def get_env():
    return os.environ.get('ENV')


def get_base_url():
    env = get_env()
    return config.HOSTS[env]
