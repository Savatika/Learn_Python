# поиск индекса чисел в диапазоне

n = int(input(" от: "))
n1 = int(input("до: "))
s = [1, 2, 6, 3, -7, 22, -9, -3, 5, 13, 55, -43]
s1 = []

for i in range(len(s)):
    if s[i] >= n and s[i] <= n1:
        s1.append(i)

print(s1) 