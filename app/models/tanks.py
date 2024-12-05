import uuid

from django.db import models

from app.models.companies import Companies


class Tanks(models.Model):
    """
    There is constraint on uniqueness of tanks per company, this is to enable easier identification.
    Soft deleting the records to ensure reporting and historical data can be maintained.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=240)
    company = models.ForeignKey(
        Companies, on_delete=models.CASCADE, related_name="tanks"
    )
    has_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "company",
            "name",
        )

    def __repr__(self):
        return f"{self.company.name}, {self.name}"
