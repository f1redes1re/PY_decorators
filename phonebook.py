

class Contact:

    def __init__(self, first_name, last_name, phone_num, favorite=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.favorite = favorite
        if favorite is False:
            self.favorite = 'Нет'
        self.kwargs = kwargs

    def compulsory(self):
        return f"Имя: {self.first_name}\n" \
               f"Фамилия: {self.last_name}\n" \
               f"Телефон: {self.phone_num}\n" \
               f"В избранных: {self.favorite}\n"

    def non_compulsory(self):
        kwarg = ''
        for key, value in self.kwargs.items():
            kwarg += f"               {key}: {value}"'\n'
        return kwarg

    def __str__(self):
        return f"{self.compulsory()}" \
               f"Дополнительная информация:\n" \
               f"{self.non_compulsory()}"

    def __repr__(self):
        return f"{self.compulsory()}" \
               f"Дополнительная информация:\n" \
               f"{self.non_compulsory()}"


class PhoneBook:

    def __init__(self, book_name):
        self.book_name = book_name
        self.book = []

    def show_contacts(self):
        for c in self.book:
            print(c)
        return

    def add_contact(self, *args):
        for new_con in args:
            self.book.append(new_con)

    def del_contact(self):
        phone_input = input('Введите номер телефона: ')
        for cont in self.book:
            if phone_input in str(cont):
                self.book.remove(cont)
                return
        print('Такого номера нет в списке контактов')

    def search_favorite(self):
        fav_list = []
        for cont in self.book:
            if 'В избранных: Да' in str(cont):
                fav_list.append(cont)
        return fav_list

    def search_contact(self):
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        for cont in self.book:
            if first_name and last_name in str(cont):
                return cont

    def __str__(self):
        return f"{self.book_name}, Количество контактов: {len(self.book)}"


if __name__ == '__main__':
    john = Contact('John', 'Smith', '89753442053', telegram='@johny', email='johny@smith.com')
    alex = Contact('Alexander', 'Glebov', '+7787878787', 'Да', telegram='@ag', email='ag@mail.ru')
    jason = Contact('Jason', 'Statham', '467843114', telegram='JS')
    daria = Contact('Дарья', 'Пайчармовна', '+79678112314', 'Нет', email='dariapy@gmail.com')
    book = PhoneBook('Телефонная книга')
    book.add_contact(john, jason, alex, daria)

    while True:
        print('Перед вами меню приложения "Телефонная книга".\n'
              'Выберите нужную команду:\n'
              '"1" - список контактов\n'
              '"2" - добавить контакт\n'
              '"3" - удалить контакт\n'
              '"4" - избранные контакты\n'
              '"5" - найти контакт\n'
              )
        command = input('Введите команду: ')
        if command == "1":
            book.show_contacts()
            break
        elif command == "2":
            f_name = input("Введите имя: ")
            l_name = input("Введите фамилию: ")
            ph = input("Введите телефон: ")
            fav = input("Избранный (да/нет): ")

            kwarg_dict = {}
            while True:
                key = input("Введите дополнительный параметр (для остановки введите 'stop': ")
                if key == 'stop':
                    break
                else:
                    value = input("Введите значение параметра: ")
                    kwarg_dict.setdefault(key, value)

            new_contact = Contact(f_name, l_name, ph, fav, **kwarg_dict)
            book.add_contact(new_contact)
            book.show_contacts()
            break
        elif command == "3":
            book.del_contact()
            print(book.show_contacts())
            break
        elif command == "4":
            print(book.search_favorite())
            break
        elif command == "5":
            print(book.search_contact())
            break
        else:
            print('Такая команда не предусмотрена!')
