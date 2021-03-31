primordial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
                   'была', '+5', 'градусов']

modified_list = []

for el in primordial_list:
    if not el.isalpha():
        if int(el) < 10:
            el = '0'.join(el).rjust(2, '0')
        el = ''.join("'" + el + "'")
    modified_list.append(el)
print(modified_list)

end_string = ' '.join(modified_list)
print(f'{end_string.capitalize()}.')
