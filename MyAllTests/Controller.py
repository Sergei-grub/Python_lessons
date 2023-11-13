import datetime


def current_date():
    date = datetime.datetime.now()
    date_string = date.strftime('%m.%d.%y %H:%M:%S')
    return date_string


def current_id(old_id):
    note_id = []
    new_num = old_id + 1

    note_id.append(new_num)
    print(id)



