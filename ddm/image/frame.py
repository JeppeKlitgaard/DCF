from typing import Iterable
from PIL import Image
import numpy as np

CddmFormat = Iterable[tuple[np.ndarray]]
class Framestack:
    def __init__(self, frames: Iterable[Image.Image]):
        self.frames = frames

    def to_cddm_format(self) -> CddmFormat:
        for frame in self.frames:
            yield (np.array(frame),)



