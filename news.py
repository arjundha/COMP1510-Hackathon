# e454fda9cf5b4a5d8e6f8bc3d960c7b5
import requests


def verify_news_api_response(url):
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        print("Success!")
    # Bad Request. The request was unacceptable, often due to a missing or misconfigured parameter
    elif response.status_code == 400:
        print("Not found")


def get_country_news(country_code):
    verify_news_api_response("https://newsapi.org/v2/top-headlines?country="
                             + country_code + "&apiKey=e454fda9cf5b4a5d8e6f8bc3d960c7b5")
