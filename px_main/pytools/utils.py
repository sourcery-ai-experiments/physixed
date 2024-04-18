
import pint


def ureg_f() -> pint.UnitRegistry:
    """Provide ureg class.

    Provide the ureg class. Can be used to specify custom units.

    Returns
        pint.UnitRegistry: unit registry

    """

    ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit=True)
    ureg.setup_matplotlib()

    return ureg
