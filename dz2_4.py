primordial_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                   'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for el in primordial_list:
    name = el.split()[-1]
    print(f'Привет, {name.title()}!')
