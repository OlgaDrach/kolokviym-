#Знайти найбільший елемент з елементів одновимірного масиву, що мають
#парний номер. Визначити, чи є він єдиним.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
import random


from random import randint
import numpy as np
w =[]  #Масив
v = np.zeros(10, dtype=int)  #Замінюєм нулями
for i in range(10):    #Діапазон
    a= randint(-5, 100)  #Створюеться значення у заданому діапозоні
print(a)
for i in range(a):
    if a not in w:    #Умова
        v += 1   
        w.append(a)
print(v)

