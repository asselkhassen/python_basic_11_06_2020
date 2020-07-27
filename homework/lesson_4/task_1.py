""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def salary():
    while True:
        try:
            hours = int(input('Введите выработку в часах: '))
            salary_for_hour = int(input('Введите ставку в час: '))
            award = int(input('Введите премию: '))
            return (hours * salary_for_hour) + award
        except ValueError:
            print('Неверное значение данных')


print(salary())

