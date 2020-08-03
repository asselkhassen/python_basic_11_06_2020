""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


from enum import Enum


class Direction(Enum):
    LEFT = 'налево'
    RIGHT = 'направо'


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.name = name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Магина повернула ' + direction.value)

    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.is_police = is_police
        self.speed = speed
        self.name = name
        super(TownCar, self).__init__(self.speed, self.color, self.name, self.is_police)

    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)
        if self.speed > 60:
            print('Превышение скорости')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.is_police = is_police
        self.speed = speed
        self.name = name
        super(WorkCar, self).__init__(self.speed, self.color, self.name, self.is_police)

    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)
        if self.speed > 40:
            print('Превышение скорости')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.is_police = is_police
        self.speed = speed
        self.name = name
        super(SportCar, self).__init__(self.speed, self.color, self.name, self.is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.is_police = is_police
        self.speed = speed
        self.name = name
        super(PoliceCar, self).__init__(self.speed, self.color, self.name, self.is_police)


town_car = TownCar(80, 'Красная', 'Town Car', False)
print(town_car.speed)
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
town_car.go()
town_car.stop()
town_car.turn(Direction.LEFT)
town_car.show_speed()

work_car = WorkCar(30, 'Желтая', 'Work Car', False)
sport_car = SportCar(50, 'Серая', 'Sport Car', False)
police_car = PoliceCar(50, 'Черная', 'Police Car', True)