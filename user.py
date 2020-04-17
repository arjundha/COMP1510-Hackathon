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

