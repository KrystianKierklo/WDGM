import numpy as np
import zadanie_2 as z2

#Wybrać 3 pierwsze elementy z ostatniej kolumny tablicy utworzonej w zadaniu 2, a następnie ułożyć z nich kolumnę

array2 = z2.array2

array8 = array2[:3, 4]

array8 = array8.reshape((3, 1))

print(array8)