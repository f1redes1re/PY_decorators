from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
    contacts_d = {}
    pattern = re.compile(r"(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s*\(*(доб\.\s*\d+)*\)*")
    for contact in contacts_list:
        contact[-2] = re.sub(pattern, r"+7(\2)\3-\4-\5 \6", contact[-2]).strip()
        if contact[1] == '':
            name_separated = contact[0].split(' ')
            contact[0] = name_separated[0]
            contact[1] = name_separated[1]
            try:
                contact[2] = name_separated[2]
            except IndexError:
                contact[2] = ''
        if contact[2] == '':
            first_name_separated = contact[1].split(' ')
            contact[1] = first_name_separated[0]
            try:
                contact[2] = first_name_separated[1]
            except IndexError:
                contact[2] = ''

        key = contact[0] + "_" + contact[1]
        value = [contact[2], contact[3], contact[4], contact[5], contact[6]]

        if key not in contacts_d:
            contacts_d[key] = value
        else:
            for cnt in range(len(contacts_d[key])):
                if contacts_d[key][cnt] == '':
                    contacts_d[key][cnt] = value[cnt]

    new_list = []
    for key in contacts_d:
        row = key.split("_")
        for value in contacts_d[key]:
            row.append(value)
        new_list.append(row)

    for n in new_list:
        print(n)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_list)
