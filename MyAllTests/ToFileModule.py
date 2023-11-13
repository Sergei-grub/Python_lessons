import json
notes = {
    "note": {
        "id": "1",
        "items": [{
            "name": "u_name",
            "text": "text",
            "date": "date_string"
        }]
    }
}



with open("data_file.txt", "a") as write_file:
    write_file.write("\n")
    json.dump(notes, write_file)




with open('data_file.txt', 'r') as f:
    for item in f:
        data_json = json.loads(f)
    print(data_json)

# Пример чтения данных JSON из файла
# with open('data.json', 'r') as file:
#     json_data = json.load(file)
#
# print(json_data)