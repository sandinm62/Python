# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random

x = random.randint(1, 1000)
y = random.randint(1, 1000)

print(x + y)
print(x * y)

x1 = int(input())
y1 = int(input())
if x1 == x and y1 == y:
    print("true")
elif x1 == y and y1 == x:
    print("true")
else:
    print("False")


