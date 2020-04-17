import matplotlib.pyplot as plot
from matplotlib import style
import datetime
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 4, 17)

# df = web.DataReader("^DJI", "yahoo", start, end)
# df.to_csv("dow.csv")

df = pd.read_csv("dow.csv", parse_dates=True, index_col=0)

df["Adj Close"].plot()
plot.show()
