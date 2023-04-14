# Делим шоколадку
n = int(input("Введите количество долек по вертикали: "))
m = int(input("Введите количество долек по горизонтали: "))
kolDol = int(input("Количество долек какое хотите вы? "))
flag = 0
if n == 1 or m == 1 and kolDol == 1:
    flag = 1
else:
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if i * j == kolDol:
                flag = 1
if flag == 1:
    print("YEEEES")
else:
    print("no, no, god please no, NO!!!")   

n = int(input())
for i in range(1, n + 1):
    i = 0
    if i < n:
        print(n**i)