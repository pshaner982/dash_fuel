import pytest
from uuid import uuid4

from app.models.tanks import Tanks
from app.models.tanks_volumes import TankVolume

__all__ = ["mock_tank", "sample_tank", "mock_tank_volume"]


@pytest.fixture
def mock_tank(faker):
    """Fixture to create a mock Tanks instance."""
    return Tanks(
        id=uuid4(),
        name=f"{faker.word()} Tank",
        company=None,  # Foreign key is not real in this fixture
        has_deleted=False,
    )


@pytest.fixture
@pytest.mark.django_db
def sample_tank(sample_company, faker):
    """Fixture to create and save a related company and tank instance to the test database."""
    company = sample_company
    tank = Tanks.objects.create(
        name=f"{faker.word()} Tank", company=company, has_deleted=False
    )
    return tank


@pytest.fixture
def mock_tank_volume():
    """Fixture to create a mock TankVolume instance."""
    return TankVolume(
        id=uuid4(),
        tank_id=uuid4(),
        volume=100,
    )
