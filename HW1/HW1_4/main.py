# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


print("Введите колличество самолётиков которое собрали дети(кратное 6): ")
air = int(input())
while air %6 !=0:
    print("Вы ввели число не кратное 6, повторите попытку ввода либо введите -1 для завершения программы: ")
    air = int(input())
    if air == -1:
        break


airPetya = air // 3 // 2
airSeryezha = airPetya
airKatya = airPetya * 4


print(airPetya, airKatya, airSeryezha)
