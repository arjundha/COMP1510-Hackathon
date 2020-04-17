"""
Functions that assist in generating a User object.
"""
import doctest
import user
import re


def create_user():
    name = create_name()


def create_name():
    name = input("What is your first and last name? (ex. Chris Thompson): ")
    sentinel = False
    while not sentinel:
        name = input("What is your first and last name? (ex. Chris Thompson): ")
        sentinel = validate_name(name)

    print("Pleasure to meet you, %s." % name)
    return name


def validate_name(name):
    name_regex = re.compile(r'^[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*$')  # First name starts with a capital then any letter
    match_object = name_regex.search(name)

    return True if match_object else False


def main():
    doctest.testmod()
    print("Welcome")
    create_user()


if __name__ == '__main__':
    main()
