#Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
#яка містить довжини опор, які встановлюються через кожні R/5 м.а
#Драч Ольга Олескандрівна, 122Д

import math
a = int(input('Введіть радіус даху - '))    #Просимо ввести  радіус півкола
d = []     #Створюємо пустий список
for j in range(a // 5):
    d.append(math.sqrt(r ** 2 - ((r / 5) * (4 - i)) ** 2))     #Рахуваємо довжину опори(за т.Піфагора)
for j in range(len(d) - 2, -1, -1):
    d.append(d[j])    #Добавляємо наш елемент в список
print(d)    #Виводимо довжини опор
