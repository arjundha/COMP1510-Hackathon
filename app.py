import market_data
import covid19_stats
import news
import user_generation
import funding
import dow_plot
import doctest


def option_menu() -> int:
    """
    Ask user to choose option.

    :precondition: input must be a number that corresponds with an option
    :postcondition: will return the user's choice as an int

    :return: input as an int
    """
    while True:
        print("Please select an option, or quit.")
        try:
            return int(input("""
        1. Global Statistics

        2. Information about my Country

        3. Search by Country

        4. News Articles
        
        5. Search Stocks

        6. Am I Eligible for the Canadian Emergency Response Benefit Funding?
        
        7. Show Effect of COVID-19 on DOW Jones Index
        
        8. Quit

\n"""))

        except ValueError:
            print("Please input a number that corresponds to an option on the menu.")


def menu_handler(user_input: int, user: object or str) -> object:
    """
    Return function that corresponds you user_input.

    :param user_input: a user entered integer
    :param user: a well formed user object
    :precondition: user_input must be an integer that corresponds with an option
    :precondition: user must be an object created in user_generation
    :postcondition: will return the function that corresponds with desired option
    :raise: TypeError if user_input does not correspond with and option

    :return: a function that corresponds with user_input
    """
    if user_input == 1:
        return global_statistics()

    if user_input == 2:
        return my_country(user)

    if user_input == 3:
        return country_search()

    if user_input == 4:
        return get_news()

    if user_input == 5:
        search_stocks()

    if user_input == 6:
        return verify_canadian_funding(user)

    if user_input == 7:
        show_dow_chart()

    if user_input == 8:
        print("Have a nice day, and remember to wash your hands!")
        quit()

    else:
        raise TypeError


def search_stocks():
    """
    Ask user for stock

    :postcondition: will run ask_for_stock() and ask user for a stock and then display the information
    """
    market_data.ask_for_stock()


def show_dow_chart():
    """
    Display DOW JONES chart.

    :postcondition: will run the main function in dow_plot file
    """
    dow_plot.main()


def verify_canadian_funding(user: object):
    """
    Verify if user is eligible for Canadian Emergency Response Benefit funding.

    :param user: User object
    :precondition: user_object must be a well-formed User object
    :postcondition: Successfully verify if user is eligible for Canadian Emergency Response Benefit funding
    """
    funding.verify_for_funding(user)


def my_country(user: object or str):
    """
    Display statistics from user country.

    :param user: a well formed user object
    :precondition: user must be an object created in user_generation
    :postcondition: will display all information regarding the user's inputted location
    """
    print(user.get_country())

    # Get Country stats by passing it to get_country_stats
    country_stats = covid19_stats.get_country_stats(user.get_country())
    display_statistics(country_stats)


def get_news():
    """
    Display news article interface

    :postcondition: will run the news article function get_default_country_top_headlines() from news
    """
    news.display_news_articles_menu()


def country_search():
    """
    Search country specific statistics.

    :precondition: country input must be a valid country
    :postcondition: will display the information regarding the entered country
    :except: StopIteration if input is not a valid country
    """
    # Ask user for input
    country = input("Please input country\n").strip()

    # Check if input meets conditions
    try:
        country_statistics = covid19_stats.get_country_stats(country)

    except StopIteration:
        print("Sorry, Your input is not a valid country\n")
        print("Try typing the full name of the country. Ex: United States -> United States of America")

    else:
        # Display information
        print(country.capitalize())
        display_statistics(country_statistics)


def global_statistics():
    """
    Display the global COVID-19 statistics.

    :postcondition: will display all statistics for the world
    """
    # Get the dictionary from from the api
    global_dict = covid19_stats.global_stats()

    # Specify the key
    statistics = global_dict['Global']

    # Display the information
    display_statistics(statistics)


def display_statistics(statistics):
    """
    Display statistics from given dictionary.

    :param statistics: covid19 dictionary
    :preconditions: statistics must be a well formatted covid19 API dictionary
    :postconditions: Will display details statistics regarding the specified dictionary
    """
    print(f"""
        Total Active Cases:     {statistics["TotalConfirmed"] - statistics["TotalDeaths"] - statistics["TotalRecovered"]}

        New Confirmed Cases:    {statistics["NewConfirmed"]}

        Total Confirmed:        {statistics["TotalConfirmed"]}

        New Deaths:             {statistics["NewDeaths"]}

        Total Deaths:           {statistics["TotalDeaths"]}

        Newly Recovered:        {statistics["NewRecovered"]}

        Total Recovered:        {statistics["TotalRecovered"]}

        \n""")

    input("Hit enter to continue")


def main():
    """
    Run program.
    """
    doctest.testmod()
    # Welcome message
    print("Welcome to the COVID-19 App! Before we get started, lets generate your user profile.")

    # Create user
    user = user_generation.create_user()

    # Check if user information is correct
    user_generation.check_if_user_information_is_correct(user)

    while True:
        user_choice = option_menu()

        try:
            menu_handler(user_choice, user)

        except TypeError:
            print("Your input was invalid or not an option, try again")


if __name__ == '__main__':
    main()
