import numpy as np
import pint
import pytest
from numpy.typing import NDArray

from ..pytools.lineplot import make_plot


@pytest.fixture()
def ureg() -> pint.UnitRegistry:
    """Create unit registry for testing."""
    return pint.UnitRegistry()


@pytest.mark.parametrize(
    ("x_data", "y_data"),
    [
        ([1, 2, 3], [4, 5, 6]),
        (np.array([1, 2, 3]), np.array([4, 5, 6])),
        ([0, 0, 0], [0, 0, 0]),
        (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100))),
    ],
)
def test_make_plot_happy(x_data: NDArray | list, y_data: NDArray | list, ureg: pytest.FixtureRequest) -> None:
    """
    Test the make_plot function with happy path inputs.

    Args:
        x_data (NDArray | list): The x-axis data for the plot.
        y_data (NDArray | list): The y-axis data for the plot.
        ureg (FixtureRequest): The unit registry for testing.

    """
    result = make_plot(x_data * ureg.m, y_data * ureg.kg)

    assert "<html>" in result
    assert "Plotly" in result


@pytest.mark.parametrize(
    ("x_data", "y_data"), [(None, [1, 2, 3]), ([1, 2, 3], None), ("string", [1, 2, 3]), ([1, 2, 3], "string")]
)
def test_make_plot_sad(x_data: str | list | None, y_data: str | list | None) -> None:
    """
    Test case for the make_plot function with invalid input types.

    Args:
        x_data (str | list | None): The x-axis data for the plot.
        y_data (str | list | None): The y-axis data for the plot.
        ureg (FixtureRequest): The unit registry for testing.

    Raises:
        TypeError: If the make_plot function does not raise a TypeError when given invalid input types.

    """
    with pytest.raises(TypeError):
        make_plot(x_data, y_data)
