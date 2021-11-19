from dcf.constants import k_B

from math import pi


def diffusion_coefficient_calculator(diameter: float, viscosity: float, temperature: float) -> float:
    return k_B * temperature / (3 * pi * viscosity * diameter) * 1.0e12

def diameter_calculator(diffusion_coefficient: float, viscosity: float, temperature: float, pix2mum: float, framerate: float) -> float:
    scaling_factor = (pix2mum ** 2) * framerate
    diameter = k_B * temperature / (3 * pi * viscosity * scaling_factor * diffusion_coefficient) * 1.0e12

    return diameter
