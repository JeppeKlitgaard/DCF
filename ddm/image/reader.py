"""
Reads frame files
"""

from ddm.image.frame import Frame, Framestack
from pathlib import Path
from PIL import Image

def read_frame(img_path: Path) -> Frame:
    im = Image.open(img_path)

    return im


def read_experiment(data_path: Path, ext="pgm") -> Framestack:
    stack: Framestack = []

    for img_path in data_path.glob(f"*.{ext}"):
        stack.append(read_frame(img_path))

    return stack
