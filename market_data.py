"""
Handles retrieval of market data
"""
import yfinance as yf
import textwrap
import app


def ask_for_stock() -> object:
    """
    Ask user for a stock name.

    :precondition: user_input must be a valid abbreviated stock name
    :postcondition: will return user_input as a parameter of check_with_user to check if user_input meets conditions
    :raise ValueError if the user enters an empty string

    :return: user_input as a string and as a parameter of check_with_user
    """
    while True:
        try:
            user_input = input("Please input the stock abbreviated name.\n Example: Microsoft Corp. -> MSFT\n").strip()

            # Check if the string is empty, if it is raise an error and catch it after
            if user_input == "":
                raise ValueError

        except ValueError:
            print("A stock name cannot be blank. Please try again.")

        else:
            return check_with_user(user_input)


def check_with_user(stock: str) -> object:
    """
    Check if a stock name is valid.

    :param stock: abbreviated stock name
    :precondition: stock must be a string
    :precondition: user_input must be a number that corresponds with the options given

    :return: a function that corresponds with user_input
    """
    while True:
        try:
            # Declare ticker
            ticker = yf.Ticker(stock)

        except (ImportError, KeyError, IndexError):
            # Except error and inform user
            print("We can't find the stock entered..")
            print("Please input the stock abbreviated name.\n Example: Microsoft Corp. -> MSFT\n")

        else:
            try:
                # Clarify with user
                print("Is this the desired Company?")
                print(ticker.info['longName'])

            except (IndexError, KeyError, ImportError):
                # Sometimes api data can be broken for certain stocks
                print("There seems to be an issue fetching the information for the stock entered")
                print("Please try a different stock, input the stock abbreviated name.\n")
                ask_for_stock()

            else:
                user_input = input("1. Yes\n2. No\n")

                if user_input == '1':
                    # Display info
                    return display_info(ticker.info)

                elif user_input == '2':
                    # Repeat if user is not satisfied
                    # Make sure you enter the abbreviated stock name correctly

                    return ask_for_stock()


def display_info(stock_ticker: dict) -> object:
    """
    Display stock information.

    :param stock_ticker: a yFinance stock dictionary
    :precondition: stock_ticker must be a well formatted yFinance dictionary
    :precondition: user_input must be a number that corresponds with the options given
    :postcondition: will neatly print all information regarding the stock and return nothing or ask_user()

    :return: None or ask_user depending on user_input
    """
    # Initialize the summary for text wrap
    summary = stock_ticker['longBusinessSummary']

    # Create the wrapper and word list to display later
    wrapper = textwrap.TextWrapper(width=100)
    word_list = wrapper.wrap(text=summary)

    # Check if dividendYield has a value
    try:
        dividend_yield = float(stock_ticker['dividendYield']) * 100

    except TypeError:
        # When some markets are closed they dont have a dividend yield
        dividend_yield = "-"

    else:
        dividend_yield = str(dividend_yield) + "%"

    # Print information regarding stock_ticker
    print(f"""
{stock_ticker['shortName']}    {stock_ticker['currency']}$         
_______________________________________________________

Daily High:         {stock_ticker['dayHigh']}

Ask:                {stock_ticker['ask']}

Daily Low:          {stock_ticker['dayLow']}

Open:               {stock_ticker['open']}

Dividend Yield:     {dividend_yield}

NOTE: IF MARKETS ARE CLOSED DIVIDEND YIELD MAY NOT DISPLAY
___________________________________________________________
Business Summary:
    """)
    # Print summary corresponding to the textwrap
    for line in word_list:
        print(line)

    print("\n")

    # Ask user what they want to do next
    while True:
        user_input = input("1: Enter another stock?\n2: Back to menu\n3: Quit")

        if user_input == '1':
            # Ask user for new stock
            return ask_for_stock()

        elif user_input == '2':
            # Return to option menu
            return app.option_menu()

        elif user_input == '3':
            quit()

        else:
            # Inform user
            print("Sorry please choose 1 of the 3 options.\n")
