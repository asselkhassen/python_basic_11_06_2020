""" Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self.__income


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.get_income()['wage'] + self.get_income()['bonus']


position = Position('Assel', 'Khassen', 'analyst', 350000, 660000)
print(position.get_full_name())
print(position.get_total_income())