# e454fda9cf5b4a5d8e6f8bc3d960c7b5
import json

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
