#Розсортуйте заданий лінійний масив по зростанню.
#Драч Ольга Олескандрівна, 122Д

import numpy as np
from random import randint
def bbuble_sort(h):
    no= len(h) - 1
    for i in range(0, no):
        for x in range(0, no):
            if h[v] > h[v + 1]:
                h[v], h[v + 1] = h[v + 1], h[v]
    return h
n = np.zeros(10, dtype=int)
for m in range(7):
    n[m] = random.randint(1, 7)
print(n)
print(bbuble_sort(n))
