# Урок 5. Рекурсия и алгоритмы

""" 
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""

""" def fib_r(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib_r(num - 1) + fib_r(num - 2)
        
num = int(input('Введите число: '))
print(fib_r(num)) """


""" 
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1 
"""

""" import random
def mix(list):
    for i in range(len(list)):
        if list[i] == max(list):
            list[i] = min(list)
    return list


vasiliy_num = [random.randint(1, 5) for i in range(int(input('Введите количество оценок: ')))]
print(vasiliy_num)
mix(vasiliy_num)
print(vasiliy_num) """


""" 
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
"""
""" 
num = int(input('Введите число для проверки: '))
if num % 1 == 0 and num % 2 == 1 and num % 3 != 0:
    print('yes')
else:
    print('no')
print(num) """



""" def prost(n):
    if n % 1 == 0 and n % 2 != 0 and n % 3 != 0:
        st = "Yes"
    else:
        st = "No"
    return st


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input('Введите число для проверки: '))
print(is_prime(num)) """


""" 
Задача №37. Решение в группах
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 412
Output: 4 3 
"""

num = str(input('Введите число элементов: '))
print(num)
print(num[::-1])


""" def nums_ret(num):
    if len(num) == 0:
        return []
    else:
        return [num[-1]] + nums_ret(num[:-1])


num = str(input('Введите числа: '))
print(nums_ret(num)) """



""" 
def reverse_numbers(numbers):
    if len(numbers) == 0:
        return []
    else:
        return [numbers[-1]] + reverse_numbers(numbers[:-1])


def in_out(n):
	if n == 0:
		return
	k = input('Введите число: ' )
	in_out(n - 1)
	print(k, end=' ')


n = int(input('Введите число элементов: '))
in_out(n) """