# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter number: '))
summ = 0
count = 0
while summ < n:
    summ = 2 ** count
    if summ > n:
        break
    print(summ)
    count+=1



