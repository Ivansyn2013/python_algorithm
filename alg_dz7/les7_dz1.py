import random


def bubble_sort(ar):
    res = ar
    n = 1
    while n < len(res):
        for i in range(len(res) - 1):
            if res[i] < res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
        n += 1
    return res


get_data = [random.randint(-100, 100) for x in range(50)]

print(get_data)

print(bubble_sort(get_data))
