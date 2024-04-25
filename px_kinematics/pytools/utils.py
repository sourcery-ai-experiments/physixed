import numpy as np
import pint

from px_main.pytools.utils import value_parse_unit


class FreeFallModel:
    """Physical model to simulate free fall.

    Attributes
        initial_h (tuple): the initial height of the object with unit.
        initial_v (tuple): the initial velocity of the object with unit.
        time_discretization_step (tuple): time step with unit.

    """

    def __init__(
        self,
        initial_h: tuple,
        initial_v: tuple,
        time_discretization_step: tuple | None = (0.01, "s"),
    ):
        self.initial_h = value_parse_unit(initial_h)
        self.initial_v = value_parse_unit(initial_v)
        self.time_discretization_step = value_parse_unit(time_discretization_step)
        self.g = value_parse_unit((9.81, "m/s**2"))

    def solve_endtime(self) -> pint.Quantity:
        """Calculate time till object hits the ground.

        Returns
            pint.Quantity: time till the object hits the ground.

        """
        return -self.initial_v / self.g + np.sqrt(self.initial_v**2 / self.g**2 + 2 * self.initial_h / self.g)

    def solve_eq(self) -> dict:
        """Calculate the height and velocity for every time step.

        Returns
            dict: resulting values for height, velocity and time for every time step.

        """
        end_time = self.solve_endtime()
        time = value_parse_unit((np.arange(0, end_time.magnitude, self.time_discretization_step.magnitude), "s"))
        height = self.initial_h - self.initial_v * time - 0.5 * self.g * time**2
        velocity = self.initial_v + self.g * time

        return {"height": height, "velocity": velocity, "time": time}
