import uuid

from django.db import models


class Companies(models.Model):
    """
    This is just a placeholder starting point to ensure uniqueness of tanks per company and searchable when creating
    or removing tanks
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name
