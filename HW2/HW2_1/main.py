# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

number = int(input())
count = 0
eagle = 0
tails = 0
while count < number:
    money = random.randint(0, 1)
    print(money)
    if money == 0:
        tails+=1
    else:
        eagle+=1
    count+=1

if eagle < tails:
    print("Нужно перевернуть: ", eagle)
else:
    print("Нужно перевернуть: ", tails)
