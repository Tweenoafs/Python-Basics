def val_checker(callback_):
    def _val_checker(func):
        def wrapper(number):
            if callback_(number):
                print(func(number))
            else:
                raise ValueError(f'wrong value: {number}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
    b = calc_cube(-5)
except ValueError as error:
    print(error)
