from django.core.exceptions import ObjectDoesNotExist


def get_tank_by_id(tank_id):
    try:
        ...
    except ObjectDoesNotExist:
        raise TankError(f"Tank {tank_id} does not exist.")
