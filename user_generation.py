"""
Functions that assist in generating a User object.
"""
import doctest
import user
import re
import covid19_stats


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
        name = input("What is your first and last name? (ex. Chris Thompson): ").strip().title()  # title case & strip
        sentinel = validate_name(name)  # Uses a ReGex check to determine if the name is valid, if it is, breaks loop

    print("Pleasure to meet you, %s." % name)  # Greet the user by name
    return name


def validate_name(name: str) -> bool:
    """
    Determine whether a user's name is valid/formed correctly.

    :param name: Name of a user being checked for accurate formation
    :precondtion: The name parameter is a string
    :postcondition: Will attempt to match the name against the ReGex
    :return: A boolean True if it is a matched name, False if it is not
    """
    # REGEX EXAMPLE IS HERE
    name_regex = re.compile(r'^[A-Z][a-zA-Z\-]* [A-Z][a-zA-Z\-]*$')  # ReGex for checking name formation
    match_object = name_regex.search(name)  # Check if the name matches the ReGex (True if it does)

    return True if match_object else False


def enter_age() -> int:
    """
    Determine the age of a user.

    :precondition: User enters a positive integer when prompted.
    :postcondition: Will determine the age of a user.
    :raise ValueError when a user enters age less than or equal to 0
    :return: User age as an int
    """
    while True:
        try:
            age = int(input("What is your current age?: "))  # Ask the user for their age

            if age <= 0:
                raise ValueError  # Raise a value error if the age is less than or equal to 0

        except ValueError:  # Catch a ValueError
            print("Please enter your age as a positive integer.")  # Prints a helpful message upon a ValueError

        else:
            return age


def enter_income() -> int:
    """
    Determine the annual income of a user.

    :precondition: User enters a positive integer when prompted.
    :postcondition: Will determine the income of a user.
    :raise ValueError when a user enters an income less than 0
    :return: Annual income as an int
    """
    while True:
        try:
            # Prompt the user to enter their income and cast it as an integer
            income = int(input("What is your current annual income? (Enter your income as a positive integer): "))

            if income < 0:  # If the user enters a negative income, raise a ValueError
                raise ValueError

        except ValueError:  # Catch the ValueError and print a helpful message
            print("Please enter your income as a positive integer.")

        else:
            return income


def enter_country() -> str:
    """
    Determine what country a user is residing in.

    :precondition: User enters a string representing a country when prompted
    :postcondition: Will return the country as a string to be used in object construction
    :raise ValueError when a user enters an empty string
    :return: a string representing the country where a user lives
    """
    while True:
        try:
            # Prompt user to enter their country
            country = input("What is your country of residence?: ")
            if country.strip() == "":  # Check to see if the country is an empty string
                raise ValueError  # Raise an error if it empty

        except ValueError:  # Catch the ValueError and print a helpful message
            print("A country cannot be blank, please try again.")

        else:
            try:
                covid19_stats.get_country_stats(country)  # Check to see if a country exists in the covid19_stats API

            except StopIteration:  # Catch the StopIteration error and print helpful messages
                print("Im sorry we dont recognize this country.")
                print("Try typing the full name of the country. Ex: United States -> United States of America")

            else:
                return country.strip().title()


def is_student() -> bool:
    """
    Determine whether a user is a current post-secondary student.

    :precondition: User enters 1 or 2 when prompted
    :postcondition: Will allow users the chance to declare their student status
    :return: a Boolean representing whether a user is a student or not (True if they are)
    """
    #  Prompt users to choose options 1 or 2 from an enumerated list (Yes or No)
    #  This is in regards to whether they are a current post-secondary student or not

    print("Are you a current post-secondary student?")
    numbered_list(["Yes", "No"])

    while True:
        user_input = input().strip()
        
        if user_input == "1":
            return True

        elif user_input == "2":  # If 2 (No) return False
            return False

        else:
            print("Please enter 1 or 2.")  # If the user didn't enter a valid option, keep them in the while-loop


def check_if_user_information_is_correct(user_object: object):
    print("\nIs this information correct?\n%s\n" % user_object)
    numbered_list(["Yes", "No"])

    sentinel = False
    while not sentinel:
        user_input = input().strip()
        if user_input == "1":
            print("Great!")
            sentinel = True

        elif user_input == "2":
            edit_user(user_object)
            sentinel = True

        else:
            print("Please enter 1 or 2.")


def edit_user(new_user: object):
    sentinel = False
    while not sentinel:
        print("\nHere are your options to edit.")
        numbered_list(["Name", "Age", "Income", "Country", "Student Status"])
        user_input = input("\nWhat would you like to change? (b to go back): ").strip()

        if user_input in {"1", "2", "3", "4", "5"}:  # DEMONSTRATING A SET
            edit_user_info(user_input, new_user)
            print("\nUPDATED:\n%s" % new_user)

        elif user_input == "b":
            sentinel = True


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


def numbered_list(user_list: list):
    """
    Print an enumerated list of elements.

    This helper function was created through decomposition to reduce the amount of repetitive code being used. Many
    functions in this module utilize this function.

    :param user_list: A list containing elements that will be printed in as a numbered list
    :precondition: Parameter is a list
    :postcondition: Will print the list as a numbered list
    """
    for i, thing in enumerate(user_list):  # For each thing in the list, print the list with an increasing number
        print("%d: %s" % (i + 1, thing))


def main():
    """
    Test the functions in the module.
    """
    doctest.testmod()
    print("Welcome!")
    new_user = create_user()
    check_if_user_information_is_correct(new_user)
    print("Nice")


if __name__ == '__main__':
    main()
