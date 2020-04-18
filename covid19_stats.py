import doctest
import requests
import json
import doctest


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

    >>> get_country_stats('canada')
    {'Country': 'Canada', 'CountryCode': 'CA', 'Slug': 'canada', 'NewConfirmed': 2005, 'TotalConfirmed': 32814, 'NewDeaths': 97, 'TotalDeaths': 1355, 'NewRecovered': 847, 'TotalRecovered': 10545, 'Date': '2020-04-18T02:46:42Z'}
    >>> get_country_stats('United States of America')
    {'Country': 'United States of America', 'CountryCode': 'US', 'Slug': 'united-states', 'NewConfirmed': 31855, 'TotalConfirmed': 699148, 'NewDeaths': 3853, 'TotalDeaths': 36758, 'NewRecovered': 3842, 'TotalRecovered': 58545, 'Date': '2020-04-18T02:46:42Z'}
    """
    # Search list for specified country key
    return next(item for item in get('https://api.covid19api.com/summary')['Countries'] if
                item["Country"].lower() == country.strip().lower())


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
