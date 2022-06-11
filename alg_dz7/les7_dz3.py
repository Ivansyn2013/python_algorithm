'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках.
'''

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


n = int(input('Put number: '))

get_data = [random.randint(0, 100) for i in range(2 * n + 1)]
print(get_data)
print(fast_sort(get_data))
print(f'Median of list is {get_data[int((len(get_data) - 1) / 2)]}')

# я не очень понял задание.
# Как найти такой элемент без сортировки? Ведь в случайном наборе может быть так , что
# нет такого числа, чтобы слева были только меньше, а справа только больше,а
# если отсортировать, то такое число будет всегда -\-_-/-
