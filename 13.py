#Створіть масив з 15 цілочисельних елементів і визначте серед них
#мінімальне значення.
#Драч Ольга Олескандрівна, 122Д

from random import randint
l = 1000
for j in range(15):         #діапазон масиву
    n = randint(-999,999)     #Масив
    if n < l:         #перевіряємо чи менше інтеріюєме ніж попереднє мінімальне
        l = n         #робимо його мінімальним
print(l)