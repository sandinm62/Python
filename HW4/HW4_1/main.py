# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import os

n = int(input("Введите длину первого множества: "))
m = int(input("Введите длинну второго множества: "))
numericFirst = []
numericSeconde = []

print("Вводите поочерёдно первое множество после каждого числа нажимайте клавишу Enter")
for i in range(n):
    numericFirst.append(int(input()))

print("Вводите поочерёдно первое множество после каждого числа нажимайте клавишу Enter")
for i in range(m):
    numericSeconde.append(int(input()))

numericFirst = tuple(set(sorted(numericFirst)))                 # убираем повторения и сортируем списко и конвертируем его в кортеж
numericSeconde = tuple(set(sorted(numericSeconde)))


def clear_console():                                            # чистим консоль чтобы увидеть ответ
    os.system('cls')
clear_console()
print(*numericFirst)
print(*numericSeconde)

for i in range(len(numericFirst)):
    for j in range(len(numericSeconde)):
        if numericFirst[i] == numericSeconde[j]:
            print(numericFirst[i])
            break
    
    



# Не правильно прочитал условия задаи но все равно получилось интересно, данный скрип сравниевает оба массива и выводит зачение по возрастанию без повторений =)

# numericFirst = [8, 9, 1, 9, 5, 5, 4, 7, 23]
# numericSeconde = [2, 1, 1, 1, 6, 4, 13]
# print(type(numericFirst))
# numericFirst = tuple(set(sorted(numericFirst)))

# print(type(numericFirst))

# print(*numericFirst)
# print(type(numericSeconde))
# numericSeconde = tuple(set(sorted(numericSeconde)))
# print(*numericSeconde)

# countNumeric1 = 0
# countNumeric2 = 0
# for i in range(len(numericFirst) + len(numericSeconde)):
#     if countNumeric1 < len(numericFirst) and countNumeric2 < len(numericSeconde):
#         minValue1 = numericFirst[countNumeric1]
#         minValue2 = numericSeconde[countNumeric2]
#         if minValue1 < minValue2:
#             print(minValue1)
#             countNumeric1 += 1
#         elif minValue2 < minValue1:
#             print(minValue2)
#             countNumeric2 += 1
#         else:
#             print(minValue1)
#             countNumeric1 += 1
#             countNumeric2 += 1
#     elif countNumeric1 >= len(numericFirst) and countNumeric2 < len(numericSeconde):
#         print(numericSeconde[countNumeric2])
#         countNumeric2 += 1
#     elif countNumeric1 < len(numericFirst) and countNumeric2 >= len(numericSeconde):
#         print(numericFirst[countNumeric1])
#         countNumeric1 += 1
