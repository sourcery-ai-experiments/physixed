from collections.abc import Callable

import pint
import pytest

from ..pytools.utils import ureg_f


@pytest.fixture()
def registry()->Callable:
    """Create a registry."""
    def _registry(unit: str)->pint.Quantity:
        return ureg_f()(unit)

    return _registry

class TestPint:
    """Test all pint related functions."""
    @pytest.mark.parametrize(
        ("unit_str", "expected"),
        [
            ("meter", "meter"),
            ("meter per second", "meter/second"),
            ("second", "second"),
        ]
    )
    def test_units(self, registry:Callable, unit_str:str, expected:str)->None:
        """Check if units are correct.

        Args:
            registry: fixture to create unit registry
            unit_str: unit parsed in the registry fixture
            expected: expected outcome of the registry fixture

        """
        unit = registry(unit_str)
        assert unit.units == expected
