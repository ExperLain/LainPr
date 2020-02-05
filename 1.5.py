cost = int(input('Введите значение издержек: '))
revenue = int(input('Введите значение выручки: '))
if cost > revenue:
    print('издержки больше выручки')
elif cost == revenue:
    print('издержки равны выручке')
else:
    cost < revenue
    print('Выручка больше издержек')
    profit = revenue - cost
    rent = profit/revenue
    print(f'Рентабельность предприятия {rent}')
    man = int(input('Введите количество сотрудников: '))
    man = profit/man
    print(f'На одного сотрудника приходится {man} денег')