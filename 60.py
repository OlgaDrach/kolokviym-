#Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
#однакових чисел, що йдуть підряд в ньому.
#Драч Ольга Олескандрівна, 122Д

n = 0
p = [1,2,2,2,2,2,23,3,3,5,8,13,13,]
for b in p:
    m = p.count(b)
    if m > n:
        n = m
print('Найбільше кількість однакових чисел, що йдуть підряд:', n)