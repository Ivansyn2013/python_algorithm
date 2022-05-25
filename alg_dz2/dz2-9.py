'''9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр.'''


def max_sum_digit():
    res = 0
    x = input('Введи последовательность чисел через пробел:  ').split(' ')
    if not all(map(str.isdigit, x)):
        print('Введены не цифры')
        max_sum_digit()
    else:

        for i in x:
            sum_d = sum(map(int, list(str(i))))
            if sum_d > res:
                res = sum_d
        print(f'Максимальная сумма = {res}')
    return None


max_sum_digit()
