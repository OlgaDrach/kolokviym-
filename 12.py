#Дані про температуру повітря за декаду грудня зберігаються в масиві.
#Визначити, скільки раз температура була вище середньої за цю декаду.
#Драч Ольга Олескандрівна, 122Д

a = []
for i in range(30):
    a.append(int(input("Введіть: ")))
print(a)
counter = 0
for i in range(30):
    if a[i] > -4 :
        counter += 1
print(counter, "раз(и/ів) температура була вище середньої за цю декаду.")
