from Lab02.BaseImage import *
from Lab03.GrayScaleTransform import GrayScaleTransform
from Lab04.Histogram import *
#from Lab03.Image import Image
from enum import Enum
from typing import Any
import numpy as np
import math


class ImageDiffMethod(Enum):
    mse = 0
    rmse = 1



class ImageComparison(BaseImage):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def histogram(self) -> Histogram:
        return Histogram(self.data)
        pass

    def compare_to(self, other: GrayScaleTransform) -> float:

        image1 = GrayScaleTransform(self.data)

        image2 = GrayScaleTransform(other)

        hist1 = Histogram(image1.data).values
        hist2 = Histogram(other.data).values

        mse = 0

        for x in range(len(hist1)):
            mse = mse + ((hist1[x] - hist2[x]) ** 2)

        return mse
        pass