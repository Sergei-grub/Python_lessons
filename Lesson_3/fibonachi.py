# Лекция 2 Python. Функции, рекурсия, алгоритмы

""" n = int(input('Ввудите значение: '))
fib1 = fib2 = 1
fib = 0
for i in range(n):
    print(fib, end = ' ')
    fib1 = fib2
    fib2 = fib
    fib = fib1 + fib2 """


""" n = int(input('Введите длину ряда: '))
f1 = f2 = 1
print(f1, f2, end=' ')
 
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ') """


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))