from requests import get
from ip2geotools.databases.noncommercial import DbIpCity


def get_ip() -> str:
    """Get the user's IP address.

    :postcondition: correctly returns the IP_address as a string
    :return: the user's ip_address as a string
    """
    ip_address = get('https://api.ipify.org').text
    return ip_address


def print_ip(ip_address: str):
    """Print the user's IP address.

    :param ip_address: a string
    :precondition: ip_address is a well-formed IP address
    :postcondition: the user's IP address has been printed
    """
    print(f"Your IP Address is: {ip_address}")


def get_default_country(ip_address: str) -> str:
    """Get the user's default country.

    :param ip_address: the user's ip_address
    :precondition: ip_address is a well formed IP address
    :postcondition: correctly returns the user's country based on their IP address
    :return: the user's default country code as a string
    """
    response = DbIpCity.get(f'{ip_address}', api_key='free')
    return response.country


def print_default_country(default_country: str):
    """Print the user's default country.

    :param default_country: the country code of the user's current location
    :precondition: default_country is a well formed country code
    :postcondition: the user's default country code has been successfully printed
    """
    print(f"default country is: {default_country}")


def main():
    ip_address = get_ip()
    print_ip(ip_address)
    default_country = get_default_country(ip_address)
    print_default_country(default_country)
