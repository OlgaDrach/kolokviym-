#Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
#чисел в ньому.
#Драч Ольга Олескандрівна, 122Д

w = [13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946, 13,21,34,55,89,144]
for j in w:   #Проходимось по масиву
    if w.count(j)>1:   #якщо повторів більше ніж 1
        while w.count(j)>1:   #то поки воно не стане рівним 1
            w.remove(j)             #всі елементи видаляються
print('Кількість різних чисел:',len(w))
