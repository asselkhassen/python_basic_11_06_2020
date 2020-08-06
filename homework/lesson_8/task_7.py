""" Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, value):
        self.__value = value

    def __get_value(self):
        return self.__value

    def __str__(self):
        return str(self.__value)

    def __add__(self, other):
        return ComplexNumber(self.__value + other.__get_value())

    def __mul__(self, other):
        return ComplexNumber(self.__value * other.__get_value())


number_1 = ComplexNumber(12)
number_2 = ComplexNumber(565)
print(number_1.__add__(number_2))
print(number_1.__mul__(number_2))