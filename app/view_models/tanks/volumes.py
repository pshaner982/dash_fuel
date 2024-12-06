from datetime import datetime
from app.models.tanks_volumes import TankVolume

def insert_tank_volume(volume: float, tank_id: str, time_stamp: datetime) -> TankVolume:
    """creates a new volume record for the tank provided.  This can be used to create a new
    volume even in the past.

    Will fail if the volume timestamp is in the future.
    Args:
        volume (float): the volume of the tank at time of creation.
        tank_id (str): the id of the tank volume is recorded for
        time_stamp (datetime): the timestamp of the volume creation.
    Raises:
        TankException is the volume timestamp is in the future.
        TankException if the tank does not exist.
    """
    ...

