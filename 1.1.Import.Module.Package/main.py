from application import salary
from application.db import people
import datetime


def salary_1():
    print(salary.calculate_salary())
    a = datetime.datetime.today()
    print(f'Дата и время: {a}\n')


def people_1():
    print(people.get_employees())
    a = datetime.datetime.today()
    print(f'Дата и время: {a}\n')


def main():
    while True:
        command = input("Выберите нужную команду: ")
        if command == 's':
            return salary_1()
        elif command == 'p':
            return people_1()
        elif command == 'q':
            print('Выход из программы')
            break


if __name__ == '__main__':
    main()
