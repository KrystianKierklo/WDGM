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
    sepia = 5


class BaseImage:
    data: np.ndarray  # tensor przechowujacy piksele obrazu
    color_model: ColorModel  # atrybut przechowujacy biezacy model barw obrazu

    def __init__(self, path: str) -> None:
        self.data = imread(path)
        self.color_model = 0
        pass

    def save_img(self, path: str) -> None:
        imsave(path, self.data)
        pass

    def show_img(self) -> None:
        imshow(self.data)
        pass

    def get_layer(self, layer_id: int) -> 'BaseImage':
        return self.data[:,:,layer_id]
        pass

    def to_hsv(self) -> 'BaseImage':
        if self.color_model == 0:
            R, G, B = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))

            H = np.zeros((R.shape[0], R.shape[1]))
            S = np.zeros((G.shape[0], G.shape[1]))
            V = np.zeros((B.shape[0], B.shape[1]))

            for x in range(R.shape[0]):
                for y in range(R.shape[1]):

                    M = max(R[x,y], G[x,y], B[x,y])
                    m = min(R[x,y], G[x,y], B[x,y])

                    V[x,y] = M / 255

                    if (M > 0):
                        S[x,y] = 1 - m/M
                    else:
                        S[x,y] = 0

                    if (G[x,y] >= B[x,y]):
                        H[x,y] = np.arccos((R[x,y] - (0.5*G[x,y]) - (0.5*B[x,y])) / np.sqrt(((R[x,y]**2) + (G[x,y]**2)
                                + (B[x,y]**2) - (R[x,y]*G[x,y]) - (R[x,y]*B[x,y]) - (G[x,y]*B[x,y]))))
                    else:
                        H[x,y] = 360 - np.arccos((R[x,y] - (0.5*G[x,y]) - (0.5*B[x,y])) / np.sqrt(((R[x,y]**2) +
                                (G[x,y]**2) + (B[x,y]**2) - (R[x,y]*G[x,y]) - (R[x,y]*B[x,y]) - (G[x,y]*B[x,y]))))


            self.data = np.dstack((H,S,V))
            self.color_model = 1
            return self
            pass


    def to_hsi(self) -> 'BaseImage':
        R, G, B = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))

        H = np.zeros((R.shape[0], R.shape[1]))
        S = np.zeros((G.shape[0], G.shape[1]))
        I = np.zeros((B.shape[0], B.shape[1]))

        for x in range(R.shape[0]):
            for y in range(R.shape[1]):

                M = max(R[x,y], G[x,y], B[x,y])
                m = min(R[x,y], G[x,y], B[x,y])

                I[x,y] = (R[x,y] + G[x,y] + B[x,y]) / 3

                if (M > 0):
                    S[x,y] = 1 - m / M
                else:
                    S[x,y] = 0

                if (G[x, y] >= B[x, y]):
                    H[x, y] = np.arccos((R[x, y] - (0.5 * G[x, y]) - (0.5 * B[x, y])) / (np.sqrt(((R[x, y] ** 2) +
                    (G[x, y] ** 2)+ (B[x, y] ** 2) - (R[x, y] * G[x, y]) - (R[x, y] * B[x, y]) - (G[x, y] * B[x, y])))))
                else:
                    H[x, y] = 360 - np.arccos((R[x, y] - (0.5 * G[x, y]) - (0.5 * B[x, y])) / (np.sqrt(((R[x, y] ** 2) +
                    (G[x, y] ** 2) + (B[x, y] ** 2) - (R[x, y] *G[x, y]) - (R[x, y] *B[x, y]) - (G[x, y] *B[x, y])))))


        self.data = np.dstack((H,S,I))
        self.color_model = 2
        return self
        pass


    def to_hsl(self) -> 'BaseImage':
        R, G, B = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        H = np.zeros((R.shape[0], R.shape[1]))
        S = np.zeros((G.shape[0], G.shape[1]))
        L = np.zeros((B.shape[0], B.shape[1]))


        for x in range(R.shape[0]):
            for y in range(R.shape[1]):

                M = max(R[x,y], G[x,y], B[x,y])
                m = min(R[x,y], G[x,y], B[x,y])

                d = (M - m) / 255
                L[x,y] = (0.5 * (M + m)) / 255

                if (L[x,y] > 0):
                    S[x,y] = d / (1 - abs(2 * L[x,y] - 1))
                else:
                    S[x,y] = 0

                if (G[x, y] >= B[x, y]):
                    H[x, y] = np.arccos((R[x, y] - (0.5 * G[x, y]) - (0.5 * B[x, y])) / (np.sqrt(((R[x, y] ** 2) +
                    (G[x, y] ** 2)+ (B[x, y] ** 2) - (R[x, y] * G[x, y]) - (R[x, y] * B[x, y]) - (G[x, y] * B[x, y])))))
                else:
                    H[x, y] = 360 - np.arccos((R[x, y] - (0.5 * G[x, y]) - (0.5 * B[x, y])) / (np.sqrt(((R[x, y] ** 2) +
                    (G[x, y] ** 2) + (B[x, y] ** 2) - (R[x, y] *G[x, y]) - (R[x, y] *B[x, y]) - (G[x, y] *B[x, y])))))



        self.data = np.dstack((H,S,L))
        self.color_model = 3
        return self
        pass

    def to_rgb(self) -> 'BaseImage':

        if self.color_model == 1:
            H, S, V = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))

            R = np.zeros((H.shape[0], H.shape[1]))
            G = np.zeros((H.shape[0], H.shape[1]))
            B = np.zeros((H.shape[0], H.shape[1]))


            for x in range(H.shape[0]):
                for y in range(H.shape[1]):

                    M = 255 * V[x,y]
                    m = M * (1 - S[x,y])

                    z = (M - m) * (1 - abs(((H[x,y] / 60) % 2) -1))

                    if (H[x,y] >= 0 and H[x,y] < 60):
                        R[x,y] = M
                        G[x,y] = z + m
                        B[x,y] = m
                    elif (H[x,y] >= 60 and H[x,y] < 120):
                        R[x,y] = z + m
                        G[x,y] = M
                        B[x,y] = m
                    elif (H[x,y] >= 120 and H[x,y] < 180):
                        R[x,y] = m
                        G[x,y] = M
                        B[x,y] = z + m
                    elif (H[x,y] >= 180 and H[x,y] < 240):
                        R[x,y] = m
                        G[x,y] = M
                        B[x,y] = z + m
                    elif (H[x,y] >= 240 and H[x,y] < 300):
                        R[x,y] = z + m
                        G[x,y] = m
                        B[x,y] = M
                    else:
                        R[x,y] = M
                        G[x,y] = m
                        B[x,y] = z + m

        if self.color_model == 2:
            H, S, I = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))

            R = np.zeros((H.shape[0], H.shape[1]))
            G = np.zeros((H.shape[0], H.shape[1]))
            B = np.zeros((H.shape[0], H.shape[1]))

            for x in range(H.shape[0]):
                for y in range(H.shape[1]):

                    if (H[x,y] == 0):
                        R[x,y] = I[x,y] + 2 * I[x,y] * S[x,y]
                        G[x,y] = I[x,y] - I[x,y] * S[x,y]
                        B[x,y] = I[x,y] - I[x,y] * S[x,y]

                    elif (H[x,y] > 0 and H[x,y] < 120):
                        R[x,y] = I[x,y] + I[x,y]*S[x,y] * math.cos(H[x,y]) / math.cos(60-H[x,y])
                        G[x,y] = I[x,y] + I[x,y]*S[x,y] * (1-math.cos(H[x,y]) / math.cos(60-H[x,y]))
                        B[x,y] = I[x,y] - I[x,y]*S[x,y]
                    elif (H[x,y] == 120):
                        R[x,y] = I[x,y] - I[x,y]*S[x,y]
                        G[x,y] = I[x,y] + 2*I[x,y]*S[x,y]
                        B[x,y] = I[x,y] - I[x,y]*S[x,y]
                    elif (H[x,y] > 120 and H[x,y] < 240):
                        R[x,y] = I[x,y] - I[x,y]*S[x,y]
                        G[x,y] = I[x,y] + I[x,y]*S[x,y] * math.cos(H[x,y]-120) / math.cos(180-H[x,y])
                        B[x,y] = I[x,y] + I[x,y]*S[x,y] * (1-math.cos(H[x,y]-120) / math.cos(180-H[x,y]))
                    elif (H[x,y] == 240):
                        R[x,y] = I[x,y] - I[x,y]*S[x,y]
                        G[x,y] = I[x,y] - I[x,y]*S[x,y]
                        B[x,y] = I[x,y] + 2*I[x,y]*S[x,y]
                    else:
                        R[x,y] = I[x,y] + I[x,y]*S[x,y] * (1-math.cos(H[x,y]-240)/math.cos(300-H[x,y]))
                        G[x,y] = I[x,y] - I[x,y]*S[x,y]
                        B[x,y] = I[x,y] + I[x,y]*S[x,y] * math.cos(H[x,y] -240)/ math.cos(300-H[x,y])

            R[R>255] = 255
            G[G>255] = 255
            B[B>255] = 255

        if self.color_model == 3:
            H, S, L = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))

            R = np.zeros((H.shape[0], H.shape[1]))
            G = np.zeros((H.shape[0], H.shape[1]))
            B = np.zeros((H.shape[0], H.shape[1]))

            for x in range(H.shape[0]):
                for y in range(H.shape[1]):
                    d = S[x,y]*(1-abs(2*L[x,y]-1))
                    m = 255 * (L[x,y] - 0.5*d)
                    x = d(1-abs(((H[x,y]/60)%2)-1))

                    if (H[x,y]>=0 and H[x,y]<60):
                        R[x,y] = 255 * d +m
                        G[x,y] = 255*x +m
                        B[x,y] = m
                    elif(H[x,y]>=60 and H[x,y] <120):
                        R[x,y] = 255 * x + m
                        G[x,y] = 255*d + m
                        B[x,y] = m
                    elif(H[x,y] >= 120 and H[x,y]<180):
                        R[x,y] = m
                        G[x,y] = 255*d + m
                        B[x,y] = 255 *x +m
                    elif(H[x,y] >= 180 and H[x,y]<240):
                        R[x,y] = m
                        G[x,y] = 255*x + m
                        B[x,y] = 255 * d + m
                    elif(H[x,y] >= 240 and H[x,y] < 300):
                        R[x,y] = 255 * x + m
                        G[x,y] = m
                        B[x,y] = 255 * d + m
                    else:
                        R[x,y] = 255 * d + m
                        G[x,y] = m
                        B[x,y] = 255 * x + m



        self.data = np.dstack((R,G,B)).astype('uint16')
        self.color_model = 0
        return self
        pass


