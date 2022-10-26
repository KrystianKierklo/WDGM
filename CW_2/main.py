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
        img_tabhsv = copy.copy(self.data)


        for x in range(self.data.shape[0]):
            for y in range(self.data.shape[1]):
                R = self.data[x][y][0]
                G = self.data[x][y][1]
                B = self.data[x][y][2]

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

                img_tabhsv[x][y][0] = H
                img_tabhsv[x][y][1] = S
                img_tabhsv[x][y][2] = V

        imghsv_stacked = np.dstack((img_tabhsv[:,:,0], img_tabhsv[:,:,1], img_tabhsv[:,:,2]))
        return imghsv_stacked
        pass


    def to_hsi(self) -> 'BaseImage':
        img_tabhsi = copy.copy(self.data)

        for x in range(self.data.shape[0]):
            for y in range(self.data.shape[1]):
                R = self.data[x][y][0]
                G = self.data[x][y][1]
                B = self.data[x][y][2]

                M = max(R, G, B)
                m = min(R, G, B)

                I = (R + G + B) / 3

                if (M > 0):
                    S = 1 - m / M
                else:
                    S = 0

                if (G >= B):
                    H = math.acos(
                        (R - 0.5 * G - 0.5 * B) / (math.sqrt(R ** 2 + G ** 2 + B ** 2 - R * G - R * B - G * B)))
                else:
                    H = 360 - math.acos(
                        (R - 0.5 * G - 0.5 * B) / (math.sqrt(R ** 2 + G ** 2 + B ** 2 - R * G - R * B - G * B)))

                img_tabhsi[x][y][0] = H
                img_tabhsi[x][y][1] = S
                img_tabhsi[x][y][2] = I

        imghsi_stacked = np.dstack((img_tabhsi[:, :, 0], img_tabhsi[:, :, 1], img_tabhsi[:, :, 2]))
        return imghsi_stacked
        pass

    def to_hsl(self) -> 'BaseImage':
        img_tabhsl = copy.copy(self.data)

        for x in range(self.data.shape[0]):
            for y in range(self.data.shape[1]):
                R = self.data[x][y][0]
                G = self.data[x][y][1]
                B = self.data[x][y][2]

                M = max(R, G, B)
                m = min(R, G, B)

                d = (M - m) / 255
                L = (0.5 * (M + m)) / 255

                if (L > 0):
                    S = d / (1 - abs(2 * L - 1))
                else:
                    S = 0

                if (G >= B):
                    H = math.acos(
                        (R - 0.5 * G - 0.5 * B) / (math.sqrt(R ** 2 + G ** 2 + B ** 2 - R * G - R * B - G * B)))
                else:
                    H = 360 - math.acos(
                        (R - 0.5 * G - 0.5 * B) / (math.sqrt(R ** 2 + G ** 2 + B ** 2 - R * G - R * B - G * B)))

                img_tabhsl[x][y][0] = H
                img_tabhsl[x][y][1] = S
                img_tabhsl[x][y][2] = L

        imghsl_stacked = np.dstack((img_tabhsl[:, :, 0], img_tabhsl[:, :, 1], img_tabhsl[:, :, 2]))
        return imghsl_stacked
        pass

    def to_rgb(self) -> 'BaseImage':

        img_tabhsv = self.to_hsv()
        img_tabrgb = copy.copy(img_tabhsv)

        for x in range(self.data.shape[0]):
            for y in range(self.data.shape[1]):
                H = img_tabhsv[x][y][0]
                S = img_tabhsv[x][y][1]
                V = img_tabhsv[x][y][2]

                M = 255 * V
                m = M * (1 - S)

                z = (M - m) * (1 - abs(((H / 60) % 2) -1))

                if (H >= 0 and H < 60):
                    R = M
                    G = z + m
                    B = m
                elif (H >= 60 and H < 120):
                    R = z + m
                    G = M
                    B = m
                elif (H >= 120 and H < 180):
                    R = m
                    G = M
                    B = z + m
                elif (H >= 180 and H < 240):
                    R = m
                    G = M
                    B = z + m
                elif (H >= 240 and H < 300):
                    R = z + m
                    G = m
                    B = M
                else:
                    R = M
                    G = m
                    B = z + m

                img_tabrgb[x][y][0] = R
                img_tabrgb[x][y][1] = G
                img_tabrgb[x][y][2] = B

        imgrgb_stacked = np.dstack((img_tabrgb[:, :, 0], img_tabrgb[:, :, 1], img_tabrgb[:, :, 2]))
        return imgrgb_stacked
        pass


