'''8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна
вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце
 следует вывести полученную матрицу.
 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''


def matrix_5_4():
    x = []
    res = []
    collumns = []
    max_min_in_coll = []
    for i in range(4):
        x = []
        try:
            x = (input("Введи 4 числа через пробел: ").split(' '))
        except ValueError:
            print("Ошибка значений")
            return matrix_5_4()
        except TypeError:
            print("Ошибка значений")
            return matrix_5_4()

        if len(x) < 4 or not all(map(str.isdigit, x)):
            print('Ошибка значений')
            return matrix_5_4()

        x = [*map(int, x)]

        res.append(x)

    for i in res:
        print(*i, f'| {sum(i)}')
    for i in range(len(res)):
        collumns.append([])

    for ii in res:
        for inx, elm in enumerate(ii):
            collumns[inx].append(elm)

    for i in collumns:
        max_min_in_coll.append(min(i))

    return f'Максимальный из минимальных в столбцах  = {max(max_min_in_coll)}'


print(matrix_5_4())
