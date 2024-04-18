import pytest


@pytest.fixture()
def freefall_factory():
    return FreeFall()

@pytest.mark.parametrize(
    ("h", "v", "t", "expected"),
    [
        (None, 0, 4, 78),
        (78, None, 4, 39),
        (None, 0, 4),
    ]
)
def test_freefall(freefall_factory, h, v, t, expected):
    result = free_fall_factory.calc_params(h,v,t)
    assert result == expected

