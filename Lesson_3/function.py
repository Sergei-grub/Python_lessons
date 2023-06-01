# Лекция 2 Python. Функции, рекурсия, алгоритмы

""" def sum_numbers (n, y = 'Hellow'):
    print(y)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum, y

a = sum_numbers(5, 'qwerty')
print(a) """


def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q','e', 'l'))
