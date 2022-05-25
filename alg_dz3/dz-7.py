'''7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
 между собой (оба являться минимальными), так и различаться.'''
import random


def find_all_min():
    a = []
    for i in range(20):
        a.append(random.randint(0, 100))
    print(a)
    a.sort()

    return a[:2]


print(find_all_min())
