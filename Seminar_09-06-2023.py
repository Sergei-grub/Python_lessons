# Урок 7. Функции высшего порядка (семинар)


""" def square1(x):
    return x ** 2


square2 = lambda x: x ** 2

print(square1(2))
print(square2(2))

def summa(x, y):
    return x + y

summa1 = lambda x, y: x + y """


""" sp = ["1", "2", "3", "4"]
sp1 = map(int, sp)
for i in sp1:
    print(i)

sp = [1, 2, 3, 4, 5]
sp1 = map(lambda x: x ** 2, sp)
for i in sp1:
    print(i) """


""" sp = [1, 2, 3, 4, 5]
sp = filter(lambda x: x % 2 == 0, sp)
print(list(sp))


sp = [x ** 2 for x in range(1, 6)]
sp = [x for x in range(1, 6) if x % 2 == 0] """


""" sp = list(map(int, input().split()))
sp = [int(i) for i in input().split()]
print(sp) """


""" letters = ["a", "b", "c"]
numbers = [1, 2, 3]
print(*zip(letters, numbers)) """


""" week = ["пн", "вт", "ср"]
for n, day in enumerate(week, 1):
    print(n, "-", day) """


""" Задача №47. Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values. """


""" values = [1, 23, 42, 'asdfg']
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print('fail') """


""" Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна 

Ввод:
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    print(*find_farthest_orbit(orbits))
Вывод:
    2.5 10

(pi = 3,1415926535)
"""

""" def find_farthest_orbit (list_1):
    temp = finde = 0
    pi = 3.14
    for i,k in list_1:
        temp = pi * i * k
        if temp > finde and i != k: 
            finde = temp
    return finde


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
 """



""" def find_farthest_orbit(lst):
    square_orbits = [int(3.14 * val[0] * val[1]) for val in lst if val[0] != val [1]]
    max_index = square_orbits.index(max(square_orbits))
    return lst[max_index]

    
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits)) """


""" def find_farthest_orbit(orbits):
    lst_without_circles = [i for i in orbits if i[0] != i[1]]
    return max(lst_without_circles, key=lambda x: 3.14 * x[0] * x[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits)) """


""" Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print(‘same’)
else:
print(‘different’) 

Вывод: same
"""



""" def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    first = characteristic(objects[0])
    lst = [characteristic(i) == first for i in objects]  
    return (False, True)[len(lst) == sum(lst)]


values = [0, 2, 10, 6, 5]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different') """

x = 1023 
y = x % 1003
print(y)