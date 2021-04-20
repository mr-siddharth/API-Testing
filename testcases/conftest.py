import pytest
from utils.logger import get_logger

@pytest.fixture(scope="session")
def logger():
    return get_logger()