# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пузырьковая сортировка топ !!!!)
numericFirst = (8, 9, 9, 5, 5, 4, 7, 3)
numericSeconde = (2, 1, 1, 1, 6, 4, 13)
print(type(numericFirst))
print(*numericFirst)
print(type(numericSeconde))
print(*numericSeconde)
minValueFirstNumeric = numericFirst[0]
minValueSecondeNumeric = numericSeconde[0]
listFirst = []

for i in range(numericFirst):    
    if numericFirst[i] < minValueFirstNumeric:
        minValueFirstNumeric = numericFirst
    for j in range(numericSeconde):        
        if minValueSecondeNumeric[j] < minValueSecondeNumeric:
            minValueSecondeNumeric = numericSeconde[j]


