import os
from datetime import datetime


# Home task 1
def log_decor(function):
    def new_function(*args):
        with open('log.txt', 'w', encoding='utf-8-sig') as log:
            date = datetime.today()
            some_func = function(*args)
            log.write(f'Дата и время лога: {date}\n'
                      f'Имя функции: {function.__name__}\n'
                      f'Аргументы: {[*args]}\n'
                      f'Результат функции: {some_func}')
            return some_func
    return new_function


@log_decor
def logger(*args):
    print(args*2)


# Home task 2
def path_decor(abspath):
    def log(function):
        def new_path_func(*args):
            with open(abspath, 'w', encoding='utf-8-sig') as log:
                date = datetime.today()
                some_func = function(*args)
                log.write(f'Дата и время лога: {date}\n'
                          f'Имя функции: {function.__name__}\n'
                          f'Аргументы: {[*args]}\n'
                          f'Результат функции: {some_func}\n'
                          f'Путь к файлу: {os.path.abspath(abspath)}')
                return some_func
        return new_path_func
    return log


@path_decor(os.path.abspath('result.txt'))
def path(*args):
    print(args*2)


# Home task 3
# Пример взят из ДЗ "Функции"
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# p–people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
def p_people(some_param):
    number_counter = 0
    sum_input = input('Введите номер документа: ')
    for sum2 in some_param:
        if sum2["number"] != sum_input:
            number_counter += 1
        if number_counter % len(sum2) == 0:
            print('Такого документа нет в списке документов')
        else:
            if sum2["number"] == sum_input:
                print(sum2["name"])


# l–list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def l_list(some_param):
    for documents1 in some_param:
        print('{} {} {}'.format(documents1["type"], '"' + documents1["number"] + '"', '"' + documents1["name"] + '"'))


# s–shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def s_shelf(some_param):
    number_input = input('Введите номер документа: ')
    for doc_num in some_param:
        if number_input in some_param[doc_num]:
            print("Документ находится на полке № {}".format(doc_num))
            return
    print('Такого документа нет на полках с документами')


# a–add – команда, которая добавит новый документ в каталог
# и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def a_add(some_param, some_param_1):
    doc_type = input('Введите тип документа: ')
    doc_num = input('Введите номер документа: ')
    person_name = input('Введите имя человека: ')
    shelf_num = input('Введите номер полки: ')
    documents_add = {"type": doc_type, "number": doc_num, "name": person_name}
    some_param.append(documents_add)
    if shelf_num in some_param_1.keys():
        some_param_1[shelf_num].append(doc_num)
    else:
        some_param_1.setdefault(shelf_num, [doc_num])
    print(f'{some_param} \n{some_param_1}')
    return


# Задача №2. Дополнительная (не обязательная)
# d–delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
def d_delete(some_param, some_param_1):
    doc_num_input = input('Введите номер документа: ')
    for doc_num_1 in some_param_1.values():
        if doc_num_input in doc_num_1:
            doc_num_1.remove(doc_num_input)
            for doc_num_1 in some_param:
                if doc_num_input in doc_num_1["number"]:
                    some_param.remove(doc_num_1)
                    print(f'{documents} \n{directories}')
                    return
    print('Такого документа нет на полках с документами')


# m–move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
def m_move(some_param):
    doc_num_input = input('Введите номер документа: ')
    shelf_num_input = input('На какую полку положить документ: ')
    for shelf_num in some_param.keys():
        if shelf_num_input in shelf_num:
            for doc_num_1 in some_param.values():
                if doc_num_input in doc_num_1:
                    doc_num_1.remove(doc_num_input)
                    some_param[shelf_num_input].append(doc_num_input)
                    print(some_param)
                    return
            print('Такого документа нет на полках с документами')
            return
    print('Такой полки нет!')
    return


# as–add_shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
def add_shelf(some_param):
    new_shelf = input('Введите номер новой полки: ')
    some_param.setdefault(new_shelf, [])
    print(some_param)


@log_decor
def l_list(some):
    return


if __name__ == '__main__':
    logger('Log 1', 'Log 2')
    path('Text 1', 'Text 2')
    l_list(documents)
