import matplotlib.pyplot as plot
from matplotlib import style
import datetime
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")

#
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 4, 17)

# df = web.DataReader("^DJI", "yahoo", start, end)
# df.to_csv("dow.csv")

# reading data from csv file, parsing the Dates to make the x-axis, setting index_col to zero to remove it
csv_file = "dow.csv"
data_frame = pd.read_csv(csv_file, parse_dates=True, index_col=0)

# plotting the price at Close of the dow after each day
data_frame["Close"].plot()

# showing the plot
plot.show()
