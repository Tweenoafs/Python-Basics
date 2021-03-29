class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return self.amount - other.amount
        return "В первой ячейке меньше клеток, чем во второй!"

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        return self.amount // other.amount

    def make_order(self, rows):
        numb = divmod(self.amount, rows)
        return "\n".join(["*" * rows for _ in range(numb[0])]) + '\n' + "*" * numb[1]


cell_1 = Cell(12)
print(cell_1.make_order(5))
print()
cell_2 = Cell(15)
print(cell_2.make_order(4))
print(cell_1 - cell_2)
