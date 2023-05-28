# a = list()
# b = []
# b.append(10)
# n = 5
# m = 10
# for i in range(n, m):
#     a.append(i)
# print(a)
# print(b)
# number = [4, 5, 2, 8]
# for i in range(len(number)):
#     if i == 3:
#         number[i] = 100
#     print(number[i])
# for i in number:
#     print(i)

# number = [1, 2, 3, 4, 5, 6]
# print(number[:3])
# print(number[3:])
# print(number[-2:])
# number = number[::-1]
# print(number)

# mn = set()
# mn = {1, 2, 3}
# mn.add(4)
# mn.add(4)
# print(mn)
# number = [1, 1, 2, 2, 3, 3]
# print(*set(number))

# sl = dict()
# sl = {"login": "vasya", "password": "123"}
# print(sl["login"])
# sl["address"] = "Moscow"
# print(sl)
# print(list(sl.keys()))
# print(list(sl.values()))
# for key, value in sl.items():
#     print(key, '-', value)
# print(list(sl.items()))
# sl = dict(sorted(list(sl.items())))
# print(sl)
# http://ya.ru?search=собака
#
# {"search": "собака"}

# coords = 1, 2
# coords1 = sorted(coords)
# print(coords[0], coords[1])
#
#
# def get_coords():
#     x = 4
#     y = 5
#     return x, y

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # for i in matrix:
# #     print(*i)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i % 2 == 0 and j % 2 != 0:
#             matrix[i][j] += 10
#         print(matrix[i][j], end=' ')
#     print()

# number = [1, 2, 3]
# number2 = number.copy()
# number3 = number[:]
# number.append(5)
# print(number)
# print(number2)

""" number = [1, 2, 3]
print(dir(number))
help(number.insert)
number.insert(0, 8)
print(number) """


""" Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6 """

""" number = [1,1,2,0,-1,3,4,4]
print(len(set(number))) """

""" lst =  [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(lst)))


number = [1, 1, 2, 0, -1, 3, 4, 4]
sl = {}
for el in number:
    sl[el] = sl.get(el, 0) + 3
    # if el not in sl:
    #     sl[el] = 1
    # else:
    #     sl[el] += 1
print(sl) """

""" Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
 """


""" number = [1, 2, 3, 4, 5]
k = 3
print(number[k:] + number[:k])
print(*number[len(number)-k+1:], *number[:k]) """


""" Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'} """


""" sl = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {" VIII": "S007"}]
print(sl)
temp = set()
for element in sl:
    temp.add(*element.values())
for i in temp:
    print(i) """


""" Семинар 3. Списки и словари
Задача No23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3) """

""" list = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list)-1):
    if list[i] < list[i + 1]:
        count += 1
    print(i)
print(f"Элементов массива, больших предыдущего: {count}")
 """

""" lst = [0, -1, 5, 2, 3]
print(len([i for i in range(len(lst) - 1) if lst[i] < lst[i + 1]])) """


for i in 5,:
    print(i)