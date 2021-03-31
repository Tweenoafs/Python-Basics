class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split("-"):
            my_date.append(int(i))
        return f"{my_date[0]}-{my_date[1]}-{my_date[2]}"

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 2020 >= year > 0:
            return f"Всё верно."
        if day < 1 or day > 31:
            return f"Неверное число!"
        if month < 1 or month > 12:
            return f"Неверный месяц"
        if year < 1 or year > 2020:
            return f"Введите год от 1 до 2020"

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


the_date = Date("04-11-2020")
print(Date.validation(4, 11, 2020))
print(Date.extract("04-11-2020"))
