import json
import time
import requests
import os.path
import hashlib
import pprint

url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

cou_list = []
response = requests.get(url).json()
for countries in response:
    cou_list.append(countries["name"]["common"])


class Iterator:

    def __init__(self, c_list):
        self.c_list = c_list
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            c_name = self.c_list[self.start]
            c_url = f'https://wikipedia.org/wiki/{self.c_list[self.start].replace(" ", "_")}'
        except IndexError:
            raise StopIteration
        self.start += 1
        return f'Country: {c_name}, url: {c_url}'


if __name__ == '__main__':
    with open('countries.json', 'w', encoding='utf-8-sig') as c:
        final_list = []
        for item in Iterator(cou_list):
            final_list.append(item)
            print(item)
        json.dump(final_list, c, ensure_ascii=False, indent=2)

    def gen(path):
        with open(path, encoding='utf-8-sig') as p:
            for i in p:
                hash_object = hashlib.md5(i.encode())
                yield hash_object.hexdigest()

    file_path = os.path.abspath('countries.json')
    generator = gen(file_path)

    for item in generator:
        print(item)