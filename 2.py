#Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
#екран значення коріння і квадратів кожного з елементів масиву.
#Драч Ольга Олескандрівна, 122Д

import math
import numpy as np
a = []
for i in range(5):
    b = []
    b.append(int(input("Введіть елементи: ")))
    a.append(b)
c = np.array(a)
for i in range(5):
    print("Квадратний корінь з числа: ", a[i], "дорівнює: ", math.sqrt(c[i]))
print(" ")
for i in range(5):
    print("Квадрат числа:", a[i], "дорівнює: ", math.pow(c[i], 2))
