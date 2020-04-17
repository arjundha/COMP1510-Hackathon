# e454fda9cf5b4a5d8e6f8bc3d960c7b5
import json
import textwrap
import webbrowser
import requests


def verify_news_api_response(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()

    try:
        response.raise_for_status()
    # Bad Request. The request was unacceptable, often due to a missing or misconfigured parameter
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        return json.loads(response.text)


def get_country_news(country_code: str):
    country_news_info = verify_news_api_response("https://newsapi.org/v2/top-headlines?country="
                                                 + country_code + "&apiKey=e454fda9cf5b4a5d8e6f8bc3d960c7b5")

    articles_of_country = country_news_info["articles"][0:5]
    display_headline_title(articles_of_country)


def display_headline_title(articles: list):
    print("These are the top 5 articles of your selected country: \n")

    for article in articles:
        print(article["title"])


def get_user_article_choice():
    pass

get_country_news('ca')
