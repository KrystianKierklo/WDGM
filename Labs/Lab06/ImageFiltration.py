import copy
from typing import Optional
from Lab02.BaseImage import BaseImage
import numpy as np


class ImageFiltration(BaseImage):
    def __init__(self, path: str):
        super().__init__(path)

    def conv_2d(self, kernel: np.ndarray, prefix: Optional[float] = 1) -> BaseImage:

        kopia = copy.deepcopy(self)

        if kopia.color_model == 0:
            kopia.data = np.zeros((self.data.shape[0], self.data.shape[1], self.data.shape[2]))

            for x in range(self.data.shape[0]):
                for y in range(self.data.shape[1]):
                    for z in range(self.data.shape[2]):
                        for m in range(kernel.shape[0]):
                            for n in range(kernel.shape[1]):
                                kopia.data[x, y, z] = kopia.data[x, y, z] + kernel[m, n] * self.data[x-m, y-n, z]

        else:
            kopia.data = np.zeros((self.data.shape[0], self.data.shape[1]))

            for x in range(self.data.shape[0]):
                for y in range(self.data.shape[1]):
                    for m in range(kernel.shape[0]):
                        for n in range(kernel.shape[1]):
                            kopia.data[x, y] = kopia.data[x, y] + kernel[m, n] * self.data[x - m, y - n]

        kopia.data = kopia.data * prefix

        kopia.data[kopia.data > 255] = 255
        kopia.data[kopia.data < 0] = 0

        self.data = kopia.data.astype('uint16')
        return self
