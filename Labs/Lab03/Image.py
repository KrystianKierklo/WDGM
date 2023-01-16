from Lab02.BaseImage import *
from Lab03.GrayScaleTransform import *
from Lab04.Histogram import Histogram
from Lab04.ImageComparison import *
from Lab05.ImageAligning import *
from Lab06.ImageFiltration import *
from Lab07.Thresholding import *
from typing import Any

class Image(ImageComparison, ImageAligning, ImageFiltration, Thresholding):
    def __init__(self, path: str, color_model: Optional[ColorModel] = 0) -> None:
        super().__init__(path)


