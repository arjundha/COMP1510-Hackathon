"""
Functions to verify if a user is qualified for CERB funding.
"""


# Verify country, age, income, student, province
import webbrowser


def verify_for_funding(user):
    verification = {"Country": verify_country(user), "Age": verify_age(user), "Income": verify_income(user)}

    if all(value for value in verification.values()):
        print("You are verified! Please follow the instructions in the link that has been opened.")
        open_link("https://www.canada.ca/en/revenue-agency/services/benefits/apply-for-cerb-with-cra.html")


def verify_country(user):
    return True if user.get_country() == "Canada" else False


def verify_age(user):
    return True if user.get_age() >= 15 else False


def verify_income(user):
    if user.get_income() >= 5000:
        return verify_province()
    else:
        if verify_if_student(user):
            print("Because you are a post-secondary student, BC's government is ensuring emergency support. "
                  "A link has been opened for your educational viewing.")
            open_link("https://news.gov.bc.ca/releases/2020AEST0018-000615")


def verify_province():
    user_province = input("What province do you currently reside in? (EX. BC) ").upper().strip()

    print(user_province)
    return True if user_province == "BRITISH COLUMBIA" or user_province == "BC" else False


def verify_if_student(user):
    return True if user.get_student() else False


def open_link(url):
    webbrowser.open_new(url)
