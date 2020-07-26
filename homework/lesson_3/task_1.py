""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division():
    while True:
        try:
            divisible = float(input('Введите делимое: '))
            divider = float(input('Введите делитель: '))
            return divisible / divider
        except ValueError:
            print('Неверное значение данных')
        except ZeroDivisionError:
            print('На ноль делить нельзя!')


print(division())
