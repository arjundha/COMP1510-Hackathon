import matplotlib.pyplot as plot
from matplotlib import style
import datetime
import pandas as pd
import pandas_datareader.data as web


def create_csv(start, end):
    data_frame = web.DataReader("^DJI", "yahoo", start, end)
    data_frame.to_csv("dow.csv")


def read_csv():
    # reading data from csv file, parsing the Dates to make the x-axis, setting index_col to zero to remove it
    csv_file = "dow.csv"
    data_frame = pd.read_csv(csv_file, parse_dates=True, index_col=0)
    return data_frame


def plot_data(data_frame):
    # plotting the price at Close of the dow after each day
    data_frame["Close"].plot()

    # showing the plot
    plot.show()


def main():
    style.use("ggplot")
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2020, 4, 17)
    create_csv(start, end)
    data_frame = read_csv()
    plot_data(data_frame)


if __name__ == "__main__":
    main()
