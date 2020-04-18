import matplotlib.pyplot as plot
import warnings
from matplotlib import style
import datetime

warnings.simplefilter(action="ignore", category=FutureWarning)
import pandas_datareader.data as web
import pandas as pd


def create_csv(start, end):
    """Create a csv files with the financial data of the DOW jones from 2020-1-1 to 2020-4-17.

    :param start: an object containing the datetime on January 1st, 2020
    :param end: an object containing the datetime on January 1st, 2020
    :precondition: start and end must be well-formed datetime objects
    :postcondition: a csv file has successfully been created and the financial history of the DOW jones over the
                    specified period has been written to it
    """
    data_frame = web.DataReader("^DJI", "yahoo", start, end)
    data_frame.to_csv("dow.csv")


def read_csv():
    """Read from the dow.csv file.
    
    :precondition: a well formed csv file named dow.csv exists
    :postcondition: successfully returns the data in the dow.csv file
    :return: the data in the dow.csv file
    """
    csv_file = "dow.csv"

    # read the data from the csv file, parsing the Dates to make the x-axis, setting index_col to zero to remove it
    data_frame = pd.read_csv(csv_file, parse_dates=True, index_col=0)
    return data_frame


def plot_data(data_frame):
    """Plot the daily closes for the DOW Jones over the past 4 months.

    :param data_frame: the data contained in the dow.cvs file
    :precondition: data_frame must be well-formed
    :postcondition: the daily closes of the dow over the past 4 months have been correctly plotted
    """
    # plot the price at daily close of the dow after each day
    data_frame["Close"].plot()

    # show the plot
    plot.show()

    input("Hit enter to continue")


def main():
    style.use("ggplot")
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2020, 4, 17)

    create_csv(start, end)
    data_frame = read_csv()
    plot_data(data_frame)


if __name__ == "__main__":
    main()
