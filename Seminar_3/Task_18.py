# Ближайшее число в списке

n = int(input("Введите размер списка: "))
s = []
count = 0
number = 0
total = 0

print("Введите элементы списка")
for i in range(n):
    N = int(input())
    s.append(N)

x = int(input("какое число будем искать? "))
flag = 0
while flag == 0:
    for i in range(len(s)):
        if s[i] == x:
            flag = 1
            number = s[i]
        elif s[i] + total == x:
            flag = 1
            number = s[i]
        elif s[i] - total == x:
            flag = 1
            number = s[i]
    total += 1
print("Ближайшее число -", number)