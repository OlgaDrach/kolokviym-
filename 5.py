#Створіть масив А [1..7] за допомогою генератора випадкових чисел і
#виведіть його на екран. Збільште всі його елементи в 2 рази.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
import random
o = np.zeros(7, dtype=int)
for i in range(7):
    o[i] = random.randint(1, 7)
print(o)
c = 0
b = []
for i in range(7):
    j = [o[i]**2]
    p.append(j)
print(p)
