# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
list_1 = []
number = int(input("Введите длинну массива: "))

for i in range(number):
    list_1.append(random.randint(0, 10))

print(*list_1)

numberCheck = int(input("Введите значение которое хотите проверить: "))

for i in range(len(list_1)):
    if (list_1[i] == numberCheck) or (list_1[i] % numberCheck == 1) or (numberCheck % list_1[i] == 1):
        print(list_1[i])
        break

