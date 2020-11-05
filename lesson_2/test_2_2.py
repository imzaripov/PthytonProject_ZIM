ls = []
n = int(input('Введите количество и элементы списка:'))
for i in range(0, n):  # функция range
    el = input()
    ls.append(el)
print(ls)
el = 0
for i in range(int(len(ls) / 2)):
    ls[el], ls[el + 1] = ls[el + 1], ls[el]  # обмен значениями через кортежи
    el = el + 2
print('Изменённый список')
print(ls)
