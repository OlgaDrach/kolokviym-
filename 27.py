#Лінійний масив містить відомості про кількість опадів, що випали за
#кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
#опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
#місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
#Драч Ольга Олескандрівна, 122Д

from random import randint
e = 0
g = 0
for i in range(12):    #Діапазон
    u = randint(20,45)   #Масив
            if u < 30:
                g += 1
                e = u+e
print('Середня кількість опадів:',e/12)
print('Посушливі місяці:',g)
print('Найпосушливі місяці:',e)
