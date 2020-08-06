""" Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

from enum import Enum


class DatePart(Enum):
    DAY = 0
    MONTH = 1
    YEAR = 2


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_date(cls, date):
        result = []
        idx = 0
        for number in date.split('-'):
            number_int = int(number)
            cls.validate_date(number_int, idx)
            result.append(number_int)
            idx += 1
        return result

    @staticmethod
    def validate_date(number, date_part):
        if date_part == DatePart.DAY.value:
            if number > 31:
                return ValueError('Число дней превышает')
        if date_part == DatePart.MONTH.value:
            if number > 12:
                return ValueError('Количество месяцев превышает')
        if date_part == DatePart.YEAR.value:
            if number < 1970:
                return ValueError('Ошибка')


today = Date('06-08-2020')
print(Date.extract_date('06-08-2020'))