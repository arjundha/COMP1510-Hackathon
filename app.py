import requests
import json
import textwrap
import covid19_stats


def menu():
    """
    Ask user to choose option.

    :precondition: input must be a number that corresponds with an option
    :postcondition: will return the user's choice as an int
    :return: input as an int
    """
    print("Welcome")
    return int(input("""
    1. Global Statistics

    2. Search by Country
    
    3. Quit\n
    """))


def menu_handler(user_input):
    """
    Return function that corresponds you user_input.

    :param user_input: a user entered integer
    :precondition: user_input must be an integer that corresponds with an option
    :postcondition: will return the function that corresponds with desired option
    :raise: TypeError if user_input does not correspond with and option
    :return: a function that corresponds with user_input
    """
    if user_input == 1:
        return global_statistics()
    if user_input == 2:
        return country_search()
    if user_input == 3:
        quit()
    else:
        raise TypeError


def country_search():
    """
    Search country specific statistics.

    :precondition: country input must be a valid country
    :postcondition: will display the information regarding the entered country
    :except: StopIteration if input is not a valid country
    """
    country = input("Please input country\n").strip().lower()

    try:
        country = covid19_stats.get_country_stats(country)

    except StopIteration:
        print("Sorry, Your input is not a valid country")

    else:
        display_statistics(country)


def global_statistics():
    """
    Display the global Covid-19 statistics.

    :postcondition: will display all statistics for the world
    """
    global_dict = covid19_stats.global_stats()
    statistics = global_dict['Global']

    display_statistics(statistics)


def display_statistics(statistics):
    """
    Display statistics from given dictionary.

    :param statistics: covid19 dictionary
    :preconditions: statistics must be a well formatted covid19 API dictionary
    :postconditions: Will display details statistics regarding the specified dictionary
    """
    print(f"""
        New Confirmed Cases:    {statistics["NewConfirmed"]}

        Total Confirmed:        {statistics["TotalConfirmed"]}

        New Deaths:             {statistics["NewDeaths"]}

        Total Deaths:           {statistics["TotalDeaths"]}

        Newly Recovered:        {statistics["NewRecovered"]}

        Total Recovered:        {statistics["TotalRecovered"]}

        \n""")

    input("Hit any button to continue")


def main():
    while True:
        x = menu()
        try:
            menu_handler(x)
        except TypeError:
            print("Your input was invalid or not an option, try again")


if __name__ == '__main__':
    main()
