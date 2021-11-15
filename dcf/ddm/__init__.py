from typing import Callable
from dcf.constants import k_B

from math import pi


def make_diffusion_coefficient_calculator(viscosity: float, temperature: float) -> Callable[[float], float]:
    def diffusion_coefficient_calculator(diameter: float) -> float:
        return k_B * temperature / (3 * pi * viscosity * diameter) * 1.0e12

    return diffusion_coefficient_calculator


def make_diameter_calculator(viscosity: float, temperature: float, pix2mum: float, framerate: float) -> Callable[[float], float]:
    scaling_factor = (pix2mum ** 2) * framerate

    def diameter_calculator(diffusion_coefficient: float) -> float:
        return k_B * temperature / (3 * pi * viscosity * scaling_factor * diffusion_coefficient) * 1.0e12

    return diameter_calculator