import numpy as np


from px_main.pytools.utils import ureg, value_parse_unit


class FreeFallModel:
    def __init__(
        self,
        initial_h: tuple,
        initial_v: tuple,
        time_discretization_step: tuple | None = (0.01, "s"),
    ):
        self.initial_h = value_parse_unit(initial_h)
        self.initial_v = value_parse_unit(initial_v)
        self.time_discretization_step = value_parse_unit(time_discretization_step)

    def solve_model(self):
        g = value_parse_unit((9.81, "m/s**2"))
        results = {}
        time_discretization_step = self.time_discretization_step.m_as("s")
        initial_h = self.initial_h.m_as("m")
        initial_v = self.initial_v.m_as("m/s")

        time = np.array([0])
        height = np.array([initial_h])
        velocity = np.array([initial_v])

        for _i in range(100):
            time = np.append(time, time[-1] + time_discretization_step)
            height = np.append(height, height[-1] - velocity[-1] * time_discretization_step)
            velocity = np.append(velocity, velocity[-1] + g * time_discretization_step)

        results["time"] = time * ureg.Quantity(1, "s")
        results["height"] = time * ureg.Quantity(1, "m")
        results["velocity"] = time * ureg.Quantity(1, "m/s")
        return results
