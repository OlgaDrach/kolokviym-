#Створіть масив А [1..12] за допомогою генератора випадкових чисел з
#елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
#масиву числом 0.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
import random
m = np.zeros(12, dtype=int)
for i in range(12):
    m[i] = random.randint(-20, 10)
print(m)
for i in range(12):
    if m[i] < 0:
        m[i] = 0
print(m)

