# Задача 26:  Посчитать факториал (произведение 1 до N) 

n = int(input('Введите число: '))
c = 1
fact = 1

def factorial(n, c, fact):   
    c += 1
    if c <= n:
        fact *= c
    else:
        return fact
    return factorial(n, c, fact)
        
print(factorial(n, c, fact))

# и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

N = int(input('Введите число: '))
C = 1
arProg = 1

def arithmeticProgression(n, c, arProg):   
    c += 1
    if c <= n:
        arProg += c
    else:
        return arProg
    return arithmeticProgression(n, c, arProg)
        
print(arithmeticProgression(n, c, arProg))