#Обчислити суму парних елементів одновимірного масиву до першого
#зустрінутого нульового елемента.
#Драч Ольга Олескандрівна, 122Д

m = []
l = 0
k = 0
for i in range(5):
    m.append(int(input("Введіть число:")))
for i in range(5):
    if m[i] == 0:
        break
for i in range(5):
    if m[i] == 0:
        l = m[: i]
        break
for i in range(l):
    if l[i] % 2 == 0:
        k = k + l[i]
print('Сума парних елементів:',k)
