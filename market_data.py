import yfinance as yf
import textwrap


def ask_for_stock():
    """
    Ask user for stock name

    :precondition: user_input must be a valid abbreviated stock name
    :postcodition: will return user_input as a parameter of check_with_user to check if user_input meets conditions
    :return: user_input as a string and as a parameter of check_with_user
    """
    user_input = input("Please input the stock abbreviated name.\n Example: Microsoft Corp. -> MSFT\n")
    return check_with_user(user_input)


def check_with_user(stock):
    while True:
        try:
            ticker = yf.Ticker(stock)
        except ImportError:
            print("We can't find the stock entered..")
            print("Please input the stock abbreviated name.\n Example: Microsoft Corp. -> MSFT\n")
        else:
            print("Is this the desired Company?")
            print(ticker.info['longName'])
            user_input = input("1. Yes\n2. No\n")
            if user_input == '1':
                return display_info(ticker.info)
            elif user_input == '2':
                "Make sure you enter the abbreviated stock name correctly"
                return ask_for_stock()


def display_info(stock_ticker):
    summary = stock_ticker['longBusinessSummary']

    wrapper = textwrap.TextWrapper(width=100)

    word_list = wrapper.wrap(text=summary)
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
    for line in word_list:
        print(line)
    print("\n")
    input("Hit any button to continue\n")

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
