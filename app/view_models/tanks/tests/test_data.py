import pytest

from app.models.tanks import Tanks
from app.models.tanks_volumes import TankVolume
from app.view_models.tanks.data import (
    get_all_tank_volumes_for_tank,
    get_tank_by_id,
    get_tank_volume_by_id,
)
from app.view_models.tanks.exceptions import TankException


class TestGetTank:
    @pytest.mark.parametrize(
        "tank_id",
        [None, "cats", [1, 2, 3], {"cats", "dogs"}, False, 55, {"cats": "dogs"}],
    )
    def test_it_raises_tank_error_when_invalid_id_is_provided(self, tank_id):
        with pytest.raises(TankException, match="Invalid tank id"):
            get_tank_by_id(tank_id)

    @pytest.mark.django_db
    def test_it_raises_tank_error_when_tank_does_not_exist(self, mock_tank):
        with pytest.raises(TankException) as err:
            _response = get_tank_by_id(mock_tank.id)
        assert "does not exist" in str(err.value), f"{_response}, {err.value}"

    @pytest.mark.django_db
    def test_it_returns_a_valid_tank_when_id_is_valid(self, sample_tank):
        _response = get_tank_by_id(sample_tank.id)
        assert isinstance(_response, Tanks), f"{type(_response)}, {_response}"
        assert _response.id == sample_tank.id, f"{_response.id}, {_response.id}"
        assert _response.name == sample_tank.name, f"{_response.name}, {_response.name}"


class TestGetTankVolumesForTank:
    @pytest.mark.parametrize(
        "tank_id",
        [None, "cats", [1, 2, 3], {"cats", "dogs"}, False, 55, {"cats": "dogs"}],
    )
    def test_it_raises_tank_error_when_invalid_id_is_provided(self, tank_id):
        with pytest.raises(TankException, match="Invalid tank volume id"):
            get_tank_volume_by_id(tank_id)

    @pytest.mark.django_db
    def test_it_raises_tank_error_when_tank_volume_does_not_exist(self, mock_tank):
        with pytest.raises(TankException) as err:
            _response = get_tank_volume_by_id(mock_tank.id)
        assert "does not exist" in str(err.value), f"{_response}, {err.value}"

    @pytest.mark.django_db
    def test_it_returns_a_valid_tank_volume_when_id_is_valid(self, sample_tank_volume):
        _response = get_tank_volume_by_id(sample_tank_volume.id)
        assert isinstance(_response, TankVolume), f"{type(_response)}, {_response}"
        assert _response.id == sample_tank_volume.id, f"{_response.id}, {_response.id}"
        assert (
            _response.volume == sample_tank_volume.volume
        ), f"{_response.volume}, {_response.volume}"


class TestGetAllTankVolumesForTank:
    @pytest.mark.parametrize(
        "tank_id",
        [None, "cats", [1, 2, 3], {"cats", "dogs"}, False, 55, {"cats": "dogs"}],
    )
    def test_it_raises_tank_error_when_invalid_id_is_provided(self, tank_id):
        with pytest.raises(TankException, match="Invalid tank id"):
            get_all_tank_volumes_for_tank(tank_id)

    @pytest.mark.django_db
    def test_it_returns_empty_list_when_tank_does_not_exist(self, mock_tank):
        _response = get_all_tank_volumes_for_tank(mock_tank.id)
        assert isinstance(_response, list), f"{type(_response)}, {_response}"
        assert _response == [], f"{_response}"

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "sample_tank_with_multiple_volumes", [{"count": 4}], indirect=True
    )
    def test_it_returns_list_of_records_when_tank_has_multiple_volumes(
        self, sample_tank_with_multiple_volumes
    ):
        _expected_ids = [x.id for x in sample_tank_with_multiple_volumes]
        _first_tank = sample_tank_with_multiple_volumes[0]
        _response = get_all_tank_volumes_for_tank(_first_tank.tank.id)
        assert isinstance(_response, list), f"{type(_response)}, {_response}"
        assert len(_response) == len(sample_tank_with_multiple_volumes)
        _received_ids = [str(x.id) for x in _response]
        assert sorted(_received_ids) == sorted(_expected_ids)
