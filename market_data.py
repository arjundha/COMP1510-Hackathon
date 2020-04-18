import yfinance as yf
import textwrap


def ask_for_stock():
    """
    Ask user for stock name.

    :precondition: user_input must be a valid abbreviated stock name
    :postcodition: will return user_input as a parameter of check_with_user to check if user_input meets conditions
    :return: user_input as a string and as a parameter of check_with_user
    """
    user_input = input("Please input the stock abbreviated name.\n Example: Microsoft Corp. -> MSFT\n")
    return check_with_user(user_input)


def check_with_user(stock):
    """
    Check if stock is valid.

    :param stock: abbreviated stock name
    :precondition: stock must be a string
    :precondition: user_input must be a number that corresponds with the options given
    :return: a function that corresponds with user_input
    """
    while True:
        try:
            # Declare ticker
            ticker = yf.Ticker(stock)
        except ImportError:
            # Except error and inform user
            print("We can't find the stock entered..")
            print("Please input the stock abbreviated name.\n Example: Microsoft Corp. -> MSFT\n")
        else:
            # Clarify with user
            print("Is this the desired Company?")
            print(ticker.info['longName'])
            user_input = input("1. Yes\n2. No\n")

            if user_input == '1':
                # Display info
                return display_info(ticker.info)
            elif user_input == '2':
                # Repeat if user is not satisfied
                "Make sure you enter the abbreviated stock name correctly"
                return ask_for_stock()


def display_info(stock_ticker):
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

    # Print information regarding stock_ticker
    print(f"""
{stock_ticker['shortName']}    {stock_ticker['currency']}           
_______________________________________________________

Daily High:         {stock_ticker['dayHigh']}

Ask:                {stock_ticker['ask']}

Daily Low:          {stock_ticker['dayLow']}

Open:               {stock_ticker['open']}

Dividend Yield:     {float(stock_ticker['dividendYield']) * 100}%


Business Summary:
    """)
    # Print summary corresponding to the textwrap
    for line in word_list:
        print(line)
    print("\n")
    # Wait for user
    input("Hit enter to continue\n")

    # Ask user what they want to do next
    while True:
        user_input = input("1: Enter another stock?\n2: Back to menu\n3: Quit")
        if user_input == '1':
            return ask_for_stock()
        elif user_input == '2':
            return
        elif user_input == '3':
            quit()
        else:
            print("Sorry please choose 1 of the 3 options.\n")
