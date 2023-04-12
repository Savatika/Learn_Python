# нахождение суммы цифр числа
n = int(input("Введите трехзначное число: "))
count = 0
summ = 0
len_n = len(str(n))
while count < len_n:
    summ += n%10
    count += 1
    n = int(n/10)
print("Сумма цифр числа равна", summ)