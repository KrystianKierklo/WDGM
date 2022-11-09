from Lab02.BaseImage import *


class GrayScaleTransform(BaseImage):
    def __init__(self, path) -> None:
        super().__init__(path)
        pass

    def to_gray(self) -> 'BaseImage':
        if self.color_model == 0:
            image_gray = np.zeros((self.data.shape[0], self.data.shape[1])).astype('uint64')

            R, G, B = np.squeeze(np.dsplit(self.data, self.data.shape[-1])).astype('uint64')

            for x in range(self.data.shape[0]):
                for y in range(self.data.shape[1]):
                    image_gray[x,y] = (R[x,y] + G[x,y] + B[x,y]) / 3

        self.data = image_gray
        self.color_model = 4
        return self
        pass


    def to_sepia(self, alpha_beta: tuple = (None, None), w: int = None) -> BaseImage:
        if self.color_model == 0:
            if alpha_beta != None:

                img2 = self.to_gray()

                sepia = np.zeros((img2.data.shape[0], img2.data.shape[1], 3)).astype('uint16')

                for x in range(img2.data.shape[0]):
                    for y in range(img2.data.shape[1]):
                        sepia[x,y,0] = img2.data[x,y] * alpha_beta[0]
                        sepia[x,y,1] = img2.data[x,y]
                        sepia[x,y,2] = img2.data[x,y] * alpha_beta[1]

                self.data = sepia
                self.color_model = 5
                return self
                pass

            if w != None:
                img2 = self.to_gray()

                sepia = np.zeros((img2.data.shape[0], img2.data.shape[1], 3)).astype('uint16')

                for x in range(img2.data.shape[0]):
                    for y in range(img2.data.shape[1]):
                        sepia[x,y,0] = img2.data[x,y] + 2 * w
                        sepia[x,y,1] = img2.data[x,y] + w
                        sepia[x,y,2] = img2.data[x,y]

                self.data = sepia
                self.color_model = 5
                return self
                pass