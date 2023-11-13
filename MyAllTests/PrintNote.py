

def data_print(data):
    print("___ Вывод данных ___")
    print("Id =", data['note']['id'])
    for n_item in data['note']['items']:
        print("date =", n_item['date'])
        print("name =", n_item['name'])
        print("text =", n_item['text'])