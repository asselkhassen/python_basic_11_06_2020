""" Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
"""


from enum import Enum
from time import sleep


class TrafficColor(Enum):
    RED = 'красный'
    YELLOW = 'желтый'
    GREEN = 'зеленый'
    NONE = 'none'


class TrafficLight:
    __color = TrafficColor.NONE

    def running(self):
        while True:
            self.__color = TrafficColor.RED
            print(self.__color.value)
            sleep(7)
            self.__color = TrafficColor.YELLOW
            print(self.__color.value)
            sleep(2)
            self.__color = TrafficColor.GREEN
            print(self.__color.value)
            sleep(5)


light = TrafficLight()
light.running()
