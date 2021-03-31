class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    if b == 0:
        raise MyError("На ноль делить нельзя!")
except MyError as err:
    print(err)
else:
    c = a / b
    print(f"Ответ: {int(c)}")
