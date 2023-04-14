# Переворот монеток

N = int(input("Введите количество монеток: "))
print("Вводите результаты броска монеток. 1 - орел, 0 - решка.")
orel = 0
reshka = 0
for i in range(1, N + 1):
    n = int(input())
    if n == 1:
        orel += 1
    elif n == 0:
        reshka += 1
if orel < reshka:
    print(orel)
else: 
    print(reshka)
