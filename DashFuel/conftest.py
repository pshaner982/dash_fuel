import pytest
from faker import Faker
from django.test import Client
from app.models.fixtures import *

fake = Faker("en_US")
__all__ = [
    "faker",
    "client",
    "sample_company",
    "mock_company",
    "sample_tank",
    "mock_tank",
    "mock_tank_volume",
]


@pytest.fixture(scope="session")
def faker():
    """Provides a Faker instance for generating fake data."""
    return Faker("en_US")


@pytest.fixture
def client():
    return Client()
