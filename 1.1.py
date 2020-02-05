name = ('Саурон')
print(name)
age = int(input('Предположите сколько лет Саурону? '))
print(name, 'живет уже', age, 'лет')
data_god = int(input('А какой сейчас год? '))
bith_day = data_god-age
print('Cаурон родился в ', bith_day)
tall_s = float(input('Какой рост у Саурона?(укажите в метрах)' ))
tall_user = int(input('Каков ваш рост?(укажите в сантиметрах)'))
tall_user = float(tall_user/100)
if tall_user > tall_s:
    win = tall_user - tall_s
    print(f'Саурону {age} лет отроду, родился в {bith_day} и ниже вас на {win} м')
elif tall_user == tall_s:
    print(f'Саурон{age} лет отроду, родился в {bith_day} и одного роста с вами')
else:
    raznic = tall_s - tall_user
    print(f'Саурону {age} лет отроду, родился в {bith_day} и выше вас на {raznic} м')