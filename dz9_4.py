class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Автомобиль в движении.")

    def stop(self):
        print("Автомобиль остановился.")

    def turn(self, direction):
        print(f"Автомобиль повернул {direction}.")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


class TownCar(Car):

    def info(self):
        print(f"{self.color} городской автомобиль, марка {self.name}, едет со скоростью {self.speed}км/ч.")
        if self.is_police:
            print("Инспекторы потеряли мигалку!")

    def show_speed(self):
        print(f"Скорость: {self.speed}км/ч.")
        if self.speed > 60:
            print("Превышение, снизьте скорость!")


class SportCar(Car):

    def info(self):
        print(f"{self.color} спортивный автомобиль, марка {self.name}, едет со скоростью {self.speed}км/ч.")
        if self.is_police:
            print("Инспекторы потеряли мигалку!")


class WorkCar(Car):

    def info(self):
        print(f"{self.color} рабочий автомобиль, марка {self.name}, едет со скоростью {self.speed}км/ч.")
        if self.is_police:
            print("Инспекторы потеряли мигалку!")

    def show_speed(self):
        print(f"Скорость: {self.speed}км/ч.")
        if self.speed > 40:
            print("Превышение, снизьте скорость!")


class PoliceCar(Car):
    def info(self):
        print(f"Полицейский автомобиль, едет со скоростью {self.speed}км/ч.")


car_1 = TownCar(50, "Черный", "Honda", 0)
car_1.go()
car_1.turn("налево")
car_1.info()
car_1.show_speed()
car_1.stop()
print()
car_2 = SportCar(110, "Жёлтый", "Porsche", 1)
car_2.go()
car_2.turn("направо")
car_2.info()
car_1.turn("налево")
car_2.show_speed()
car_2.stop()
print()
car_3 = WorkCar(55, "Белый", "Renault", 0)
car_3.go()
car_3.turn("направо")
car_3.info()
car_3.show_speed()
car_3.stop()
print()
car_4 = PoliceCar(90, "Синий", "Ford", 1)
car_4.go()
car_4.turn("налево")
car_4.info()
car_2.turn("направо")
car_4.show_speed()
car_4.stop()
