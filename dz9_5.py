class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Ваше сообщение: '{self.title}'. Запуск отрисовки.")


class Pen(Stationary):

    def draw(self):
        print(f"Отрисовка началсь, Ваш выбор: {self.title}.")


class Pencil(Stationary):

    def draw(self):
        print(f"Отрисовка началсь, Ваш выбор: {self.title}.")


class Handle(Stationary):

    def draw(self):
        print(f"Отрисовка началсь, Ваш выбор: {self.title}.")


start = Stationary("Привет!")
start.draw()
pen = Pen("ручка")
pen.draw()
pencil = Pencil("карандаш")
pencil.draw()
handle = Handle("маркер")
handle.draw()