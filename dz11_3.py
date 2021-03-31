class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
print("Введите числа для заполнения списка, для окончания нажмите 'q'.")

while True:
    try:
        variable = input("Введите число или 'q' для выхода: ")
        if variable.lstrip("-").isdigit() == 1:
            my_list.append(int(variable))
        elif variable == "q":
            print(f"Получился вот такой список: {my_list}")
            break
        else:
            raise MyError("Можно вводить только числа!")
    except MyError as err:
        print(err)



