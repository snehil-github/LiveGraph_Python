import matplotlib.pyplot as plot


def line_graph(x, y):

    plot.style.use('bmh')
    plot.xlabel('Model', fontsize='18')
    plot.ylabel('Prices', fontsize='18')
    plot.scatter(x, y)
    plot.plot(x, y)
    plot.show()

