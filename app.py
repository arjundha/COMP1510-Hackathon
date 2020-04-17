import requests
import json
import textwrap


def menu():
    print("Welcome")
    return int(input("""
    1. Global Statistics

    2. Search by Country\n
    """))


def menu_handler(user_input):
    if user_input == 1:
        return global_statistics()
    if user_input == 2:
        return country_search()


def country_search():
    country = input("Please input country\n")

    all_countries = get('https://api.covid19api.com/summary')

    countries_dictionary = all_countries["Countries"]

    country = next(item for item in countries_dictionary if item["Slug"] == country)
    print(f"""
        New Confirmed Cases:    {country["NewConfirmed"]}

        Total Confirmed:        {country["TotalConfirmed"]}

        New Deaths:             {country["NewDeaths"]}

        Total Deaths:           {country["TotalDeaths"]}

        Newly Recovered:        {country["NewRecovered"]}

        Total Recovered:        {country["TotalRecovered"]}

        \n""")


def global_statistics():
    global_dict = get('https://api.covid19api.com/summary')
    statistics = global_dict['Global']
    print(f"""
    New Confirmed Cases:    {statistics["NewConfirmed"]}

    Total Confirmed:        {statistics["TotalConfirmed"]}

    New Deaths:             {statistics["NewDeaths"]}

    Total Deaths:           {statistics["TotalDeaths"]}

    Newly Recovered:        {statistics["NewRecovered"]}

    Total Recovered:        {statistics["TotalRecovered"]}

    \n""")


def get(api_link):
    response = requests.get(api_link)
    response.raise_for_status()
    return json.loads(response.text)


def main():
    x = menu()

    menu_handler(x)


if __name__ == '__main__':
    main()
