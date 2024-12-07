import random
from uuid import uuid4

import pytest
import pytz

from app.models.tanks import Tanks
from app.models.tanks_volumes import TankVolume

__all__ = [
    "mock_tank",
    "sample_tank",
    "mock_tank_volume",
    "sample_tank_volume",
    "sample_tank_with_multiple_volumes",
]


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
def mock_tank_volume(faker):
    """Fixture to create a mock TankVolume instance."""
    return TankVolume(
        id=faker.uuid4(),
        tank_id=uuid4(),
        volume=100,
    )


@pytest.fixture
@pytest.mark.django_db
def sample_tank_volume(sample_tank, faker):
    """Fixture to create and save a related company and tank instance to the test database."""
    tank = sample_tank
    tank = TankVolume.objects.create(
        tank=tank,
        volume=faker.pyfloat(positive=True, right_digits=2),
        timestamp=faker.date_time_between(
            start_date=f"-{random.randint(1, 365)}d", end_date="-1d", tzinfo=pytz.UTC
        ),
    )
    return tank


@pytest.fixture
@pytest.mark.django_db
def sample_tank_with_multiple_volumes(sample_tank, faker, request):
    _count = request.param.get("count") if hasattr(request, "param") else 5
    _expected_responses = []
    for _ in range(_count):
        _record = TankVolume.objects.create(
            id=faker.uuid4(),
            tank=sample_tank,
            volume=faker.pyfloat(positive=True, right_digits=2),
            timestamp=faker.date_time_between(
                start_date=f"-{random.randint(1, 365)}d",
                end_date="-1d",
                tzinfo=pytz.UTC,
            ),
        )
        _expected_responses.append(_record)
    return _expected_responses
