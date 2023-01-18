import numpy as np

filtr_tozsamosciowy = np.array([
	[0, 0, 0],
	[0, 1, 0],
	[0, 0, 0]])
prefix_tozsamosciowy = 1



filtr_gornoprzepustowy = np.array ([
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]])
prefix_gornoprzepustowy = 1



filtr_dolnoprzepustowy = np.array ([
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]])
prefix_dolnoprzepustowy = 1/9



rozmycie_gaussowskie3x3 = np.array ([
	[1, 2, 1],
	[2, 4, 2],
	[1, 2, 1]])
prefix_gauss_3x3 = 1/16



rozmycie_gaussowskie5x5 = np.array ([
	[1, 4, 6, 4, 1],
	[4, 16, 24, 16, 4],
	[6, 24, 36, 24, 6],
	[4, 16, 24, 16, 4],
	[1, 4, 6, 4, 1]])
prefix_gauss_5x5 = 1/256



prefix_sobel = 1

sobel0 = np.array ([
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]])


sobel45 = np.array ([
	[0, 1, 2],
	[-1, 0, 1],
	[-2, -1, 0]])



sobel90 = np.array ([
	[1, 2, 1],
	[0, 0, 0],
	[-1, -2, -1]])



sobel135 = np.array ([
	[2, 1, 0],
	[1, 0, -1],
	[0, -1, -2]])


