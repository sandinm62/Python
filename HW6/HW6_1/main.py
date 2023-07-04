# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arifProgress(a, n, d, count = 1):
    if count == n:
        list_1.append(a + (count - 1) * d)
        return a + (count - 1) * d
    else:
        list_1.append(a + (count - 1) * d)
        return arifProgress(a, n, d, count + 1) 

# def printList(a, n, d):
        





firstNumber = int(input('Введите первое число: '))
defNumber = int(input('Введите разность: '))
countNumber = int(input('Введите количество элементов которое нужно вывести: '))

list_1 = []
arifProgress(firstNumber, countNumber,  defNumber)

print(*list_1)