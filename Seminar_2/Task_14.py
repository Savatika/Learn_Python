# Степень числа 2
n = int(input())
N = 2
for i in range(n):
    if N**i < n:
        print(N**i)
