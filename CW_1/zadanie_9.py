import numpy as np
import zadanie_2 as z2

#Wyznaczyć sumę wartości elementów znajdujących się w dwóch ostatnich wierszach macierzy utworzonej w zadaniu 2

array2 = z2.array2

array9 = array2[3:]

print(array9.sum())