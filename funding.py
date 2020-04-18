"""
Functions to verify if a user is qualified for CERB funding.
"""
# Verify country, age, income, student, province
import time
import webbrowser
import user
import doctest


def verify_for_funding(user_object):
    """
    Verify user for Canada's government funding.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object is verified for government funding
    """
    verification = {"Country": verify_country(user_object), "Age": verify_age(user_object),
                    "Income": verify_income(user_object)}

    if all(value for value in verification.values()):
        print("You are verified for funding! "
              "Please follow the instructions in the link that will open in your browser.")
        time.sleep(2)
        open_link("https://www.canada.ca/en/revenue-agency/services/benefits/apply-for-cerb-with-cra.html")


def verify_country(user_object):
    """
    Verify user's country.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object's country is Canada

    :return: A boolean if user_object's country is Canada

    >>> user_object = user.User("Jessica Hong", 23, 35000, "Canada", True)
    >>> verify_country(user_object)
    True

    >>> user_object = user.User("Jessica Hong", 23, 0, "United States", False)
    >>> verify_country(user_object)
    False
    """
    return True if user_object.get_country() == "Canada" else False


def verify_age(user_object):
    """
    Verify user's age.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object's age is 15 or more

    :return: A boolean if user_object's age is 15 or more

    >>> user_object = user.User("Jessica Hong", 15, 35000, "Canada", True)
    >>> verify_age(user_object)
    True

    >>> user_object = user.User("Jessica Hong", 0, 0, "United States", False)
    >>> verify_age(user_object)
    False
    """
    return True if user_object.get_age() >= 15 else False


def verify_income(user_object):
    """
    Verify user's income status.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Correctly verify if user_object's income is 5000 or more

    :return: A boolean if income is more than 5000, otherwise invoke verify_if_student function
    """
    if user_object.get_income() >= 5000:
        return True
    else:
        verify_if_student(user_object)


def verify_province():
    """
    Verify if user's province is British Columbia.

    :precondition: User's input must be a string
    :postcondition: Correctly verify if user's province is British Columbia
    """
    try:
        user_province = input("What province do you currently reside in? (EX. BC) ").upper().strip()
    except ValueError:
        print("Invalid input, try again!")
    else:
        if user_province == "BRITISH COLUMBIA" or user_province == "BC":
            print("Because you are a post-secondary student, BC's government is ensuring emergency support. "
                  "A link has been opened in your browser for your educational viewing.")
            time.sleep(2)
            open_link("https://news.gov.bc.ca/releases/2020AEST0018-000615")
        else:
            print("Sorry, you are not qualified for government funding in British Columbia!")


def verify_if_student(user_object):
    """
    Verify if user is a student.

    :param user_object: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Will successfully invoke verify_province function if user is a student, otherwise print a
    rejection message
    """
    if user_object.get_student():
        verify_province()
    else:
        print("Sorry, you are not qualified for government funding!")


def open_link(url):
    """
    Open the article URL in user's default web browser.

    :param url: A string
    :precondition: url must be a well-formed string
    :postcondition: Successfully open the article URL in user's default web browser
    """
    webbrowser.open_new(url)


def main():
    """
    Test the functions in the module.
    """
    doctest.testmod()


if __name__ == '__main__':
    main()
