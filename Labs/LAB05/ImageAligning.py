import copy
from copy import *
from Lab03.GrayScaleTransform import *


class ImageAligning(GrayScaleTransform):
    def __init__(self, path) -> None:
        super().__init__(path)

    def align_image(self, tail_elimination: bool = True) -> 'GrayScaleTransform':
        if not tail_elimination:
            if self.color_model == 4:
                obraz = copy.deepcopy(self.data)
                min_value = np.min(obraz)
                max_value = np.max(obraz)

                obraz = (obraz - min_value) * (255 / (max_value - min_value))
                self.data = obraz
                return self
            else:
                obraz = copy.deepcopy(self)
                min_value1 = np.min(obraz.data[:, :, 0])
                max_value1 = np.max(obraz.data[:, :, 0])
                min_value2 = np.min(obraz.data[:, :, 1])
                max_value2 = np.max(obraz.data[:, :, 1])
                min_value3 = np.min(obraz.data[:, :, 2])
                max_value3 = np.max(obraz.data[:, :, 2])

                obraz.data[:, :, 0] = (obraz.data[:, :, 0] - min_value1) * (255 / (max_value1 - min_value1))
                obraz.data[:, :, 1] = (obraz.data[:, :, 1] - min_value2) * (255 / (max_value2 - min_value2))
                obraz.data[:, :, 2] = (obraz.data[:, :, 2] - min_value3) * (255 / (max_value3 - min_value3))

                self.data = obraz.data
                return self

        else:
            kopia = copy.deepcopy(self.data).astype('i')
            if self.color_model == 4:
                min_value = np.percentile(kopia, 5)
                max_value = np.percentile(kopia, 95)

                kopia = (kopia - min_value) * (255 / (max_value - min_value))
                self.data = kopia
                return self

            else:
                min_value1 = np.percentile(kopia[:, :, 0], 5)
                max_value1 = np.percentile(kopia[:, :, 0], 95)
                min_value2 = np.percentile(kopia[:, :, 1], 5)
                max_value2 = np.percentile(kopia[:, :, 1], 95)
                min_value3 = np.percentile(kopia[:, :, 2], 5)
                max_value3 = np.percentile(kopia[:, :, 2], 95)
                kopia[:, :, 0] = (kopia[:, :, 0] - min_value1) * (255 / (max_value1 - min_value1))
                kopia[:, :, 1] = (kopia[:, :, 1] - min_value2) * (255 / (max_value2 - min_value2))
                kopia[:, :, 2] = (kopia[:, :, 2] - min_value3) * (255 / (max_value3 - min_value3))

                self.data = kopia
                return self
