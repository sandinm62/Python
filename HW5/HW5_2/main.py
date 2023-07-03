# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def summ(numberSum, count = 0):
    if count == numberSum:
        print(count)
        return count
    else:
        summ(numberSum, count + 1)


number1 = int(input())
number2 = int(input())
sum = number1 + number2
summ(sum)