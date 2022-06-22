def select_sort(array_s):
    a = array_s
    for i in range(len(a)):
        ind_min = i
        for j in range(i + 1, len(a)):

            if a[j] < a[ind_min]:
                ind_min = j
        tmp = a[ind_min]
        a[ind_min] = a[i]
        a[i] = tmp
    return a


def insertion_sort(arr):
    a = arr
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j - 1] > v) and j > 0:
            a[j] = a[j - 1]
            j -= 1
        a[j] = v
        print(a)
    return a


def bubble_sort(arr_s):
    a = arr_s
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i + 1] < a[i]:
                a[i], a[i + 1] = a[i + 1], a[i]
        print(a)
        n += 1
    return a


import random


def fast_sort(ar_s, start=0, end=None):
    def subpart(ar_s, start, end, pivot_index):
        ar_s[start], ar_s[pivot_index] = ar_s[pivot_index], ar_s[start]
        pivot = ar_s[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if ar_s[y] <= pivot:
                ar_s[y], ar_s[x] = ar_s[x], ar_s[y]
                x += 1
            y += 1

        ar_s[start], ar_s[x - 1] = ar_s[x - 1], ar_s[start]

        return x - 1

    if end is None:
        end = len(ar_s) - 1
    if end - start < 1:
        return ar_s

    pivot_index = random.randint(start, end)
    x = subpart(ar_s, start, end, pivot_index)
    fast_sort(ar_s, start, x - 1)
    fast_sort(ar_s, x + 1, end)
    return ar_s


arrr = [4, 3, 8, 7, 9, 1, 2]
# print(select_sort(arrr))
# print(insertion_sort(arrr))
# print(bubble_sort(arrr))
print(fast_sort(arrr))
sss = 'dfd fdfd'

print(list(sss))

qq = 'fdfdf'
print(list(qq))
print([i  for i in range (0,10)])
print(qq[1:])
leni = [0]*10

for i in range(3):
    x = '.append(1)'
    exec(f'leni[{i}]=2')
    print(leni)

test_dict = {'test': (1,2), 'test2': (3,4)}
# print(len(test_dict))
# print(test_dict.popitem())
# print(len(test_dict))
print(test_dict.items())
