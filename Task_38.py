# Работа ученика С.А. Грубова.
# ///////////////////////////////////////////////////////////////


""" 
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных  """

import os


def show_all_records(path_to):
    for line_no, line in enumerate(open(path_to, encoding="utf8"), start=1):
        print(line_no, *line.strip().split(';'))


def add_contact(path_to):
    data = open(path_to, 'a', encoding="utf8")
    data.write("\n")
    data.write(input("Введите Фамилию: "))
    data.write(";")
    data.write(input("Введите имя: "))
    data.write(";")
    data.write(input("Введите телефон: "))
    data.write(";")
    data.close


def search_record(path_to):
    fnd = input("Введите поисковый запрос: ")
    with open(path_to, "r", encoding="utf8") as file1:
        for line in file1.readlines():
            if fnd in line:
                print("Есть такой! >")
                print(*line.strip().split(';'))


def del_record(path_to):
    for line_no, line in enumerate(open(path_to, encoding="utf8"), start=1):
        print (line_no, *line.strip().split(';'))
    user_del = input('Введите данные для удаления (фамилию, имя или телефон): ')
    with open(path_to,"r+", encoding="utf8") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if user_del not in line:
                f.write(line)                
        f.truncate()


def main():
    script_dir = os.path.dirname(__file__) 
    rel_path = "Аddressbook.txt"
    path_to = os.path.join(script_dir, rel_path)
    id = 0
    menu_list = ["-----------------------------------------",
                 "\t1 - Показать справочник",
                 "\t2 - Добавить контакт",
                 "\t3 - Найти контакт",
                 "\t4 - Удалить контакт",
                 "\t0 - Выход."]
    for i in menu_list:
        print(i)
    select = int(input("Выберите действие: "))
    print()
    if select == 1:
        show_all_records(path_to)
        main()
    elif select == 2:
        add_contact(path_to)
        main()
    elif select == 3:
        search_record(path_to)
        main()
    elif select == 4:
        del_record(path_to)
        main()
    elif select == 0:
        print("До скорых встреч!")
        return 

main()