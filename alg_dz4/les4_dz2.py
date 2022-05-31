'''2. Написать два алгоритма нахождения i-го по счёту простого числа.

    Без использования «Решета Эратосфена»;
    Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию: Проанализировать
скорость и сложность алгоритмов. Результаты анализа сохранить
в виде комментариев в файле с кодом.
'''

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
def eratosfen(x):
    a = []
    for i in range (x):
        a.append(i)


    a[1] = 0
    m = 2
    while m < len(a):
        j = m*2
        while j < len(a):
            a[j] = 0
            j += m
        m +=1
    print('Eratosfen simple digit finder')
    return set(a)

@time_meg_wrapper_f
def divesion_simpe_dig_find(x):
    a = []
    for i in (range(x)):
        for j in range(2,i):
            if i%j ==0 :
                break
        a.append(i)

    print('Simple finder')
    return a

print(eratosfen(101))
print(divesion_simpe_dig_find(101))


print(eratosfen(1001))
print(divesion_simpe_dig_find(1001))
