warehouse = []
printers = []
scanners = []
xeroxes = []


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Equipment:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unit = {"Модель": {self.name}, "Цена": {self.price}, "Количество": {self.quantity}}


class Printer(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def storing(self):
        try:
            unit = self.name
            price = self.price
            quantity = self.quantity
            try:
                price = int(self.price)
                quantity = int(self.quantity)
                unit = {"Модель Принтера": unit, "Цена": price, "Количество": quantity}
                printers.append(unit)
                warehouse.append(printers)
            except:
                raise Error("Цена и количество должны быть числами")
        except Error as err:
            print(err)

    @property
    def info(self):
        return f"Информация о технике: Модель: {self.name}, Цена: {self.price}, Кол-во: {self.quantity}"


class Scanner(Equipment):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def storing(self):
        try:
            unit = self.name
            price = self.price
            quantity = self.quantity
            try:
                price = int(self.price)
                quantity = int(self.quantity)
                unit = {"Модель Сканера": unit, "Цена": price, "Количество": quantity}
                scanners.append(unit)
                warehouse.append(scanners)
            except:
                raise Error("Цена и количество должны быть числами")
        except Error as err:
            print(err)

    @property
    def info(self):
        return f"Информация о технике: Модель: {self.name}, Цена: {self.price}, Кол-во: {self.quantity}"


class Xerox(Equipment):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def storing(self):
        try:
            unit = self.name
            price = self.price
            quantity = self.quantity
            try:
                price = int(self.price)
                quantity = int(self.quantity)
                unit = {"Модель ксерокса": unit, "Цена": price, "Количество": quantity}
                xeroxes.append(unit)
                warehouse.append(xeroxes)
            except:
                raise Error("Цена и количество должны быть числами")
        except Error as err:
            print(err)

    @property
    def info(self):
        return f"Информация о технике: Модель: {self.name}, Цена: {self.price}, Кол-во: {self.quantity}"


u_1 = Printer("Xerox", 7000, 12)
u_2 = Scanner("Epson", 11000, 7)
u_3 = Xerox("HP", 15000, 5)
print()
u_1.storing()
u_2.storing()
u_3.storing()
print(warehouse)
