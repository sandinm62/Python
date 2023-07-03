# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def degree(a, b, count = 1, numDegree = 1):
    
    if count == b:
        numDegree = numDegree * a
        return numDegree
    else:
        numDegree = numDegree * a       
        count += 1
        return(degree(a, b, count, numDegree))


number = int(input('Введите число которое будете возводить в степень: '))
degreNumber = int(input('Введите степень числа: '))

print(degree(number, degreNumber)) 

    