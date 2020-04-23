#Створіть цілочисельний масив А [1..15] за допомогою генератора
#випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
#найбільший елемент масиву і його індекс.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
import random
point = 0
h = 0
u = np.zeros(12, dtype=int)
for i in range(12):
    u[i] = random.randint(1, 15)
print(u)
for i in range(len(u)):
    if u[i] > h:
        h = u[i]
        point = i
print("max-", h)
print("point-", point+1)
