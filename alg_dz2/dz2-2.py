'''2. Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2
  нечетные (3 и 5).'''


def even_count():
    try:
        x = int(input('Введи натуральное число: '))
    except ValueError:
        print("Неправильный ввод")
        even_count()

    x = list(str(x))
    odd = []
    even = []
    for i in x:
        if float(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    res = f' Четных цифр: {len(even)}\n {even}\n Нечетных цифр: {len(odd)} \n {odd}'

    return res


print(even_count())
