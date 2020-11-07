# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

n = int(input('Введите номер месяца:'))
if n < 1 or n > 12:
    print('У нас пока григорианский календарь')
    n = int(input('Введите номер заново:'))
x = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for key in x.keys():  # запускаем цикл возврата ключей в словаре
    if n in x[key]:  # как только номер месяца попадает в значения ключей, выводим сам  ключ на print
        print(f'это - {key}')
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
         'Октябрь', 'Ноябрь', 'Декабрь']
for ind, el in enumerate(month):  # класный финт - присвоение физических номеров индексам
    if ind + 1 == n:  # с учётом индексации от 0, увеличиваем на 1, при равенстве номера индексу, выводится значение
        #  списка, соотвествующее индексу.
        print(f'а точнее - {el}')