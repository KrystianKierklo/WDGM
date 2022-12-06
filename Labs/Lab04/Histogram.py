import matplotlib.pyplot as plt

from Lab02.BaseImage import *
from Lab03.GrayScaleTransform import *
import numpy as np
from typing import Any


class Histogram:
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: Any) -> None:
        if values.ndim == 2:
            self.values = np.histogram(values, bins=256, range=(0, 255))[0]
        else:
            r, g, b = np.squeeze(np.dsplit(values, values.shape[-1]))

            r = np.histogram(r, bins=256, range=(0, 255))[0]
            g = np.histogram(g, bins=256, range=(0, 255))[0]
            b = np.histogram(b, bins=256, range=(0, 255))[0]

            self.values = np.dstack((r, g, b))

    def plot(self) -> None:
        if (self.values.ndim == 1):
            plt.subplot(1, 1, 1)
            plt.title("Gray Scale")
            bins = np.linspace(0, 255, 256)
            plt.plot(bins, self.values, color='gray')

        else:
            r, g, b = np.squeeze(np.dsplit(self.values, self.values.shape[-1]))
            bins = np.linspace(0,255, 256)

            plt.figure(figsize=(12, 5))
            plt.subplot(1, 3, 1)
            plt.title("Red")
            plt.plot(bins, r, color='red')

            plt.subplot(1, 3, 2)
            plt.title("Green")
            plt.plot(bins, g, color='green')

            plt.subplot(1, 3, 3)
            plt.title("Blue")
            plt.plot(bins, b, color='blue')

        plt.show()
        pass

    def to_cumulated(self) -> 'Histogram':
        if self.values.ndim == 1:
            self.values = np.cumsum(self.values)
        else:
            self.values[:,:,0] = np.cumsum(self.values[:,:,0])
            self.values[:,:,1] = np.cumsum(self.values[:,:,1])
            self.values[:,:,2] = np.cumsum(self.values[:,:,2])
        return self
