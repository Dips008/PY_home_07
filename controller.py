import in_spr
import out_spr
import sort


def start():
    i = 0
    while i:
        print('Сделайте выбор:')
        print('1 - внести новую запись в справочник')
        print('2 - вывести записи справочника')
        print('0 - выход из справочника')
        k = int(input('Введите: '))
        if k == 1:
            new_col = in_spr.new_int()
            in_spr.spr_in(new_col)
        elif k == 2:
            out_spr.spr_out()
        i = k
