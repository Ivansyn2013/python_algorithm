'''5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.'''

import random


def max_negative():
    a = []
    for i in range(100):
        a.append(random.randint(-100, 100))
    x = min(a)
    for i in a:
        if i < 0 and i > x:
            x = i
    print(a)
    return f'Максимальное из отрицательных - {x}. Положение в массиве - {a.index(x)}'


print(max_negative())
