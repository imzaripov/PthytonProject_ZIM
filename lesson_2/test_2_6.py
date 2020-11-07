print('ТОВАРЫ')
goods = int(input('Введите количество товарных позиций:'))
n = 1
info = []
ls = []
analytica = {}
while n <= goods:
    info = dict({'название': input('Введите название:'), 'цена': input('Введите стоимость:'),
                 'количество': input('Введите количество:'), 'eд':input('Введите единицу измерения:')})
    ls.append((n, info))
    n += 1
    analytica = dict(
        {'название': info.get('название'), 'цена': info.get('цена'), 'количество': info.get('количество'),
         'ед': info.get('ед')})
print(ls)
print(analytica)
