class Worker:
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        self._income["wage"] = self.wage
        self._income["bonus"] = self.bonus
        total = sum(self._income.values())
        print(f"Оклад: {total}р.")


wrkr_1 = Position("Павел", "Смирнов", "Директор", 200000, 50000)
wrkr_1.get_full_name()
wrkr_1.get_total_income()
wrkr_2 = Position("Василий", "Пупкин", "Бухгалтер", 100000, 20000)
wrkr_2.get_full_name()
wrkr_2.get_total_income()



