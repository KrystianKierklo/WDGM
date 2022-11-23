from Lab02.BaseImage import *
from Lab03.GrayScaleTransform import *
from Lab04.Histogram import *
from Lab03.Image import *
from enum import Enum
from typing import Any
import numpy as np
import math


class ImageDiffMethod(Enum):
    mse = 0
    rmse = 1



class ImageComparison(GrayScaleTransform):
    # def __init__(self, img: Any) -> None:
    #     super().__init__(img)

    def histogram(self) -> Histogram:
        return Histogram(self.data)
        pass

    def compare_to(self, other: GrayScaleTransform, method: ImageDiffMethod) -> float:

        img1 = self.to_gray().data
        img2 = other.to_gray().data

        hist1 = Histogram(img1).values
        hist2 = Histogram(img2).values

        mse = 0

        for x in range(len(hist1)):
            mse =  mse + ((hist1[x] - hist2[x]) ** 2)
        mse = mse / len(hist1)

        if (method == 0):
            wynik = round(np.sum(mse), 1)
            return wynik
        else:
            rmse = math.sqrt(np.sum(mse))
            wynik = round(rmse, 1)
            return wynik
        pass