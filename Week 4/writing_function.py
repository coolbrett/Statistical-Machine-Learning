from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt


def automated_polynomial_regression_plot(x, y, d, fname):
    """
    Plots a polynomial regression based on degree passed in

    x - a 1d array of input data

    y - a 1d array of output data

    d - an integer (the degree of the polynomial)

    fname - a filename
    """
    poly_fit = PolynomialFeatures(degree=d, include_bias=False)
    quad_model = LinearRegression()
    quad_reg = make_pipeline(poly_fit, quad_model)
    quad_reg.fit(x.reshape(-1, 1), y)
    plt.scatter(x, y)


if __name__ == '__main__':
    automated_polynomial_regression_plot()
