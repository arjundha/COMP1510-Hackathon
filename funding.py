"""
Functions to verify if a user is qualified for CERB funding.
"""


# Verify country, age, income, student, province
def verify_for_funding(user):
    verification = {"Country": verify_country(user), "Age": verify_age(user), "Income": verify_income(user)}

    if all(value for value in verification.values()):
        print("You are verified!")


def verify_country(user):
    return True if user.get_country() == "Canada" else False


def verify_age(user):
    return True if user.get_age() >= 15 else False


def verify_income(user):
    if user.get_income() >= 5000:
        return verify_province()
    else:
        if verify_if_student(user):
            open_link("")


def verify_province():
    user_province = input("What province do you currently reside in? (EX. BC) ").upper().strip()

    print(user_province)
    return True if user_province == "BRITISH COLUMBIA" or user_province == "BC" else False


def verify_if_student(user):
    return True if user.get_student() else False


def open_link(url):
    pass
