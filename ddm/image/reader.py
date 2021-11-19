"""
Reads frame files
"""

from ddm.image.frame import Framestack
from pathlib import Path
from PIL import Image

def read_frame(img_path: Path) -> Image.Image:
    im = Image.open(img_path)

    return im


def read_experiment(data_path: Path, ext="pgm") -> Framestack:
    frames: list[Image.Image] = []

    for img_path in data_path.glob(f"*.{ext}"):
        frames.append(read_frame(img_path))

    return Framestack(frames)