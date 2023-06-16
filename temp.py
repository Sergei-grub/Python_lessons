import os
from pathlib import Path


""" def show_all_records():
    file1 = open('d:\\Разработчик\\Python\\Python_lessons\\temp.py', "a", encoding="utf8")
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
            # выводим строку
        print(*line.strip().split(';'))
        # закрываем файл
    file1.close """



""" directory = os.getcwd()
file_name = '\\addressbook.txt'
path_to = directory + file_name
print(path_to) """

""" def show_all_records(path_to):
    file1 = open('d:\\Разработчик\\Python\\Python_lessons\\file.txt', "r", encoding="utf8")
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
            # выводим строку
        print(*line.strip().split(';'))
        # закрываем файл
        file1.close
directory = os.getcwd()
file_name = '\\addressbook.txt'
path_to = directory + file_name
show_all_records(path_to) """

""" with open('d:\\Разработчик\\Python\\Python_lessons\\file.txt', 'r', encoding="utf8") as f:
    for i in range(40):
        line = f.readline()
        print(line)
        # Возвращаемся к началу файла
        f.seek(0)
 """

""" script_dir = os.path.dirname(__file__) 
rel_path = "file.txt"
abs_file_path = os.path.join(script_dir, rel_path)
f = open(abs_file_path, 'a', encoding="utf8")
next_id = str(1)
f.write('asad')

f = open(abs_file_path, "r")
while True:
    # считываем строку
    line = f.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip()) """

id = 1
list_1 = []
list_1.append(str(id))
list_1.append(str(id))
path_ = 'd:\\Разработчик\\Python\\Python_lessons\\file.txt'
for line_no, line in enumerate(open(path_, encoding="utf8"), start=1):
    print (line_no, line)
""" user_del = input('Введите данные для удаления (фамилию, имя или телефон): ')
with open(path_,"r+", encoding="utf8") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in f:
        if user_del not in new_f:
            f.write(line) """
"""             f.write(input("Введите Фамилию: "))
            f.write(";")
            f.write(input("Введите имя: "))
            f.write(";")
            f.write(input("Введите телефон: "))
            f.write(";")
            f.close """

fnd = input("Введите поисковый запрос: ")
with open(path_, "r+", encoding="utf8") as file1:
    for line in file1.writelines():
        if fnd in line:
            file1.write(input("Введите Фамилию: "))
            file1.write(";")
            file1.write(input("Введите имя: "))
            file1.write(";")
            file1.write(input("Введите телефон: "))
            file1.write(";")
            print(*line.strip().split(';'))
    file1.close