#Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
#Драч Ольга Олескандрівна, 122Д

c = 0
a = []
for j in range(1,20):   #Діапазон
    a.append(int(input("Введіть число: ")))
for j in range(5):
    if a[j] > 0  or a[j] < 0:  #Умова
        c += a[j]
print('Добуток всіх його ненульових елементів',c)
