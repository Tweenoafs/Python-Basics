class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return f"{self.re} - {abs(self.im)}j"
        else:
            return f"{self.re} + {self.im}j"

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re, self.im * other.im)


c_1 = Complex(15, 22)
c_2 = Complex(3, -5)
print(f"Сложение: {c_1 + c_2}")
print(f"Умножение: {c_1 * c_2}")