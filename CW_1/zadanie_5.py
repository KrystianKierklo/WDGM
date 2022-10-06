import numpy as np

#Utworzyć tablicę o rozmiarze 10x10 z wartościami zwiększającymi się o 0.01

array5 = np.arange(0, 10, 0.1)
array5 = array5.reshape((10,10))

print(array5)