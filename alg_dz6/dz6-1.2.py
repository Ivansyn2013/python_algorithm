'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random
import sys
def change_places():
    a = []
    for x in range(10):
        a.append(random.randint(0,10))
    print(a)
    a_max = a.index(max(a))
    a_min = a.index(min(a))
    a[a_max],a[a_min] = a[a_min],a[a_max]

    print('a get size -', sys.getsizeof(a))
    print('amin get size -', sys.getsizeof(a_min))
    print('amax get size -', sys.getsizeof(a_max))
    return a

print(change_places())

print('Function get size -', sys.getsizeof(change_places()))