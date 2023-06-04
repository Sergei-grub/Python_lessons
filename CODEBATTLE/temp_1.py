""" 
*
Создайте функцию, которая принимает три числа и возвращает сумму квадратов двух наибольших чисел.
Примеры:
13  == solution(1, 2, 3)
2  == solution(1, 1, 1)
8  == solution(1, 2, 2)
45  == solution(6, 3, 2)
41  == solution(2, 4, 5) """

""" def fun(a,b,c) -> int:
    v = sorted((a,b,c))
    return v[-1] ** 2 + v[-2] ** 2
 """
""" def fun(a,b,c) -> int:
    list = sorted((a,b,c))
    return list[-1] ** 2 + list[-2] ** 2

a = 6
b = 3
c = 8
print(fun(a,b,c)) """



""" 
За каждые 6 купленных кофейных чашек вы получаете 7-ю чашку бесплатно. 
В общей сложности, вы получаете 7 чашек. 
Создайте функцию, которая принимает n купленных чашек и рассчитывает общее количество чашек. """

""" def solution(cups: int) -> int:
    s = cups // 6
    return s + cups

cups = 240
print(solution(cups)) """


""" 
Создайте функцию, которая принимает две строки и верните индекс 
первого вхождения строки second в строку first, в ином случае верните -1.

Примеры:
5  == solution("some str", "st")
-1  == solution("some str", "11")
1  == solution("some str", "ome")
0  == solution("test", "t") """

""" def solution(first: str, second: str) -> int:
    if second in first:
        return first.index(second)
    else: return -1
print(solution("some str", "st")) """


""" Фермер просит вас посчитать сколько ног у всех его животных. 
Фермер разводит три вида: курицы = 2 ноги коровы = 4 ноги свиньи = 4 ноги 
Фермер посчитал своих животных и говорит вам, сколько их каждого вида. 
Вы должны написать функцию, которая возвращает общее число ног всех животных.

Примеры:

36  == solution(2, 3, 5)
22  == solution(1, 2, 3)
50  == solution(5, 2, 8) """

""" def solution(chickens: int, cows: int, pigs: int) -> int:
    return (chickens * 2) + (cows * 4) + (pigs *4)

print(solution(2, 3, 5)) """