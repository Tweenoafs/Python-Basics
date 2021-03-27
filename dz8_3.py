from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        my_list = [i for i in (*args, *kwargs.values())]
        nums = [f'{func.__name__}({i}: {type(i)})' for i in my_list]
        print(*nums, *func(*args, **kwargs), sep=',\n')

    return wrapper


@type_logger
def calc_cube(*x, **y):
    my_list = [i for i in (*x, *y.values()) if isinstance(i, int) or isinstance(i, float)]
    return [i ** 3 for i in my_list]


a = calc_cube(3, 7.4, 22, 45, 19.5)
print(calc_cube.__name__)
# print(a)
