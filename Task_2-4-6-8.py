""" 
Задача 2: 
Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
"""
""" 
usernum = int(input("Введите трехзначное число: "))
user_sum = (usernum % 10) + (usernum // 10 % 10) + (usernum // 100)
print(user_sum)
"""


""" 
Задача 4: 
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10 
"""
""" 
usernum = int(input("Сколько журавликов сделали дети: "))
kate = int(usernum / 3 * 2)
rebyata = int((usernum - kate) / 2)
print()
print(f"Катя сделала {kate}, Петя {rebyata}, Серёжа {rebyata}.")
"""


""" 
Задача 6: 
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no 
"""
""" usernum = str(input("Введите номер билета: "))
num1 = ''
num2 = ''
num1 = usernum[0:3]
num2 = usernum[3:6]
print(num1)
print(num2)
sum1 = (int(num1) % 10) + (int(num1) // 10 % 10) + (int(num1) // 100)
sum2 = (int(num2) % 10) + (int(num2) // 10 % 10) + (int(num2) // 100)
if sum1 == sum2:
    print(f"{usernum} > yes")
else: 
    print(f"{usernum} > no") """



""" 
Задача 8: 
Требуется определить, можно ли от шоколадки размером n х m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
3 2 4 -> yes
3 2 1 -> no 
"""
chocolate_x = int(input("Введите длину шоколадки (в дольках): "))
chocolate_y = int(input("Введите высоту шоколадки (в дольках): "))
part = int(input("Сколько долек вы хотите отломить?: "))
chocolate = chocolate_x * chocolate_y

if part % 2 == 0:
    print(f"{chocolate_x} {chocolate_y} {part} > yes")
else: 
    print(f"{chocolate_x} {chocolate_y} {part} > no")