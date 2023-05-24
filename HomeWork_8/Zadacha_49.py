def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    while (choice != 10):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            suname = get_search_suname()
            print(find_by_suname(phone_book, suname))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice == 6:
            suname = get_search_suname()
            res = del_user(phone_book, suname)
            if (len(res) == len(phone_book) - 1):
                write_csv('phonebook.csv', res)
                phone_book = res
                print(f'Абонент с фамилией {suname} удален.')
            elif (len(res) == len(phone_book)):
                print(f'В справочнике нет абонентов с фамилией {suname}')
            else:
                print(
                    f'В справочнике более одного абонента с фамилией {suname}. Используйте удаление по номеру телефона.')
        elif choice == 7:
            number = get_search_number()
            res = del_user_num(phone_book, number)
            if (len(res) == len(phone_book) - 1):
                write_csv('phonebook.csv', res)
                phone_book = res
                print(f'Абонент с телефоном {number} удален.')
            elif (len(res) == len(phone_book)):
                print(
                    f'В справочнике нет абонентов с номером телефона {number}')
            else:
                write_csv('phonebook.csv', res)
                phone_book = res
                print(
                    f'В справочнике более одного абонента с телефоном {number}. Удалены все абоненты с этим номером.')
        elif choice == 8:
            suname = get_search_suname()
            res = del_user(phone_book, suname)
            if (len(res) == len(phone_book) - 1):
                user_data = get_new_user()
                add_user(res, user_data)
                write_csv('phonebook.csv', res)
                phone_book = res
                print(f'Абонент с фамилией {suname} изменен.')
            elif (len(res) == len(phone_book)):
                print(f'В справочнике нет абонентов с фамилией {suname}')
            else:
                print(
                    f'В справочнике более одного абонента с фамилией {suname}. Используйте изменение по номеру телефона.')
        elif choice == 9:
            number = get_search_number()
            res = del_user_num(phone_book, number)
            if (len(res) == len(phone_book) - 1):
                user_data = get_new_user()
                add_user(res, user_data)
                write_csv('phonebook.csv', res)
                phone_book = res
                print(f'Абонент с телефоном {number} изменен.')
            elif (len(res) == len(phone_book)):
                print(
                    f'В справочнике нет абонентов с номером телефона {number}')
            else:
                print(
                    f'В справочнике более одного абонента с телефоном {number}. Удалите дубли через функцию удаления.')
        choice = show_menu()


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента (по фамилии)\n"
          "7. Удалить абонента (по номеру телефона)\n"
          "8. Изменить данные абонента (по фамилии)\n"
          "9. Изменить данные абонента (по номеру телефона)\n"
          "10. Закончить работу")
    return int(input())


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def print_result(data: list) -> None:
    print('\nСправочник абонентов (Фамилия, Имя, Телефон, Описание):\n')
    for line in data:
        str = ''
        for el in line:
            str += line[el] + ' '
        print(str)


def get_search_suname():
    return input('\nВведите фамилию для поиска: ')


def find_by_suname(phone_book: list, suname: str) -> str:
    res = []
    for line in phone_book:
        if suname == line['Фамилия']:
            res.append(line['Телефон'])
    if (len(res) == 0):
        return f'В справочнике нет абонентов с фамилией {suname}'
    elif (len(res) == 1):
        return 'Телефон этого абонента: ' + res[0]
    else:
        return f'Телефоны абонентов с фамилией {suname}: ' + ', '.join(res)


def get_search_number():
    return input('\nВведите номер телефона: ')


def find_by_number(phone_book, phone) -> str:
    res = []
    for line in phone_book:
        if phone == line['Телефон']:
            res.append(line['Фамилия'])
    if (len(res) == 0):
        return f'В справочнике нет абонентов с телефоном {phone}'
    elif (len(res) == 1):
        return 'Фамилия этого абонента: ' + res[0]
    else:
        return f'Странно, но в справочнике несколько абонентов с телефоном {phone}: ' + ', '.join(res)


def get_new_user() -> list:
    print('Введите данные нового абонента:')
    new_user = []
    new_user.append(input('Фамилия: '))
    new_user.append(input('Имя: '))
    new_user.append(input('Телефон: '))
    new_user.append(input('Описание: '))
    return new_user


def add_user(phone_book, user_data):
    phone_book.append({'Фамилия': f'{user_data[0]}', 'Имя': f'{user_data[1]}',
                      'Телефон': f'{user_data[2]}', 'Описание': f'{user_data[3]}'})


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def get_file_name():
    return input('Укажите имя файла: ') + '.txt'


def write_txt(file_name, phone_book):
    with open(file_name, 'w', encoding='utf-8') as fout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def del_user(phone_book, suname) -> list:
    res = []
    for line in phone_book:
        if suname != line['Фамилия']:
            res.append(line)
    return res


def del_user_num(phone_book, number) -> list:
    res = []
    for line in phone_book:
        if number != line['Телефон']:
            res.append(line)
    return res


work_with_phonebook()
