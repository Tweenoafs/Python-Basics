from abc import abstractmethod, ABC


class Cloth(ABC):
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return f"Общее количество ткани: {self.param + other.param}"

    @abstractmethod
    def materials(self):
        pass


class Coat(Cloth):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    @property
    def materials(self):
        return f"Ткань для пальто: {round(self.param / 6.5 + 0.5, 2)}"


class Costume(Cloth):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    @property
    def materials(self):
        return f"Ткань для костюма: {round((2 * self.param + 0.3) / 100, 2)}"


coat = Coat(18)
print(coat.materials)
costume = Costume(37)
print(costume.materials)
print(coat + costume)












