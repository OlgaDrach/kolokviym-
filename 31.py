#Обчислити середнє арифметичне значення тих елементів одновимірного
#масиву, які потрапляють в інтервал від -2 до 10.
#Драч Ольга Олескандрівна, 122Д

from random import randint
s = 0
for i in range(10):  #Діапазон
    g = randint(10, 40)   #Масив
    if g >= -2 and g <= 10:   #Умова
      s = s + g      #Cума
print(s)
