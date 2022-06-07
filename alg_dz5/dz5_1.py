import collections
from collections import namedtuple


def qua_count():
    company_name = input('Введи название организации')
    qu1, qu2, qu3, qu4 = 0, 0, 0, 0
    try:
        qu1 = int(input("Введи прибыль за первый квартал "))
        qu2 = int(input("Введи прибыль за второй квартал "))
        qu3 = int(input("Введи прибыль за третий квартал "))
        qu4 = int(input("Введи прибыль за четвертый квартал "))
    except ValueError:
        print("Ошибка значения")
        qua_count()
    company = (company_name, qu1, qu2, qu3, qu4)

    return company


def company_ben():
    try:
        n = int(input("Введите количество предприятий "))
    except ValueError:
        print("Ошибка значения")
        company_ben()

    company = namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4'])
    copm_d = {}
    for i in range(n):
        company_tuplf = company._make(qua_count())
        copm_d[f'company_{company_tuplf.name}'] = [company_tuplf.q1,
                                                   company_tuplf.q2,
                                                   company_tuplf.q3,
                                                   company_tuplf.q4
                                                   ]

    single_sum = [sum(ii) for ii in copm_d.values()]
    all_sum = sum(single_sum)

    for i in copm_d:
        if sum(copm_d[i]) < (all_sum / n):
            less_avr = i
        elif sum(copm_d[i]) > (all_sum / n):
            more_avr = i

    result = f'Общая прибль за год: {all_sum} \n ' \
             f'Средняя прибль за год {all_sum / n} \n' \
             f'Компания ниже среднего {less_avr} \n' \
             f'Комапания выше среднего {more_avr}'

    return result


print(company_ben())
