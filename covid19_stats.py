import doctest
import requests
import json


def get(api_link):
    """
    Get response from api

    :param api_link: a valid api request link
    :preconditon: api_link must be a string
    :postcondition: return the response as a json dictionary
    :return: the response as a json dictionary
    """
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
    """
    Get dictionary from global statistics api

    :postcondition: get the response from the api for global statistics
    :return: the response as a json dictionary
    """
    return get('https://api.covid19api.com/summary')


def get_country_stats(country):
    """
    Search api dictionary for country

    :param country: a country
    :precondition: country must be a string
    :postcondition: will search through the dictionary of countries from api for the country
    :return: the country as a string
    """
    # Search list for specified country key
    return next(item for item in get('https://api.covid19api.com/summary')['Countries'] if
                item["Country"].lower() == country.strip().lower())


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
