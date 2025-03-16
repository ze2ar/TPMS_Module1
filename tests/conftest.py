import pytest

from core.logger import logger


@pytest.fixture(autouse=True, scope="session")
def setup_logger():
    logger.info("=== Start test session ===")

    yield

    logger.info("=== End test session ===")
