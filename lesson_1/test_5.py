revenue = int(input('Выручка:'))
costs = int(input('Издержки:'))
if revenue >= costs:
    profit = revenue - costs
    print('Прибыль:', profit)
    n = int(input('Численность сотрудников:'))
    pr_mem = profit / n
    print('Прибыль на сотрудника:', pr_mem)
else:
    profit = revenue - costs
    print('Убыток:', profit)
