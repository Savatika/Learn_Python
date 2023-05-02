# наш массив

a = int(input()) # начало массива
b = int(input()) # шаг
c = int(input()) # количество элементов
w = a
s = [a]
for i in range(1, c):
    w += b
    s.append(w)
print(s)

