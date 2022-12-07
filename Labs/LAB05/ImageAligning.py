from copy import *
from Lab03.GrayScaleTransform import *


class ImageAligning(GrayScaleTransform):
    def __init__(self, path) -> None:
        super().__init__(path)

    def align_image(self, tail_elimination: bool = True) -> 'GrayScaleTransform':
        if not tail_elimination:
            if self.color_model == 4:
                min_value = np.min(self.data)
                max_value = np.max(self.data)

                self.data = (self.data - min_value) * (255 / (max_value - min_value))
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
            if self.color_model == 4:
                min_value = np.percentile(self.data, 5)
                max_value = np.percentile(self.data, 95)

                self.data = (self.data - min_value) * (255 / (max_value - min_value))
                return self

            else:
                min_value1 = np.percentile(self.data[:, :, 0], 5)
                max_value1 = np.percentile(self.data[:, :, 0], 95)
                min_value2 = np.percentile(self.data[:, :, 1], 5)
                max_value2 = np.percentile(self.data[:, :, 1], 95)
                min_value3 = np.percentile(self.data[:, :, 2], 5)
                max_value3 = np.percentile(self.data[:, :, 2], 95)
                self.data[:, :, 0] = (self.data[:, :, 0] - min_value1) * (255 / (max_value1 - min_value1))
                self.data[:, :, 1] = (self.data[:, :, 1] - min_value2) * (255 / (max_value2 - min_value2))
                self.data[:, :, 2] = (self.data[:, :, 2] - min_value3) * (255 / (max_value3 - min_value3))

                return self
