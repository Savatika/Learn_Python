# Счастливый билет
number = input("Введите шестизначное число: ")
first_trio = int(number[0: 3])
last_trio = int(number[3: 6])
count = 0
summ_first = 0
summ_last = 0
len_n = 3
while count < len_n:
    summ_first += first_trio % 10
    summ_last += last_trio % 10
    count += 1
    first_trio = int(first_trio/10)
    last_trio = int(last_trio/10)
print(summ_first)
print(summ_last)
if summ_first == summ_last:
    print("Yes")
else:
    print("No")