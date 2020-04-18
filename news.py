# API KEY: e454fda9cf5b4a5d8e6f8bc3d960c7b5
import doctest
import json
import textwrap
import webbrowser
import requests
import default_country


def print_messages(original_func):  # DEMONSTRATES DECORATORS
    """
    Print loading messages to display for user.

    :param original_func: A function
    :precondition: original_func must be a well-formed function
    :postcondition: Successfully invoke the wrapper function

    :return: wrapper_printer
    """
    def wrapper_printer(*args, **kwargs):
        print("\nLoading...")
        original_func(*args, **kwargs)
        print("Load successful!")

    return wrapper_printer


def verify_news_api_response(url: str) -> dict:
    """
    Send an HTTP request for the passed API URL.

    :param url: A string
    :precondition: url must be a well-formed string
    :postcondition: Successfully get the JSON encoded data and parses it into a Python object

    :return: Parsed JSON object as a dictionary
    """
    response = requests.get(url)

    try:
        response.raise_for_status()
    # Bad Request. The request was unacceptable, often due to a missing or misconfigured parameter
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        return json.loads(response.text)


def display_news_articles_menu():
    """
    Display news article menu to get user input.

    :precondition: User input must be an integer between 1 and 3
    :postcondition: Successfully handle user's input using menu_handler function
    """
    while True:
        try:
            # Get user input after displaying menu
            user_input = int(input(
                "1. Top news about your current location\n"
                "2. Global news about COVID-19\n"
                "3. Search news articles by keyword\n"))
        except ValueError:
            print("Invalid input! Try again.")
            continue
        else:
            if 1 <= user_input <= 3:
                menu_handler(user_input)  # Will direct user to their selected menu option
            else:
                print("Invalid input! Try again.")


def menu_handler(user_input: int):
    """
    Direct user to their selected menu option.

    :param user_input: An integer
    :precondition: user_input must be an integer between 1 and 3
    :postcondition: Successfully invoke user's selected menu option function
    """
    if user_input == 1:
        get_default_country_top_headlines()
    elif user_input == 2:
        covid_news()
    elif user_input == 3:
        get_articles_by_keyword()


def get_default_country_top_headlines():
    """
    Get the top 5 articles of user's current country location.

    :postcondition: Successfully get the news articles of the user's current country location.
    """
    country_code = default_country.get_default_country(default_country.get_ip())  # Get the user's default country code

    country_news_info = verify_news_api_response("https://newsapi.org/v2/top-headlines?country="
                                                 + country_code + "&apiKey=e454fda9cf5b4a5d8e6f8bc3d960c7b5")

    articles_of_country = country_news_info["articles"][0:5]  # Get the top 5 articles

    print("These are the top 5 news articles of your current country location: \n")
    display_headline_title(articles_of_country)


def covid_news():
    """
    Get the top 5 articles on COVID-19.

    :postcondition: Successfully get the news articles on COVID-19
    """
    covid_news_info = verify_news_api_response("https://newsapi.org/v2/everything?q=covid-19"
                                               "&sortBy=popularity&apiKey=e454fda9cf5b4a5d8e6f8bc3d960c7b5")

    top_covid_news_articles = covid_news_info['articles'][0:5]  # Get the top 5 COVID-19 news articles

    print("These are the top 5 global news articles for COVID-19: \n")
    display_headline_title(top_covid_news_articles)


def get_user_keyword() -> str:
    """
    Get user's keyword choice.

    :precondition: User's inputted keyword must be a string
    :postcondition: Successfully return keyword as a string

    :return: keyword as a string
    """
    # Loop until there is valid input
    while True:
        try:
            keyword = input("What articles would you like to search? ")  # Get the user's keyword choice
            # Will raise ValueError if keyword is empty
            if keyword == "":
                raise ValueError
        except ValueError:
            print("Invalid input, try again!")
            continue
        else:
            keyword = keyword.replace(' ', '+')  # Replaces spaces with '+' to align with News API's search query format
            # Will stop while loop
            return keyword


def get_articles_by_keyword():
    """
    Get news articles based on a keyword.

    :postcondition: Successfully invoke the display_headline_title function
    """
    keyword = get_user_keyword()

    keyword_news_info = verify_news_api_response("https://newsapi.org/v2/"
                                                 "everything?q=" + keyword + "&sortBy=popularity&apiKey="
                                                                             "e454fda9cf5b4a5d8e6f8bc3d960c7b5")

    # Get the top 5 articles using the user's entered keyword
    keyword_news_articles = keyword_news_info['articles'][0:5]

    print("These are the top 5 articles for " + keyword + ": \n")
    display_headline_title(keyword_news_articles)


def display_headline_title(articles: list):
    """
    Display the headline title of the top 5 articles.

    :param articles: A list
    :precondition: articles must be a well-formed list
    :postcondition: Successfully display the headline of the top 5 articles
    """
    for num, article in enumerate(articles, 1):  # Demonstrates ENUMERATE
        print(num, article["title"])  # Print out the headings in an ordered list

    view_choice = get_user_article_choice()

    if view_choice:  # If view choice is not empty
        view_article_in_browser(articles[view_choice - 1]['url'])


def get_user_article_choice() -> int:
    """
    Get user's choice on which article they want to view.

    :precondition: User's input must be an integer
    :postcondition: Successfully return user's input as an integer

    :return: User's choice of article number as an integer
    """
    # Loop until there is valid input
    while True:
        try:
            article_num = int(input("\nWhich article would you like to view?: "))
        except ValueError:
            print("Invalid input! Try again.")
            # Will continue the while loop
            continue
        else:
            if 0 < article_num <= 5:
                # Stop while loop iteration
                return article_num
            else:
                print("That's not a valid article number, try again!")


@print_messages
def view_article_in_browser(url):
    """
    Open the article URL in user's default web browser.

    :param url: A string
    :precondition: url must be a well-formed string
    :postcondition: Successfully open the article URL in user's default web browser
    """
    webbrowser.open_new(url)  # User's default browser will be launched
    input("Hit the enter key to continue")


def main():
    """
    Test the functions in this module.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
