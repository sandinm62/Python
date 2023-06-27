# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пузырьковая сортировка топ !!!!)

numericFirst = [8, 9, 9, 5, 5, 4, 7, 3]
numericSeconde = [2, 1, 1, 1, 6, 4, 13]
# print(type(numericFirst))
numericFirst = tuple(set(sorted(numericFirst)))

# print(type(numericFirst))

print(*numericFirst)
# print(type(numericSeconde))
numericSeconde = tuple(set(sorted(numericSeconde)))
print(*numericSeconde)
countNumeric1 = 0
countNumeric2 = 0


for i in range(len(numericFirst) + len(numericSeconde)):
    if countNumeric1 < len(numericFirst) and countNumeric2 < len(numericSeconde):
        minValue1 = numericFirst[countNumeric1]
        minValue2 = numericSeconde[countNumeric2]
        if minValue1 < minValue2:
            print(minValue1)
            countNumeric1 += 1
        elif minValue2 < minValue1:
            print(minValue2)
            countNumeric2 += 1
        else:
            print(minValue1)
            countNumeric1 += 1
            countNumeric2 += 1
    elif countNumeric1 >= len(numericFirst) and countNumeric2 < len(numericSeconde):
        print(numericSeconde[countNumeric2])
        countNumeric2 += 1
    elif countNumeric1 < len(numericFirst) and countNumeric2 >= len(numericSeconde):
        print(numericFirst[countNumeric1])
        countNumeric1 += 1

    
    




