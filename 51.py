#Дан одновимірний масив а. Сформувати новий масив, який складається
#тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
#елементів немає, то видати повідомлення.
#Драч Ольга Олескандрівна, 122Д

q = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946]
w = q[10:]   #Видаляємо 10 цифер
if w == []:  #Якщо елементів не буде то це буде пустий список
    print('Видаю повідомлення')
else:   #Iнакше показуємо результат
    print(w)