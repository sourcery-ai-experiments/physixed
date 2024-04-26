import pytest

from ..forms import FreeFallForm


class TestFormHappy:
    """Happy path tests for kinematic forms."""

    def test_freefall_form_happy(self) -> None:
        """Test if freefall form is valid."""

    form = FreeFallForm(
        data={
            "distance": 10,
            "velocity": 10,
        }
    )

    assert form.is_valid()


class TestFormSad:
    """Sad-path tests for kinematic forms."""

    @pytest.mark.parametrize(
        ("distance", "velocity"),
        [
            (-1, 10),
            (10, -1),
        ],
    )
    def test_freefall_form_sad(self, distance: float, velocity: float) -> None:
        """Test if frefall form is invalid."""
        form = FreeFallForm(data={"distance": distance, "velocity": velocity})

        assert not form.is_valid()
