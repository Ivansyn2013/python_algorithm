from time import perf_counter


def time_meg_wrapper_f(func):
    def my_wrapper(*args, **kwargs):
        start = perf_counter()
        take_f = func(*args, **kwargs)
        end = perf_counter()
        print(f'working time = {end - start}')
        return take_f

    return my_wrapper


@time_meg_wrapper_f
def try_f(*args, **kwargs):
    res = f'Its my dump function {args}'
    return res


print(try_f('gopa'))
