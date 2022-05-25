'''4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество
элементов (n) вводится с клавиатуры.'''


def through_one():
    try:
        x = int(input('Введи количество вывода: '))
        if x < 0:
            print('Неправильный ввод')
            through_one()
    except ValueError:
        print("Неправильный ввод")
        through_one()

    y = 1
    n = 0
    while x > 0:
        n += y
        y /= -2
        x -= 1

    return n

print(through_one())