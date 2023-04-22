# сбор черники

N = int(input('Введите длину списка: '))
s = []


print("Вводите элементы списка: ")
for i in range(N):
    n = int(input())
    s.append(n)
    
count = s[0] + s[1] + s[2]

for j in range(len(s) - 2):

    s1 = s[j] + s[j + 1] + s[j + 2]
    if count < s1:
        count = s1
    
print(count)