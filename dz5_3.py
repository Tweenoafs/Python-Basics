from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Константин', 'Кристина'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def tuple_gen():
    for i in tuple(zip_longest(tutors, klasses)):
        yield i


x = tuple_gen()

print(type(tuple_gen()))

while True:
    print(next(x))
