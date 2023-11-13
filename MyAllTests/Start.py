import json
import datetime

from MyAllTests.Controller import current_date, current_id
from MyAllTests.ModifyData import rewrite_data
from MyAllTests.PrintNote import data_print

u_id = current_id(0)
u_name = "Jon"
text = "Как использовать JSON в Python. В Python JSON обрабатывается с помощью модуля json"
date_string = current_date()
new_name = "Sergei"

notes = {
    "note": {
        "id": u_id,
        "items": [{
            "name": u_name,
            "text": text,
            "date": date_string
        }]
    }
}

print(type(notes))
print(notes)
print("____")

for item in notes['note']['items']:
    if item['name'] == "Jon":
        item['name'] = new_name
    print(item['name'])
print(notes)

data_print(notes)
rewrite_data(notes)
data_print(notes)



