#Знайти суму додатніх елементів лінійного масиву цілих чисел.
#Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
#Драч Ольга Олескандрівна, 122Д

from random import randint
import numpy as np
q = 0
x = []
for i in range(0, 9, 1):
    n = []
    n.append(int(input("input: ", )))
    x.append(n)
x = np.array(x)
for i in range(len(x)):
    if x[i] > 0:
        q += x[i]
print("сума додатніх елементів ", q)
