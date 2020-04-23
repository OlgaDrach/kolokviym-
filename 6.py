#Створіть масив А [1..8] за допомогою генератора випадкових чисел з
#елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
#елементів масиву.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
import random
count = 0
k = np.zeros(8, dtype=int)
for i in range(8):
    k[i] = random.randint(-10, 10)
print(a)
for i in range(8):
    if k[i] < 0:
        count += 1
print(count)
