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
        print("You are verified! Please follow the instructions in the link that has been opened.")
        time.sleep(2)
        open_link("https://www.canada.ca/en/revenue-agency/services/benefits/apply-for-cerb-with-cra.html")
    else:
        print("Unfortunately, you are not verified for Canada's government funding!")


def verify_country(user_object):
    return True if user_object.get_country() == "Canada" else False


def verify_age(user_object):
    return True if user_object.get_age() >= 15 else False


def verify_income(user_object):
    if user_object.get_income() >= 5000:
        return verify_province()
    else:
        if verify_if_student(user_object):
            print("Because you are a post-secondary student, BC's government is ensuring emergency support. "
                  "A link has been opened for your educational viewing.")
            time.sleep(2)
            open_link("https://news.gov.bc.ca/releases/2020AEST0018-000615")


def verify_province():
    user_province = input("What province do you currently reside in? (EX. BC) ").upper().strip()

    return True if user_province == "BRITISH COLUMBIA" or user_province == "BC" else False


def verify_if_student(user_object):
    return True if user_object.get_student() else False


def open_link(url):
    webbrowser.open_new(url)


def main():
    doctest.testmod()
    verify_for_funding(user.User("Jessica Hong", 23, 0, "Canada", True))


if __name__ == '__main__':
    main()
