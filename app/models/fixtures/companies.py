import pytest
from uuid import uuid4
from app.models.companies import Companies

__all__ = ["sample_company", "mock_company"]


@pytest.fixture
@pytest.mark.django_db
def sample_company(faker):
    """Fixture to create and save a Company instance to the test database."""
    company = Companies.objects.create(name=faker.company())
    return company


def mock_company(faker):
    """Fixture to create a Company instance."""
    return Companies(id=uuid4(), name=faker.company())
