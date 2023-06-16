# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Enter number:")
number = int(input())
summ = 0

while number > 0:
    remains = number % 10
    summ += remains
    number //= 10

print("Summ = ", summ)