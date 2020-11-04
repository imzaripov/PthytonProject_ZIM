x = 2
y = x + 18
z = x ** y
print('Значение переменной z:', z)

age = input('Ваш возраст:')
weight = int(input('Ваш вес:'))
height = int(input('Ваш рост:'))
index_m = weight / (height * 0.01) ** 2
print(f'Индекс массы:{index_m:.2f}')
if index_m >= 18.5 or index_m <= 24.9:
    print('Норма')
if index_m >= 30.0:
    print('Ожирение некой степени')
