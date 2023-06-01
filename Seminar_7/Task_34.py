# Винни-Пух ищет рифму 

# контрольный стих: пара-ра-рам рам-пам-папам па-ра-па-да   

stih = input("Винни, напиши свой стих: ")

vowes = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
s = stih.split()
vowes_list = []
flag = True

for i in range(len(s)):
    vowes_list.append(list(filter(lambda x: x in vowes, s[i])))
for i in range(len(vowes_list) - 1):
    if len(vowes_list[i]) != len(vowes_list[i + 1]):
        flag = False
        break

    
if flag == True:
    print("Парам пам-пам")
else: 
    print("Пам парам")

    



