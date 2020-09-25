import numpy as np


def sum_of_squares(x_list):
    y_list = sum([x * x for x in x_list])


def sum_of_squares_np(x_list):
    np.square(x_list)
    return np.sum(x_list)
