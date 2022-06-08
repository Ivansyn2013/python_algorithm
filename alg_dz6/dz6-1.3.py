'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным эл
ементами. Сами минимальный и максимальный элементы в сумму не включать.
'''
import random
import sys


def sum_of_maxmin():
    a = []
    for i in range(20):
        a.append(random.randint(0, 100))

    b = a[a.index(min(a)) + 1:a.index(max(a))]
    print(a)
    print(b, min(a), max(a))

    print('a get size -', sys.getsizeof(a))
    print('b get size -', sys.getsizeof(b))

    return 'Элементов нет' if len(b) == 0 else f' Сумма элементов = {sum(b)}'


print(sum_of_maxmin())


print('Function get size -', sys.getsizeof(sum_of_maxmin()))