import numpy as np
from enum import Enum
from matplotlib.image import imread
from matplotlib.image import imsave
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import copy
import math


class ColorModel(Enum):
    rgb = 0
    hsv = 1
    hsi = 2
    hsl = 3
    gray = 4

class BaseImage:
    data: np.ndarray  # tensor przechowujacy piksele obrazu
    color_model: ColorModel  # atrybut przechowujacy biezacy model barw obrazu

    def __init__(self, path: str) -> None:
        self.data = imread(path)
        pass

    def save_img(self, path: str) -> None:
        imsave('saved_image.jpg', self.data)
        pass

    def show_img(self) -> None:
        imshow(self.data)
        pass

    def get_layer(self, layer_id: int) -> 'BaseImage':
        img_tab = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        return img_tab[layer_id]
        pass

    def to_hsv(self) -> 'BaseImage':
        img_tab = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        img_tabhsv = copy.copy(img_tab)

        for x in range(img_tab.shape[1]):
            for y in range(img_tab.shape[2]):
                R = img_tab[0][x][y]
                G = img_tab[1][x][y]
                B = img_tab[2][x][y]

                M = max(R, G, B)
                m = min(R, G, B)

                V = M / 255

                if (M > 0):
                    S = 1 - m/M
                else:
                    S = 0

                if (G >= B):
                    H = math.acos((R - 0.5*G - 0.5*B)/(math.sqrt(R**2 + G**2 + B**2 - R*G - R*B - G*B)))
                else:
                    H = 360 - math.acos((R - 0.5*G - 0.5*B)/(math.sqrt(R**2 + G**2 + B**2 - R*G - R*B - G*B)))

                img_tabhsv[0][x][y] = H * 100
                img_tabhsv[1][x][y] = S * 100
                img_tabhsv[2][x][y] = V * 100

        imghsv_stacked = np.dstack((img_tabhsv[0], img_tabhsv[1], img_tabhsv[2]))
        return imghsv_stacked
        pass

    def to_hsi(self) -> 'BaseImage':
        img_tab = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        img_tabhsi = copy.copy(img_tab)

        for x in range(img_tab.shape[1]):
            for y in range(img_tab.shape[2]):
                R = img_tab[0][x][y]
                G = img_tab[1][x][y]
                B = img_tab[2][x][y]

                M = max(R, G, B)
                m = min(R, G, B)

                I = (R + G + B) / 3

                if (M > 0):
                    S = 1 - m / M
                else:
                    S = 0

                if (G >= B):
                    H = math.acos((R - 0.5 * G - 0.5 * B) / (math.sqrt(R ** 2 + G ** 2 + B ** 2 - R * G - R * B - G * B)))
                else:
                    H = 360 - math.acos((R - 0.5 * G - 0.5 * B) / (math.sqrt(R ** 2 + G ** 2 + B ** 2 - R * G - R * B - G * B)))

                img_tabhsi[0][x][y] = H
                img_tabhsi[1][x][y] = S
                img_tabhsi[2][x][y] = I

        imghsi_stacked = np.dstack((img_tabhsi[0], img_tabhsi[1], img_tabhsi[2]))
        return imghsi_stacked
        pass

    def to_hsl(self) -> 'BaseImage':
        img_tab = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        img_tabhsl = copy.copy(img_tab)

        for x in range(img_tab.shape[1]):
            for y in range(img_tab.shape[2]):
                R = img_tab[0][x][y]
                G = img_tab[1][x][y]
                B = img_tab[2][x][y]

                M = max(R, G, B)
                m = min(R, G, B)

                d = (M - m) / 255

                L = (0.5*(M + m)) / 255

                if (L > 0):
                    S = d / (1 - abs(2 * L - 1))
                else:
                    S = 0

                if (G >= B):
                    H = math.acos((R - 0.5*G - 0.5*B)/(math.sqrt(R**2 + G**2 + B**2 - R*G - R*B - G*B)))
                else:
                    H = 360 - math.acos((R - 0.5*G - 0.5*B)/(math.sqrt(R**2 + G**2 + B**2 - R*G - R*B - G*B)))

                img_tabhsl[0][x][y] = H
                img_tabhsl[1][x][y] = S
                img_tabhsl[2][x][y] = L

        imghsl_stacked = np.dstack((img_tabhsl[0], img_tabhsl[1], img_tabhsl[2]))
        return imghsl_stacked
        pass

    def to_rgb(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu rgb
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        pass


