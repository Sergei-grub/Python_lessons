""" Работа ученика С.А. Грубова. """

"""  
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Укажите количество элементов: '))
result = []
for i in range(n):
    result.append(a1 + i * d)
print(result)


""" Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) """

""" stat_list = [11, 6, 15, -6, 2, 9, 0, -19, 36, 1]
min = int(input('Введите минимальный индекс массива: '))
max = int(input('Введите максимальны индекс массива: '))
print(stat_list)
print(stat_list[min:max+1]) """
