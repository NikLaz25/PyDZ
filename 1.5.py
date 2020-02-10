reseipt = int(input('Введите значение выручки, руб. '))
invest = int(input('Введите значение издержек, руб. '))
profit = reseipt - invest
if profit > 0:
    print('годовая выручка составляет ', profit, 'руб.')
    profitability = profit / reseipt
    print('Рентабельность составляет', profitability)
    staff = int(input('Укажите количество персонала '))
    prof_one = profit / staff
    print('Доля прибыли на каждого сотрудника составляет', prof_one, 'руб.')
else:
    if profit < 0:
        print('Фирма отработала в убыток', profit, 'руб.')
    else:
        print('Фирма отработала в ноль')


#вношу изменения, разбираюсь как работает GIT!!!!!!