import matplotlib.pyplot as plot
import pandas as pd

# plot.style.use('bmh')
df = pd.read_csv('prices.csv')
x_ = df['Model']
y_ = df['Price']


def bar_graph(x, y):
    plot.xlabel('Model', fontsize='18')
    plot.ylabel('Prices', fontsize='18')
    plot.bar(x, y)
    plot.show()


bar_graph(x_, y_)