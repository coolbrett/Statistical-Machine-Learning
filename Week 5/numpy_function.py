import numpy as np


def sum_of_squares(x_list):
    y_list = sum([x * x for x in x_list])


def sum_of_squares_np(x_list):
    np.square(x_list)
    return np.sum(x_list)


def cube_number(num):
    """
    This functions returns the parameter cubed
    :arg: number to be cubed
    :rtype: int of cubed number
    """
    return num * num * num
