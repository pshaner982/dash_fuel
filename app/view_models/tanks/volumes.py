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


def update_tank_volume(
    volume_id: str, volume: float = None, time_stamp: datetime = None
) -> TankVolume:
    """Will update an existing volume record for a tank volume id. To enable updating and error
    correcting of volumes.

    Arguments are optional and will only update what has been provided.  If the argument is
    provided then will change the value on that record.
    Args:
         volume_id (str): the id of the tank volume id that will be updated.
         volume (float): the volume of the tank volume id that will be updated.
         time_stamp (datetime): the timestamp of the volume creation.
    Raises:
        TankException: the volume timestamp is in the future.
        TankException: the tank_volume record does not exist.
    """
    ...


def delete_tank_volume(volume_id: str) -> TankVolume:
    """Will remove an existing tank volume record.
    Args:
        volume_id (str): the id of the tank volume id that will be deleted.
    Raises:
        TankException: the volume id does not exist.
    Notes:
        This will be a hard delete.
    """
    ...
