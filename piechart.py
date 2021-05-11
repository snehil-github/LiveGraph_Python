import matplotlib.pyplot as plot


def pie_chart(x, y):

    plot.style.use('bmh')
    plot.pie(y, labels=x, radius=1.2, autopct='%0.01f%%', shadow=True, explode=[.05, .2, .05, .2, .05, .2, .05])
    plot.show()

