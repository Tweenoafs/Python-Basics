from time import sleep


class TrafficLight:
    __color = ["Красный", "Жёлтый", "Зелёный", "Жёлтый"]

    def running(self):
        while True:
            for i in self.__color:
                if i == "Красный":
                    print("Стой!")
                    sleep(7)
                elif i == "Жёлтый":
                    print("Приготовься!")
                    sleep(2)
                elif i == "Зелёный":
                    print("Иди!")
                    sleep(10)


traffic_light = TrafficLight()
traffic_light.running()
