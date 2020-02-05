time_all = int(input('Введите количество секунд: '))
sec = time_all % 60
mint = time_all // 60
hour = mint // 60
mint = mint % 60
print(f'{hour} ч/{mint} мин/{sec} сек')