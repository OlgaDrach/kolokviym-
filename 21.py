#Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
#числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
#від 50 до 100.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
from random import randint
b = int(input("Введiть значення: "))
c = 0
f = 1
a = np.zeros(10, dtype=int)
for i in range(10):   #Діапазон
    a = randint(50, 100)  #Рандом
    if a < b:   #Умова
        c += a  #Перевіряємо чи є такі числа щоб в кінці не вийшло значчання а 
        f = f * a  #Добуток
if a == 0:
    print(a)  
else:
    print(c)