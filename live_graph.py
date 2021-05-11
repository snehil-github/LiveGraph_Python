from matplotlib.animation import FuncAnimation
from multiprocessing import Process
from itertools import count
import threading
import matplotlib.pyplot as plt
import random
import pandas as pd
import random
import csv
import time

# def datafile():
#     x_value = 0
#     total_1 = 1000
#     total_2 = 1000

#     fieldnames = ["x_value", "total_1", "total_2"]

#     with open('data.csv', 'w') as csv_file:
#         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         csv_writer.writeheader()

#     while True:

#         with open('data.csv', 'a') as  csv_file:
#             csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#             info = {
#                 "x_value": x_value,
#                 "total_1": total_1,
#                 "total_2": total_2
#             }

#             csv_writer.writerow(info)
#             print(x_value, total_1, total_2)


#             x_value += 1
#             total_1 = total_1 + random.randint(-6, 8)
#             total_2 = total_2 + random.randint(-5, 6)


#         time.sleep(1)

def livegraph():

    x_val = []
    y_val = []

    index = count()

    def animate(i):
        data = pd.read_csv('data.csv')
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']

        plt.cla()

        plt.plot(x, y1, label='Channel 1')
        plt.plot(x, y2, label='Channel 2')
        plt.legend(loc='upper left')
        plt.tight_layout()
        

    animate_ = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    
    t1 = threading.Thread(target=livegraph())
    t1.start()
    t1.join()

    # t2 = threading.Thread(target=datafile())    
    # t2.start()
    # t2.join()