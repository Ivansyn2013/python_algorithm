import random


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    left = merge_sort(arr[:(len(arr) // 2)])
    right = merge_sort(arr[len(arr) // 2:])
    n = m = k = 0

    c = [0] * (len(arr))

    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            c[k] = left[n]
            n += 1
        else:
            c[k] = right[m]
            m += 1
        k += 1

    while n < len(left):
        c[k] = left[n]
        k += 1
        n += 1
    while m < len(right):
        c[k] = right[m]
        k += 1
        m += 1

    return c


get_data = [random.randint(0, 50) for i in range(50)]

print(get_data)

print(merge_sort(get_data))
