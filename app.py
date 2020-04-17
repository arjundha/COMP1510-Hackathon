import requests
import json
import textwrap


def get(api_link):
    response = requests.get(api_link)
    response.raise_for_status()
    return json.loads(response.text)


def main():
    print()


if __name__ == '__main__':
    main()
