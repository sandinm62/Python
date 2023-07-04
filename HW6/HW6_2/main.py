# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


import random
def printMass(n, count = 0):
    if count == (n - 1): 
        if list1[count - 1] >= numberMin and list1[count - 1] <= numberMax:
             listSorted.append(count)    
        return list1.append(random.randint(0, 10))
    else:
        list1.append(random.randint(0, 10))
        if list1[count - 1] >= numberMin and list1[count - 1] <= numberMax:
            listSorted.append(count)
        return printMass(n, count + 1)




list1 = []
listSorted = []
counter = int(input('Введите колличество элементов в массиве: '))
numberMin = int(input('Введите минимальное число диапазона: '))
numberMax = int(input('Введите максимальное число диапазона: '))

printMass(counter)
# sortedMass()

print(*list1)
print(*listSorted)
