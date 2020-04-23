#Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
#одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
#числами від 500 до 1000.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
from random import randint
q = 0
g = np.zeros(30, dtype=int)
for i in range(30):   # Діапазон
    g = randint(500, 1000)   # Рандом
print(g)
for i in range(30):
    if g % 5 == 0 and g % 8 == 0:  # Умова
        q += g
print(q)
