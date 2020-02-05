number_n = int(input('Введите целое положительное число: '))
number_x = number_n % 10
number_n = number_n // 10
while number_n > 0:
    if number_x <= number_n % 10:
        number_x = number_n % 10
    number_n = number_n // 10
print(number_x)
