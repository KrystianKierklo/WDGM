import copy

from Lab02.BaseImage import BaseImage
from Lab03.GrayScaleTransform import GrayScaleTransform

class Thresholding(GrayScaleTransform):
    def __init__(self, path) -> None:
        super().__init__(path)

    def threshold(self, value: int) -> GrayScaleTransform:
        obraz = copy.deepcopy(self)
        obraz.data[obraz.data < value] = 0
        obraz.data[obraz.data >= value] = 255
        self.data = obraz.data
        return self
        pass