"""
Functions to verify if a user is qualified for CERB funding.
"""


# Verify country, age, income, student, province
def verify_for_funding(user):
    verification = {"Country": verify_country(user), "Age": verify_age(user), "Income": verify_income(user)}

    if all(value for value in verification.values()):
        print("You are verified!")
