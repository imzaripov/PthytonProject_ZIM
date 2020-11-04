dis = int(input('Дневная дистанция:'))
res = int(input('Общий результат:'))
day = 1
while dis <= res:
    dis = dis + (dis * 0.1)
    day += 1
    print(f'{day}-й день - {dis:.2f} км')
print(f'Результат не менее {dis:.0f} км на - {day} день')
