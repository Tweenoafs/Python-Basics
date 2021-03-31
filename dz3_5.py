from random import randrange
from random import choice

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']


def get_jokes(n, repeat=False):
    """
    Функция возвращает случайную последовательность слов, формирующих шутки из трех списков
    :param n: кол-во шуток
    :param repeat: повтор/не повтор
    :return: список случайных шуток
    repeat=False -- флаг уникальности
    """

    jokes_list = []
    while n and len(nouns):
        elem = randrange(len(adjectives))
        if repeat:
            jokes_list.append(f'{nouns.pop(elem)} {adverbs.pop(elem)} {adjectives.pop(elem)}')
        else:
            jokes_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return jokes_list


print(get_jokes(5))
