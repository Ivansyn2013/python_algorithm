'''4. Определить, какое число в массиве встречается чаще всего.'''
import random
def more_offen():
    a = []
    for i in range(100):
        a.append(random.randint(0,100))
    x = 0
    for  i  in a:
        if a.count(i) > x:
            x = i
    print(a)
    return f'Число {x} встречается {a.count(x)} раза'


print(more_offen())