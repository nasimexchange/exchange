import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def simple_plot(X, y, title="", xlabel="", ylabel="", legend=[]):
    '''

    :param X: The X input
    :param y: y can be ndarray
    :param title: the title for whole graph
    :param xlabel: label of x-axis
    :param ylabel: label of y-axis
    :param legend: list of legends
    :return:
    '''
    fig, ax = plt.subplots()
    for i in range(y.shape[1]):
        ax.plot(X, y[:,i], label=legend[i])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='best')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    print("Hello Plot")
