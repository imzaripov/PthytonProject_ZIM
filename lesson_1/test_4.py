# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

n = int(input('Задайте число n:'))
maxima = n % 10
n = n // 10
while n > 0:
    if n % 10 > maxima:
        maxima = n % 10
    n = n // 10
print('Самая большая цифра -', maxima)
