def print_menu():
    print("""
    1 - Показать список контактов
    2 - Найти контакт
    3 - Добавить контакт 
    4 - Изменить контакт
    5 - Удалить контакт 
    6 - Выход  
    """)

def addContact(): # добавить контакт

    with open(file_path, 'a', encoding='utf8') as open_book:
        add_f = (input('Введите фамилию: ' ).title())
        add_i = (input('Введите Имя: ' ).title())
        add_o = (input('Введите Отчество: ' ).title())
        add_tel = (input('Введите телефон: ' ).title())
        new_line = add_f + ' ' + add_i + ' ' + add_o + ' ' + add_tel 
        open_book.writelines(f'\n{new_line}')
        print(new_line)

def searchContact(): # поиск контакта

    with open(file_path, 'r', encoding='utf8') as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if seach_param in line:
                print(line)

def removeContact(): # удалить контакт

    with open(file_path, 'r', encoding="utf-8") as open_book:
        X = input('Введите имя или фамилию для удаления: ')
        lines = open_book.readlines()
        with open(file_path, 'w', encoding="utf-8") as open_book:
            for line in lines:
                if X in line:
                    return print("Строка удалена")
                else:
                    print(line)    
                    open_book.write(line)


def editContact(): # редактировать контакт
    with open(file_path, 'r', encoding="utf-8") as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        with open (file_path, 'w', encoding='utf8') as open_book:
            for line in seach_param:
                if seach_param in line:
                    print(line)
                    add_f = (input('Введите фамилию: ' ).title())
                    add_i = (input('Введите Имя: ' ).title())
                    add_o = (input('Введите Отчество: ' ).title())
                    add_tel = (input('Введите телефон: ' ).title())
                    new_line = add_f + ' ' + add_i + ' ' + add_o + ' ' + add_tel  + '\n'
                    line = line.replace(line, new_line)
                return open_book.writelines(line)

def readAll(): # показать все контакты
    with open(file_path, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  



def tasks(task):
   if task > 6: 
    print('Вы ошиблись')
   if task == 6: 
       print('До свидания!')
   else:
    match task:
        case 1: 
            readAll()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))   
        case 2: 
            searchContact()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 3: # добавить контакт
            addContact()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 4: # изменить контакт
            editContact()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 5: # удалить контакт
            removeContact()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))            

file_path = 'phone_book.txt'
print_menu()
tasks(int(input('Введите номер задачи от 1 до 6: ')))