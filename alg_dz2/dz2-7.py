'''
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных
 чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''


def proof():
    try:
        n = int(input('введи натуральное число:  '))
    except ValueError:
        print("Неправильный ввод")
        proof()

    x = (n * (n + 1)) / 2
    y = sum(i for i in range(1, n + 1))

    return True if x == y else False


print(proof())
