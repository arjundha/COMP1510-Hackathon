"""
Class constructor for an application's user
"""
import doctest


class User:

    def __init__(self, name: str, age: int, income: int, country: str, student: bool):
        self.__name = name
        self.__age = age
        self.__income = income
        self.__country = country
        self.__student = student

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_income(self) -> int:
        return self.__income

    def get_country(self) -> str:
        return self.__country

    def get_student(self) -> bool:
        return self.__student

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_age(self, new_age: int):
        self.__age = new_age

    def set_income(self, new_income: int):
        self.__income = new_income

    def set_country(self, new_country: str):
        self.__country = new_country

    def set_student(self, new_student: bool):
        self.__student = new_student


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
