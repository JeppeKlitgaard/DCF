from collections.abc import Callable
from dcf.constants import k_B
from math import pi, sin, radians

def make_particle_sizer(viscosity: float, temperature: float, wavelength: float, refractive_index: float) -> Callable[[float, float], float]:

    def particle_sizer(tau, theta):
        a = k_B * temperature * tau / (3 * pi * viscosity) * ((4 * pi * refractive_index) / wavelength * sin(radians(theta / 2))) ** 2

        return a

    return particle_sizer