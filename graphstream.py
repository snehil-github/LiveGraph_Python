import pandas as pd
import  linegraph
import piechart
import bargraph


df = pd.read_csv('prices.csv')
x = df['Model']
y = df['Price']


piechart.pie_chart(x, y)
bargraph.bar_graph(x,y)
linegraph.line_graph(x, y)

