my_list = []
edited_list = []

# for i in range(1, 1000):
#     if i % 2 == 0:
#         my_list.append(i ** 3)

for i in range(1, 1000, 2):
    my_list.append(i ** 3)

# my_list = [1, 6859, 27, 125, 79507]   # Для быстрой проверки

amount = 0
ed_amount = 0
new_amount = 0

for el in range(len(my_list)):
    count = 0
    elem = my_list[el]
    while elem > 0:
        count += elem % 10
        elem //= 10
    if count % 7 == 0:
        amount += my_list[el]
    # my_list[el] += 17         #Для варианта без создания нового списка раскомментировать
print(f'Сумма: {amount}')

# Этот блок для задания C закомментить до строки 40
for i in my_list:
    edited_list.append(i + 17)

for idx, val in enumerate(edited_list):
    ed_count = 0
    while val > 0:
        ed_count += val % 10
        val //= 10
    if ed_count % 7 == 0:
        ed_amount += edited_list[idx]
print(f'Сумма: {ed_amount}')
# До этой


# Для варианта без создания нового списка раскомментировать

# for el in range(len(my_list)):
#     count = 0
#     elem = my_list[el]
#     while elem > 0:
#         count += elem % 10
#         elem //= 10
#     if count % 7 == 0:
#         new_amount += my_list[el]
# print(f'Сумма: {new_amount}')
