from Lab02.BaseImage import *
from Lab03.GrayScaleTransform import *
import numpy as np
from typing import Any


class Histogram:
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: Any) -> None:
        self.values = values
        pass


    def plot(self) -> None:
        if (self.values.ndim == 2):
            plt.subplot(1,1,1)
            plt.title("Gray Scale")
            hist, bins = np.histogram(self.values, bins=256, range=(0, 255))
            plt.plot(bins[:-1], hist, color='gray')

        else:
            r, g, b = np.squeeze(np.dsplit(self.values, self.values.shape[-1]))

            plt.figure(figsize=(12, 5))
            plt.subplot(1, 3, 1)
            plt.title("Red")
            hist, bins = np.histogram(r, bins=256, range=(0, 255))
            plt.plot(bins[:-1], hist, color='red')

            plt.subplot(1, 3, 2)
            plt.title("Green")
            hist, bins = np.histogram(g, bins=256, range=(0, 255))
            plt.plot(bins[:-1], hist, color='green')

            plt.subplot(1, 3, 3)
            plt.title("Blue")
            hist, bins = np.histogram(b, bins=256, range=(0, 255))
            plt.plot(bins[:-1], hist, color='blue')

        plt.show()
        pass