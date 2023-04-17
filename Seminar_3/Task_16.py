# Ищем количество вхождиний числа в список

n = int(input("Введите размер списка: "))
s = []
count = 0
print("Введите элементы списка")
for i in range(n):
    N = int(input())
    s.append(N)
find = int(input("Какое число будем искать? "))
for i in range(len(s)):
    if find == s[i]:
        count += 1
print("Количество числа", find, "в списке -", count)