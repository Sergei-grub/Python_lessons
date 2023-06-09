"""
Работа ученика С.А. Грубова.

Урок 3. Списки и словари
"""

""" 
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
3
-> 1 
"""
""" usernum = int(input('Введите кол-во элементов: '))
list = [i for i in range(1, usernum + 1)]
print(*list)
fndnum = int(input('Введите искомое число: '))
count = 0
for i in range(len(list)):
    if fndnum == list[i]:
        count += 1
if fndnum > len(list): print('Такого числа нет в списке.')
else: print(f'-> {count}') """


""" 
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
6
-> 5 
"""

""" usernum = int(input('Введите кол-во элементов: '))
list = [i for i in range(1, usernum + 1)]
print(*list)
fndnum = int(input('Введите искомое число: '))
min = max = eq = 1
for i in range(len(list)):
    if fndnum > list[i]:
        max = list[i]     
    elif fndnum == list[i]:
        eq = list[i]
if fndnum == eq:
    print(f'Заданное число {fndnum} равно элементу {eq}')
elif fndnum > max:
    print(f'Самый близкий по величине элемент к заданному числу {fndnum} -> {max}')
elif fndnum < min: 
    print(f'Самый близкий по величине элемент к заданному числу {fndnum} -> {min}')  """


""" 
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
*Пример:*
ноутбук
12 
"""
rus = {1:'АВЕИНОРСТ',
       2:'ДКЛМПУ',
       3:'БГЁЬЯ',
       4:'ЙЫ',
       5:'ЖЗХЦЧ',
       8:'ШЭЮ',
       10:'ФЩЪ'}
eng = {1:'AEIOULNSTR',
       2:'DG',
       3:'BCMP',
       4:'FHVWY',
       5:'K',
       8:'JX',
       10:'QZ'}
print(rus.items())
print(eng.items())
print()
count = 0 
userchoiсe = input('Выберите язык. Для русского нажмите '"1"', для английского '"2"': ')
if userchoiсe == '1':
    userword = input('Введите слово: ').upper()
    for i in userword:
        for (k,v) in rus.items():
            if i in v:
                count += k
    print('Стоимость слова в игре: ', count)
elif userchoiсe == '2':
    userword = input('Введите слово: ').upper()
    for i in userword:
        for (k,v) in eng.items():
            if i in v:
                count += k
    print('Стоимость слова в игре: ', count)