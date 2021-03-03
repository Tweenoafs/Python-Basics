price_list = [250.04, 320.50, 1200.90, 9, 90.15, 118.77, 28.14, 888, 559.80, 14]
print(f'ID элемента "9": {id(price_list[3])}')
print('-' * 145)

for el in price_list:
    value = str(f'{el:.2f}').split('.')
    print(f'{value[0]} руб {value[1]} коп',  end=' ')

print()
print('-' * 145)
price_list.sort()
print(f'Сортировка без создания нового списка: {price_list}')
print(f'ID элемента "9" после сортировки: {id(price_list[0])}')
print('-' * 145)

new_list = sorted(price_list, reverse=True)
print(f'Обратная сортировка списка с созданием: {new_list}')
print('-' * 145)
print(f'Первые 5 самых дорогих цены в списке: {sorted(price_list)[-5:]}')

