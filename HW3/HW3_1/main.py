# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

number = int(input("Введите колличество символов которое нужно сформировать в строке: "))
list_1 = []                                                                                 
for i in range(number):
    n = random.randint(0, 10)
    list_1.append(n)

print(*list_1)
numbercCheck = int(input("Какое число вы хотите найти: "))
count = 0

for i in range(len(list_1)):
    if numbercCheck == list_1[i]:
        count += 1

print(count)







