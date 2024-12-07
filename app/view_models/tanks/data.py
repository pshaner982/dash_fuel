import uuid

from django.core.exceptions import ObjectDoesNotExist

from app.models import TankVolume
from app.models.tanks import Tanks
from app.view_models.tanks.exceptions import TankException


def get_tank_by_id(tank_id) -> Tanks:
    try:
        if not isinstance(tank_id, uuid.UUID):
            raise TankException(f"Invalid tank id: {tank_id}")
        _tank = Tanks.objects.get(id=tank_id)
        return _tank
    except ObjectDoesNotExist:
        raise TankException(f"Tank {tank_id} does not exist.")


def get_tank_volume_by_id(tank_volume_id) -> TankVolume:
    try:
        if not isinstance(tank_volume_id, uuid.UUID):
            raise TankException(f"Invalid tank volume id: {tank_volume_id}")
        _tank_volume = TankVolume.objects.get(id=tank_volume_id)
        return _tank_volume
    except ObjectDoesNotExist:
        raise TankException(f"Tank volume {tank_volume_id} does not exist.")


def get_all_tank_volumes_for_tank(tank_id: uuid) -> list[TankVolume]:
    if not isinstance(tank_id, uuid.UUID):
        raise TankException(f"Invalid tank id: {tank_id}")
    _tank_volumes = TankVolume.objects.filter(tank=tank_id).order_by("timestamp")
    return list(_tank_volumes)
