

def create_new_tank_for_company(company_id: str, tank_name: str, initial_volume: int = 0):
    """Created to isolate the creation of a new tank for an existing company.

    Will ensure uniqueness in the tank name for the company catching the db error, and generating
    a user actionable error.
    Args:
        company_id (str): UUID of the company that the tank will be associated with.
        tank_name (str): User friendly way to identify the tank.
        initial_volume (int, optional): Initial volume of the tank. Defaults to 0.

    Notes:
        Enhancement might be to increment the provided name if a table with that
        name already exist.
    """
    ...


def update_existing_tank(tank_id: str, updated_tank_details: dict):
    """Used to change elements of an existing tank, should not be used to update the volume records
    of tank.

    Should not be used to update the volume records of an existing tank.

    Args:
        tank_id (str): UUID of the tank to update.
        updated_tank_details (dict): Dictionary of tank details, that will be changed.
    """


