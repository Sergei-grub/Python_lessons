from MyAllTests.Controller import current_date


def rewrite_data(data):
    print("___ Изменить название заметки ___")
    new_name = input("Введите новое название: ")
    new_date = current_date()
    for item in data['note']['items']:
        item['name'] = new_name
        item['date'] = new_date

