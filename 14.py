#Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
#пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
#Драч Ольга Олескандрівна, 122Д

z = int(input())
d = list()
for v in range(1,11):     #Діапазон часу
    c = v*z   #Якщо тіло рухаєтьсяя рівномірно, то кожний елемент масиву це певна відстань яку пройшов об'єкт за певний час
    d.append(c)   #Додаємо елемент в масив
print(d)
