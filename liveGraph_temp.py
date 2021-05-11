import matplotlib.pyplot as plot_temp
import pandas as pd
import random


# dataframe_ = pd.read_csv()
xVal = [0, 1, 2, 3, 4, 5, 6, 8]
yVal = [0, 1, 2, 1, 4, 3, 6, 2]


def live_graph(x_Val, y_Val):

    plot_temp.style.use('fivethirtyeight')
    plot_temp.xlabel('Model', fontsize='18')
    plot_temp.ylabel('Prices', fontsize='18')

    plot_temp.scatter(x_Val, y_Val)
    plot_temp.plot(x_Val, y_Val)
    plot_temp.show()


live_graph(xVal, yVal)
