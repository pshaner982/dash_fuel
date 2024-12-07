from django.db import models
from django.utils import timezone
import uuid
from app.models.tanks import Tanks


class TankVolume(models.Model):
    """Serves as a time based table this will also store volume as a float to enable more granular data."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tank = models.ForeignKey(Tanks, on_delete=models.CASCADE, related_name="volumes")
    volume = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
            "tank",
            "timestamp",
        )

    def __repr__(self):
        return f"{self.tank.name}, {self.volume}: {self.timestamp}"
