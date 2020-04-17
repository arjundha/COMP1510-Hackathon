"""
Class constructor for an application's user
"""
import doctest


class User:

    def __init__(self, name: str, age: int, income: list, country: str, student: bool):
        self.__name = name
        self.__age = age
        self.__income = income
        self.__country = country
        self.__student = student

