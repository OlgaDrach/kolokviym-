#З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
#що протягом цього часу температура знижувалася. Визначте, о котрій годині було
#вперше зафіксовано від'ємну температуру.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
g = []
for i in range(3):
    f = []
    f.append(int(input("Введіть час: ")))
    g.append(f)
print(g)
array = np.array(g)
c = []
time=0
for i in range(0,3,1):
    if array[i] < 0:
        time=i+8
        c = array[i]
        break
print("Температура - ", c)
print("Час зафіксування - ", time)
