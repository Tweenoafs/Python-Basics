trans_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(keys):
    for key, value in trans_dict.items():
        if keys == key:
            return f'"{value}"'
    return None


print(num_translate('five'))
