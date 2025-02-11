from collections.abc import Callable

import numpy as np
import pint
import pytest

from ..pytools import utils

# TODO: Clean up the files and make parametrize smaller


@pytest.fixture()
def registry() -> Callable:
    """Create a registry."""

    def _registry(unit: str) -> pint.Quantity:
        return utils.ureg_f()(unit)

    return _registry


class TestPintHappy:
    """Happy-path tests for all pint related functions."""

    @pytest.mark.parametrize(
        ("unit_str", "expected"),
        [
            ("meter", "meter"),
            ("meter per second", "meter/second"),
            ("second", "second"),
        ],
    )
    def test_ureg_happy(self, registry: Callable, unit_str: str, expected: str) -> None:
        """Check if units are correct.

        Args:
            registry (Callable): fixture to create unit registry
            unit_str (str): unit parsed in the registry fixture
            expected (str): expected outcome of the registry fixture

        """
        unit = registry(unit_str)
        assert unit.units == expected

    @pytest.mark.parametrize(
        ("input_tuple", "expected"),
        [
            (
                (
                    1,
                    "W/(m K)",
                ),
                (1, "W/K/m"),
            ),
            (
                (
                    None,
                    "W/(m K)",
                ),
                (np.nan, "W/K/m"),
            ),
            (
                None,
                (np.nan, ""),
            ),
            (
                (1, "W/(m K)", "W/(cm K)"),
                (0.01, "W/K/cm"),
            ),
            (
                (1, "W/(m K)", None),
                (1, "W/K/m"),
            ),
            (
                pint.UnitRegistry().Quantity(1.0, "(W/(m K))"),
                (1, "W/K/m"),
            ),
            (
                (
                    1.0,
                    " ",
                ),
                (1, ""),
            ),
            (
                (
                    1.0,
                    "",
                ),
                (1, ""),
            ),
            (
                (1.0,),
                (1, ""),
            ),
        ],
    )
    def test_value_parse_unit_happy(self, input_tuple: tuple, expected: tuple) -> None:
        """Test value parsing and unit conversion.

        Args:
            input_tuple (tuple): input tuple wwith input values
            expected (tuple): expected values

        """
        output = utils.value_parse_unit(input_tuple)
        assert f"{output.magnitude}" == str(float(expected[0]))
        assert f"{output.units:~C}" == expected[1]


class TestPintSad:
    """Sad-path tests for all pint related functions."""

    def test_ureg_sad(self, registry: Callable) -> None:
        """Test errorhandling of the defined pint unit registry.

        Args:
            registry (Callable): fixture that defines the unit registry

        """
        with pytest.raises(pint.UndefinedUnitError) as exp:
            registry("Rankine")
        assert str(exp.value) == "'Rankine' is not defined in the unit registry"

    def test_magnitude_sad(self) -> None:
        """Test errorhandling of the magnitude parsing."""
        with pytest.raises(TypeError) as exp:
            utils.value_parse_unit(("random", "meter"))
        assert str(exp.value) == f"int, float, ndarray expected, got {str}"

    def test_convert_2_quantitity(self) -> None:
        """Test errorhandling of the unit parsing."""
        with pytest.raises(TypeError) as exp:
            utils._try_convert_2_quantity((10, 10), 10)
        assert str(exp.value) == f"str expected, got {int}"
