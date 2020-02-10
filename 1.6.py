result1 = int(input('Введите первоначальный результат, км '))
result2 = int(input('Введите конечный результат, км '))
res_middle = result1 * 1.1
day = 1
if result1 < result2:
    while res_middle < result2:
        res_middle = res_middle * 1.1
        day = day + 1
    print('Спортсмен достигнет конечного результата за ', day, 'дн.')
else:
    print('Результаты введены неверно')
# вношу изменения, разбираюсь как работает GIT оставляю коммит из master
# изменения на ветке new1 оставляю коммит из new1
# очередные изменения


