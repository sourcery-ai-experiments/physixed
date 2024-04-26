import pytest
from pint import Quantity

from ..pytools.utils import FreeFallModel


@pytest.fixture()
def free_fall_model() -> FreeFallModel:
    """Create the free fall instance.

    Returns
       FreeFallModel: A free fall model instance

    """
    return FreeFallModel((10, "m"), (0, "m/s"))


class TestFreeFallHappy:
    """Happy path testing for free fall model."""

    def test_solve_endtime(self, free_fall_model: FreeFallModel) -> None:
        """Test end time method of free fall object.

        Args:
            free_fall_model (FreeFallModel): Fixture to create the free fall object

        """

        assert isinstance(free_fall_model.solve_endtime(), Quantity)
        assert free_fall_model.solve_endtime().magnitude == pytest.approx(1.43, rel=0.1)
        assert free_fall_model.solve_endtime().units == "second"

    def test_solve(self, free_fall_model: FreeFallModel) -> None:
        """Test model solve of free fall object.

        Args:
            free_fall_model: Fixture to create the free fall object

        """

        assert isinstance(free_fall_model.solve_eq(), dict)
