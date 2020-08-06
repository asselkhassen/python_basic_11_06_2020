""" Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByNull(ZeroDivisionError):

    def __init__(self):
        self.text = 'Нельзя делить на ноль'

    def __str__(self):
        return self.text


divisible = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))

try:
    if divider == 0:
        raise DivisionByNull()
    print(divisible / divider)
except DivisionByNull as err:
    print(err)


