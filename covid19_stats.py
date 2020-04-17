import doctest
import requests
import json


def get(api_link):
    # Get response from the api
    response = requests.get(api_link)

    # Check status of response
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        # Return json dictionary
        return json.loads(response.text)


def global_stats():
    return get('https://api.covid19api.com/summary')


def get_country_stats(country):
    # Search list for specified country key
    return next(item for item in get('https://api.covid19api.com/summary')['Countries'] if
                item["Country"].lower() == country.strip().lower())


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
