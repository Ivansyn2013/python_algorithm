'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в
 диапазоне от 2 до 9.
'''

def multiple():
    a = [x for x in range(2, 100)]
    res = {}

    for i in a:
        for ii in range(2, 10):
            if i % ii == 0:
                res.setdefault(ii, []).append(i)

    return res

print(multiple())