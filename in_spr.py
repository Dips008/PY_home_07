def new_int():
    col = 'ID: '
    col += input('Введите ID: ')
    col += ' First Name: '
    col += input('Введите Имя: ')
    col += ' Last Name: '
    col += input('Введите Фамилию: ')
    col += ' Tel: '
    col += input('Введите Номер телефона: ')
    col += ' Comment: '
    col += input('Введите Комментарий: ')
    return col


def spr_in(s):
    with open('baza_tel.txt', 'a') as data:
        data.write(f'{s}\n')
        print('\nНовый контакт успешно добавлен!\n')
