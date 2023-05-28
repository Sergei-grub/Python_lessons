# Урок 2. Коллекции данных. Профилирование и отладка
""" 
# Списки []
list1 = []
list_2 = list()
list1 = [4, 2, 3, 44, 6]

for i in range(5):
    list_2.append(i)
    print(*list_2)
print(list1)
print(list1.pop(6))
print(list1) """

""" list1 = []
for i in range(1, 11):
    list1.append(i)
print(list1)
print(list1[0])
print(list1[len(list1)-1])
print(len(list1))
print(*list1[5:6])
print(*list1[:2])
print(list1[len(list1) - 2:])
print(*list1[2:4])
print()
print(*list1[5:],  *list1[:5]) """

""" 
# Картеж (, )
t = ()
print(type(t))

t = (1, 4, 8, )
print(type(t))

v = [1, 6, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b = 1, 2
с = а = 2

a, b, c = v
print(a, b, c) """


""" 

t = (1, 2, 3, 5, )
for i in range(len(t)):
    print(t[i]) """

""" t = [1, 2, 3, 5]
t[0] = 2
print(*t) """

""" 
# Словари {}
d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d['q']) """

""" dic = {}
dic = {'up': '1', 'left': '<', 'right':'>'}
print(dic)
print(dic['left'])

dic[888] = 1234

print(dic)

del dic ['up']
print(dic)

for i in dic:
    print('{}: {}'.format(i, dic[i]))


print(dic.items())
for (v) in dic.items():
    print(v)

print(dic.items())
for (k,v) in dic.items():
    print(v) """


""" 
# Множества

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')
print(colors)
colors.add('grey')
print(colors)
colors.add(123)
print(colors)
colors.remove(123)
print(colors)

colors.clear()
print(colors)

q = set()
print(colors)
print(q) """


""" # Операции со множествами в Python

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()    # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}
 """

""" a = {1, 8, 6}
b = frozenset(a)
print(b) """


