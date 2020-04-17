from requests import get
from ip2geotools.databases.noncommercial import DbIpCity


def get_ip():
    """Get the user's IP address.

    :postcondition: correctly returns the IP_address as a string
    :return: the user's ip_address as a string
    """
    ip_address = get('https://api.ipify.org').text
    return ip_address


def print_ip(ip_address):
    """Print the user's IP address.

    :param ip_address: a string
    :precondition: ip_address is a well-formed IP address
    :postcondition: the user's IP address has been printed
    """
    print(f"Your IP Address is: {ip_address}")


def get_default_country(ip_address):
    """Get the user's default country.

    :param ip_address: the user's ip_address
    :precondition: ip_address is a well formed IP address
    :postcondition: correctly returns the user's country based on their IP address
    :return: the user's default country code as a string
    """
    response = DbIpCity.get(f'{ip_address}', api_key='free')
    return response.country


def print_default_country(default_country):
    print(f"default country is: {default_country}")


def main():
    ip_address = get_ip()
    print_ip(ip_address)
    default_country = get_default_country(ip_address)
    print_default_country(default_country)



if __name__ == "__main__":
    main()