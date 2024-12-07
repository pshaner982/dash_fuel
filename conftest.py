import pytest
from django.test import Client
from faker import Faker

from app.models.fixtures import (
    mock_company, mock_tank, mock_tank_volume, sample_company, sample_tank, sample_tank_volume,
)

fake = Faker("en_US")
__all__ = [
    "faker",
    "client",
    "sample_company",
    "mock_company",
    "sample_tank",
    "sample_tank_volume",
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
