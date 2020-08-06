"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.


Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

from enum import Enum


class Department(Enum):
    FINANCE = 'Отдел финансов'
    IT = 'Отдел ИТ'
    HR = 'Отдел кадров'


class OfficeEquipment:

    def __init__(self, brand, width, length, height):
        self.brand = brand
        self.width = width
        self.length = length
        self.height = height


class Printer(OfficeEquipment):

    def __init__(self, brand, width, length, height):
        super(Printer, self).__init__(brand, width, length, height)
        self.brand = brand
        self.width = width
        self.length = length
        self.height = height

    def __str__(self):
        return 'Printer ' + str(self.brand) + ' width: ' + str(self.width) + ' height: ' + str(self.height) + ' length: ' + str(self.length)


class Scanner(OfficeEquipment):

    def __init__(self, brand, width, length, height):
        super(Scanner, self).__init__(brand, width, length, height)
        self.brand = brand
        self.width = width
        self.length = length
        self.height = height

    def __str__(self):
        return 'Scanner ' + str(self.brand) + ' width: ' + str(self.width) + ' height: ' + str(self.height) + ' length: ' + str(self.length)


class Xerox(OfficeEquipment):

    def __init__(self, brand, width, length, height):
        super(Xerox, self).__init__(brand, width, length, height)
        self.brand = brand
        self.width = width
        self.length = length
        self.height = height

    def __str__(self):
        return 'Xerox ' + str(self.brand) + ' width: ' + str(self.width) + ' height: ' + str(self.height) + ' length: ' + str(self.length)


class Warehouse:

    def __init__(self):
        self.__scanners = []
        self.__xeroxes = []
        self.__printers = []
        self.__logs = {
            Department.FINANCE.name: {
                'printers': [],
                'scanners': [],
                'xeroxes': []
            },
            Department.IT.name: {
                'printers': [],
                'scanners': [],
                'xeroxes': []
            },
            Department.HR.name: {
                'printers': [],
                'scanners': [],
                'xeroxes': []
            }
        }

    def accept(self, equipment):
        if type(equipment) is Printer:
            self.__printers.append(equipment)
        if type(equipment) is Scanner:
            self.__scanners.append(equipment)
        if type(equipment) is Xerox:
            self.__xeroxes.append(equipment)

    def distribution(self, equipment_type, department):
        if equipment_type == 'Printer':
            if len(self.__printers) > 0:
                printer = self.__printers.pop()
                self.__logs[department.name]['printers'].append(printer)
            else:
                print('Принтера нет на складе')
        if equipment_type == 'Scanner':
            if len(self.__scanners) > 0:
                scanner = self.__scanners.pop()
                self.__logs[department.name]['scanners'].append(scanner)
            else:
                print('Сканнера нет на складе')
        if equipment_type == 'Xerox':
            if len(self.__xeroxes) > 0:
                xerox = self.__xeroxes.pop()
                self.__logs[department.name]['xeroxes'].append(xerox)
            else:
                print('Ксерокса нет на складе')

    def __str__(self):
        result = ''

        print(self.__logs)
        for printer in self.__printers:
            result += printer.__str__() + '\n'

        for printer in self.__xeroxes:
            result += printer.__str__() + '\n'

        for printer in self.__scanners:
            result += printer.__str__() + '\n'
        return result


wr = Warehouse()

while True:
    try:
        printer_sum = int(input('Сколько принтеров добавить? '))
        for el in range(0, printer_sum):
            wr.accept(Printer('HP', 30, 20, 10))
        break
    except ValueError:
        print('Это должно быть чисто')

while True:
    try:
        scanner_sum = int(input('Сколько сканнеров добавить? '))
        for el in range(0, scanner_sum):
            wr.accept(Scanner('HP', 30, 20, 10))
        break
    except ValueError:
        print('Это должно быть чисто')

while True:
    try:
        xerox_sum = int(input('Сколько ксероксов добавить? '))
        for el in range(0, xerox_sum):
            wr.accept(Xerox('HP', 34, 12, 445))
        break
    except ValueError:
        print('Это должно быть чисто')

# printer_1 = Printer('HP', 30, 20, 10)
# printer_2 = Printer('Samsung', 15, 25, 15)
# scanner_1 = Scanner('HP', 30, 20, 10)
# scanner_2 = Scanner('Samsung', 20, 35, 18)
# xerox_1 = Xerox('HP', 34, 12, 445)
# xerox_2 = Xerox('Samsung', 21, 54, 665)
#
# wr.accept(printer_1)
# wr.accept(printer_2)
# wr.accept(scanner_1)
# wr.accept(scanner_2)
# wr.accept(xerox_1)
# wr.accept(xerox_2)

wr.distribution(Printer.__name__, Department.IT)
wr.distribution(Scanner.__name__, Department.HR)
wr.distribution(Xerox.__name__, Department.FINANCE)

print(wr)

