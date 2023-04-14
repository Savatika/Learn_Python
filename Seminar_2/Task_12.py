# Катя отгадывает числа Пети.

x = 0
y = 0
S = int(input("Сумма чисел: "))
P = int(input("Произведение чисел: "))
for i in range(1, S + 1):
    for j in range(1, P + 1):
        if i + j == S:
            if i * j == P:
                x = i
                y = j
print(x, y)

