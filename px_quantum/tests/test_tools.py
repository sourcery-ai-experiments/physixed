import pytest
import numpy as np
import re

from ..pytools.schroedinger import Schroedinger
from ..pytools.lineplot import make_plot


def test_ml2v():
    assert Schroedinger().get_ml2v().all() == np.zeros(100).all()


def test_eigenvalues():
    w, v = Schroedinger().get_w_v()

    assert len(w) == 10
    assert len(v) == 10


# Happy path tests with various realistic test values
@pytest.mark.parametrize(
    "x_data, y_data, x_label, y_label, test_id",
    [
        ([1, 2, 3], [4, 5, 6], "Time", "Value", "basic_linear"),
        ([0, 0.5, 1], [0, 0.25, 1], "Probability", "Outcome", "fractional_values"),
        ([-1, 0, 1], [1, 0, 1], "Position", "Magnitude", "includes_negative"),
        ([], [], "Empty X", "Empty Y", "empty_lists"),
    ],
    ids=["basic_linear", "fractional_values", "includes_negative", "empty_lists"],
)
def test_make_plot_happy_path(x_data, y_data, x_label, y_label, test_id):
    # Act
    result = make_plot(x_data, y_data, x_label, y_label)

    # Assert
    assert isinstance(result, str)
    assert "<html>" not in result  # Confirming full_html=False
    assert x_label in result
    assert y_label in result


@pytest.mark.parametrize(
    "x_data, y_data, x_label, y_label, test_id",
    [
        ([1], [1], "Single Point X", "Single Point Y", "single_point"),
        ([1, 2], [3], "Mismatched Lengths", "Mismatched", "mismatched_lengths"),
    ],
    ids=["single_point", "mismatched_lengths"],
)
def test_make_plot_edge_cases(x_data, y_data, x_label, y_label, test_id):
    if test_id == "mismatched_lengths":
        with pytest.raises(
            ValueError,
            match=re.escape(f"x of shape {np.shape(x_data)} and y of shape {np.shape(y_data)} are mismatched."),
        ):
            make_plot(x_data, y_data, x_label, y_label)
    else:
        result = make_plot(x_data, y_data, x_label, y_label)
        assert isinstance(result, str)
        assert x_label in result
        assert y_label in result
