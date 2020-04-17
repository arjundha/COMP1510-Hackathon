# API KEY: e454fda9cf5b4a5d8e6f8bc3d960c7b5
import json
import textwrap
import webbrowser
import requests
import default_country


def verify_news_api_response(url: str) -> dict:
    response = requests.get(url)

    try:
        response.raise_for_status()
    # Bad Request. The request was unacceptable, often due to a missing or misconfigured parameter
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        return json.loads(response.text)


def get_default_country_top_headlines():
    """
    Get the articles of a specified country.

    :precondition: country_code must be a well-formed string
    :postcondition: Successfully get the news articles of the user's current country location.
    """
    country_code = default_country.get_default_country(default_country.get_ip())

    country_news_info = verify_news_api_response("https://newsapi.org/v2/top-headlines?country="
                                                 + country_code + "&apiKey=e454fda9cf5b4a5d8e6f8bc3d960c7b5")

    articles_of_country = country_news_info["articles"][0:5]
    display_headline_title(articles_of_country)


def display_headline_title(articles: list):
    """
    Display the headline title of the top 5 articles.

    :param articles: A list
    :precondition: articles must be a well-formed list
    :postcondition: Successfully display the headline of the top 5 articles
    """
    print("These are the top 5 articles of your selected country: \n")

    for num, article in enumerate(articles, 1):
        print(num, article["title"])

    view_choice = get_user_view_choice()

    if view_choice:
        view_article_in_browser(articles[view_choice - 1]['url'])


def get_user_view_choice():
    """
    Get user's choice if they want to view an article.

    :precondition: User's input must be an integer
    :postcondition: Successfully invoke the get_user_article_choice function

    :return: The value returned from get_user_article_choice as an integer or None
    """
    try:
        view = int(input("\nDo you want to view an article? 1 - Yes, 2 - No: "))
    except ValueError as e:
        print(e)
    else:
        if view == 1:
            return get_user_article_choice()
        else:
            return None


def get_user_article_choice():
    """
    Get user's choice on which article they want to view.

    :precondition: User's input must be an integer
    :postcondition: Successfully return user's input as an integer

    :return: User's choice of article number as an integer
    """
    try:
        article_num = int(input("Which article would you like to view?: "))
    except ValueError as e:
        print(e)
    else:
        if 1 <= article_num <= 5:
            return article_num
        else:
            print("That's not a valid article number, try again!")
            get_user_article_choice()


def view_article_in_browser(url):
    """
    Open the article URL in user's default web browser.

    :param url: A string
    :precondition: url must be a well-formed string
    :postcondition: Successfully open the article URL in user's default web browser
    """
    webbrowser.open_new(url)
