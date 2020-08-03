""" Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self):
        self.title = 'ручка'
        super(Pen, self).__init__(self.title)

    def draw(self):
        print('Началась отрисовка ручкой.')


class Pencil(Stationery):

    def __init__(self):
        self.title = 'карандаш'
        super(Pencil, self).__init__(self.title)

    def draw(self):
        print('Началась отрисовка карандашом.')


class Handle(Stationery):

    def __init__(self):
        self.title = 'маркер'
        super(Handle, self).__init__(self.title)

    def draw(self):
        print('Началась отрисовка маркером.')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()