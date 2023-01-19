from Lab02.BaseImage import *
import cv2
import matplotlib.pyplot as plt
import numpy as np

class Opencv:
    image: np.ndarray

    def __init__(self, path: str) -> None:
        self.image = cv2.imread(path, cv2.IMREAD_COLOR)


    def otsu(self, thresh=0, maxval=255):
        obraz = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh_otsu = cv2.threshold(obraz, thresh=thresh, maxval=maxval, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.image = thresh_otsu
        return self


    def adaptive(self, maxvalue=255, blocksize=13, c=8):
        obraz = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        thresh_adaptive = cv2.adaptiveThreshold(obraz, maxValue=maxvalue, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                                   thresholdType=cv2.THRESH_BINARY, blockSize=blocksize, C=c)
        self.image = thresh_adaptive
        return self

    def canny_edges(self, prog_histerezy1=16, prog_histerezy2=40, wielkosc_filtra=3):
        obraz = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(obraz, prog_histerezy1, prog_histerezy2, wielkosc_filtra)

        self.image = canny
        return self

    def clahe_gray(self, cliplimit=2.0, tilegridsize=(4, 4)):
        obraz_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=cliplimit, tileGridSize=tilegridsize)
        equalized_obraz = clahe.apply(obraz_gray)

        plt.subplot(221)
        plt.imshow(obraz_gray, cmap='gray')

        plt.subplot(222)
        plt.hist(obraz_gray.ravel(), bins=256, range=(0, 256), color='gray')

        plt.subplot(223)
        plt.imshow(equalized_obraz, cmap='gray')

        plt.subplot(224)
        plt.hist(equalized_obraz.ravel(), bins=256, range=(0, 256), color='gray')

        plt.show()

        return


    def clahe_color(self, cliplimit=2.0, tilegridsize=(8, 8)):
        obraz_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        obraz_lab = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)

        clahe = cv2.createCLAHE(clipLimit=cliplimit, tileGridSize=tilegridsize)
        obraz_lab[..., 0] = clahe.apply(obraz_lab[..., 0])
        obraz_color_equalized = cv2.cvtColor(obraz_lab, cv2.COLOR_LAB2RGB)

        plt.subplot(221)
        plt.imshow(obraz_rgb)

        plt.subplot(222)
        plt.hist(obraz_rgb[..., 0].ravel(), bins=256, range=(0, 256), color='b')
        plt.hist(obraz_rgb[..., 1].ravel(), bins=256, range=(0, 256), color='g')
        plt.hist(obraz_rgb[..., 2].ravel(), bins=256, range=(0, 256), color='r')

        plt.subplot(223)
        plt.imshow(obraz_color_equalized)

        plt.subplot(224)
        plt.hist(obraz_color_equalized[..., 0].ravel(), bins=256, range=(0, 256), color='b')
        plt.hist(obraz_color_equalized[..., 1].ravel(), bins=256, range=(0, 256), color='g')
        plt.hist(obraz_color_equalized[..., 2].ravel(), bins=256, range=(0, 256), color='r')

        plt.show()
        return


    def lines_detect(self, thresh=0, maxval=255, prog_histeri1=20, prog_histeri2=50, wielkosc_filtra=3,
                     zm1=2, zm2=180, zm3=30):
        obraz = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, lines_thresh = cv2.threshold(obraz, thresh=thresh, maxval=maxval, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        lines_edges = cv2.Canny(lines_thresh, prog_histeri1, prog_histeri2, wielkosc_filtra)
        lines = cv2.HoughLinesP(lines_edges, zm1, np.pi/zm2, zm3)
        result_lines_img = cv2.cvtColor(obraz, cv2.COLOR_GRAY2RGB)
        for line in lines:
            x0, y0, x1, y1 = line[0]
            cv2.line(result_lines_img, (x0, y0), (x1, y1), (0, 0, 255), 5)

        self.image = result_lines_img
        return self

    def circles_detect(self, dp=2, minDist=60, minRadius=20, maxRadius=100):
        obraz_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        obraz_color = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        circles = cv2.HoughCircles(obraz_gray, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, minRadius=minRadius,
                                   maxRadius=maxRadius)
        for(x,y,r) in circles.astype(int)[0]:
            cv2.circle(obraz_color, (x,y), r, (0, 255, 0), 4)

        self.image = obraz_color
        return self