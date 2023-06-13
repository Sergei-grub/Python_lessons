# Урок 4. Функции высшего порядка, работа с файлами

""" def f(x):
    return x * x

a = f
print(a(5))
print(f(5)) """


# ///////////////////////////////////////////////////////////////


""" def calc1(a, b):
    return a + b


def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calc1, 5, 45) """


# ///////////////////////////////////////////////////////////////


""" def calc2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))


math(lambda a, b:  a + b, 5, 45) """


# ///////////////////////////////////////////////////////////////


""" def retrn(lst):
    return ['slss' for i in lst if i % 2 == 0]

lst = [1,2,3,5,8,15,23,38, 44]
print(retrn(lst)) """


# ///////////////////////////////////////////////////////////////


""" def map(f, col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

lst = [1,2,3,5,8,15,23,38]
res = map(int, lst)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = map(lambda x: (x, x**2), res)
print(res) """


# ///////////////////////////////////////////////////////////////


""" lst1 = [x for x in range(1,20)]
print(lst1)

lst1 = list(map(lambda x: x + 10, lst1))
print(lst1) """


# ///////////////////////////////////////////////////////////////


""" data = '12 67 1223 34 5556 67 2 33'
lst = []
for i in data:
    tmp = data.split()
for x in tmp:
    lst.append(int(x))
print(lst) """


# ///////////////////////////////////////////////////////////////


""" data = list(map(int, data.split()))
print(data) """


# ///////////////////////////////////////////////////////////////

""" def where(f,col):
    return [x for x in col if f(x)]

lst = [1,2,3,5,8,15,23,38]
res = map(int, lst)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res) """


# ///////////////////////////////////////////////////////////////


""" data = [15, 65, 9 ,36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res) """


# ///////////////////////////////////////////////////////////////


""" lst = [1,2,3,5,8,15,23,38]
res = map(int, lst)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res) """


# ///////////////////////////////////////////////////////////////


""" users = ['user1', 'user2', 'user3']
id = [1, 2, 3, 4, 5]
lst = list(zip(id, users))
print(lst) """


# ///////////////////////////////////////////////////////////////


""" users = ['user1', 'user2', 'user3']
lst = list(enumerate(users))
print(*lst) """


# ///////////////////////////////////////////////////////////////


""" colors = ['red ', 'green ', 'blue ']
data = open('file.ai', 'a')
data.writelines(colors)
data.close """


# ///////////////////////////////////////////////////////////////


""" with open('file.txt', 'w') as data:
    data.write('line 2\n')
    data.write('line 3\n')

print(56) """


# ///////////////////////////////////////////////////////////////


""" path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)

data.close() """