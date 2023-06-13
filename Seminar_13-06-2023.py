# ///////////////////////////////////////////////////////////////
# Урок 8. Работа с файлами
# ///////////////////////////////////////////////////////////////

""" colors = ['red ', 'green ', 'blue ']
data = open('file.txt', 'a')
data.writelines(colors)
data.close
 """

"""  sp = ["567\n", "888"]
with open("../../file.txt", "a", encoding="utf8") as f:
    f.writelines(sp) """

""" with open("F:/Программирование/Python/Python_lessons/file.txt", "r", encoding="utf8") as f:
    data = f.readlines()
    data = list(map(str.strip, data))
    print(data) """

# ///////////////////////////////////////////////////////////////

""" Задача №49. Общее обсуждение
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной 

Образец записи в справочнике: Иванов;Иван;Иванович;456465

Построчное считывание файла:
file1 = open("sample.txt", "r")

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip())

# закрываем файл
file1.close


with open('file.txt', 'r') as f:
    for i in range(40):
        line = f.readline()
        # Возвращаемся к началу файла
        f.seek(0)

"""


def show_all_records():
    file1 = open("F:/Программирование/Python/Python_lessons/file.txt", "r", encoding="utf8")
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


def search_record():
    fnd = input("Введите поисковый запрос: ")
    with open("F:/Программирование/Python/Python_lessons/file.txt", "r", encoding="utf8") as file1:
        for line in file1.readlines():
            if fnd in line:
                print("Есть такой! >")
                print(line)


def add_contact():
    data = open('F:/Программирование/Python/Python_lessons/file.txt', 'a', encoding="utf8")
    data.write("\n")
    data.write(input("Введите Фамилию: "))
    data.write(";")
    data.write(input("Введите имя: "))
    data.write(";")
    data.write(input("Введите телефон: "))
    data.write(";")
    data.close


def main():
    menu_list = ["-----------------------------------------",
                 "\t1 - Показать справочник; ",
                 "\t2 - Добавить контакт; ",
                 "\t3 - Найти контакт; ",
                 "\t4 - Выход."]
    for i in menu_list:
        print(i)
    select = int(input("Выберите действие: "))
    print()
    if select == 1:
        show_all_records()
        main()
    elif select == 2:
        add_contact()
        main()
    elif select == 3:
        search_record()
    elif select == 4:
        print("До скорых встреч!")
        return 

main()
