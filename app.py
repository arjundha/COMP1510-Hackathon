import requests
import json
import textwrap


def menu():
    print("Welcome")
    return input("""
    1. Global Statistics

    2. Search by Country
    """)


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

    """)


def get(api_link):
    response = requests.get(api_link)
    response.raise_for_status()
    return json.loads(response.text)


def main():
    print()


if __name__ == '__main__':
    main()
