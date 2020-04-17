"""
Functions that assist in generating a User object.
"""
import doctest
import user
import re


def create_user() -> object:
    """
    Assemble variables and create a User object.

    :precondition: User will enter valid data when prompted
    :postcondition: Will create a User object
    :return: A well-formed User object
    """
    name = enter_name()  # Get user's name as a string
    age = enter_age()  # Get user's age a positive integer
    income = enter_income()  # Get user's annual income as a positive integer
    country = enter_country()  # Determine the country of residence for a user
    student_status = is_student()  # Determine if the user is a post-secondary student

    return user.User(name, age, income, country, student_status)


def enter_name() -> str:
    """
    Determine a user's name.

    :precondition: Enter your first and last name
    :postcondition: Will prepare the name for object assembly
    :return: User's name as a string
    """
    sentinel = False  # Sentinel value for checking if a name is valid or not

    while not sentinel:
        name = input("What is your first and last name? (ex. Chris Thompson): ").strip().title()
        sentinel = validate_name(name)  # Uses a ReGex check to determine if the name is valid, if it is, breaks loop

    print("Pleasure to meet you, %s." % name)  # Greet the user by name
    return name


def validate_name(name:str ) -> bool:
    """
    Determine whether a user's name is valid/formed correctly.

    :param name: Name
    :return:
    """
    name_regex = re.compile(r'^[A-Z][a-zA-Z\-]* [A-Z][a-zA-Z\-]*$')  # First name starts with a capital then any letter
    match_object = name_regex.search(name)

    return True if match_object else False


def enter_age() -> int:
    while True:
        try:
            age = int(input("What is your current age?: "))

            if age < 0:
                raise ValueError

        except ValueError:
            print("Please enter your age as a positive integer.")

        else:
            return age


def enter_income() -> int:
    while True:
        try:
            income = int(input("What is your current annual income? (Enter your income as a positive integer): "))

            if income < 0:
                raise ValueError

        except ValueError:
            print("Please enter your income as a positive integer.")

        else:
            return income


def enter_country() -> str:
    while True:
        try:
            country = input("What is your country of residence?: ")
            if country.strip() == "":
                raise ValueError

        except ValueError:
            print("A country cannot be blank, please try again.")

        else:
            return country.strip().title()


def numbered_list(user_list: list):
    for i, thing in enumerate(user_list):
        print("%d: %s" % (i + 1, thing))


def is_student() -> bool:
    print("Are you a current post-secondary student?")
    numbered_list(["Yes", "No"])

    while True:
        user_input = input()
        if user_input == "1":
            return True

        elif user_input == "2":
            return False

        else:
            print("Please enter 1 or 2.")


def check_if_user_information_is_correct(user_object: object):
    print("\nIs this information correct?\n%s\n" % user_object)
    numbered_list(["Yes", "No"])

    while True:
        user_input = input()
        if user_input == "1":
            print("Great!")
            break

        elif user_input == "2":
            edit_user(user_object)

        else:
            print("Please enter 1 or 2.")


def edit_user(new_user: object):
    while True:
        print("\nHere are your options to edit.")
        numbered_list(["Name", "Age", "Income", "Country", "Student Status"])
        user_input = input("\nWhat would you like to change? (b to go back): ")

        if user_input in ["1", "2", "3", "4", "5"]:
            edit_user_info(user_input, new_user)
            print("\nUPDATED:\n%s" % new_user)

        elif user_input == "b":
            break


def edit_user_info(user_input: str, new_user):
    if user_input == "1":
        name = enter_name()
        new_user.set_name(name)

    elif user_input == "2":
        age = enter_age()
        new_user.set_age(age)

    elif user_input == "3":
        income = enter_income()
        new_user.set_income(income)

    elif user_input == "4":
        country = enter_country()
        new_user.set_country(country)

    elif user_input == "5":
        student_status = is_student()
        new_user.set_student(student_status)


def main():
    doctest.testmod()
    print("Welcome!")
    new_user = create_user()
    check_if_user_information_is_correct(new_user)
    print("Nice")


if __name__ == '__main__':
    main()
