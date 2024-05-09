@@ -0,0 +1,21 @@
"""
 This code creates a scatter plot and curve plot for the data and the fit polynomial 
 """

__author__ =  'Olivia Manring'


import numpy as np
import matplotlib.pyplot as plt

def plot_data_with_fit(data, fit_curve, data_format="o", fit_format=""):
    scatter_plot = plt.plot(data[0], data[1], data_format, color='Black')
    curve_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format, color='Orange')
    return scatter_plot, curve_plot

if __name__ == '__main__':
    data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
    fit_curve = [np.linspace(-2, 2), np.linspace(-2, 2) ** 2]

    scatter_plot, curve_plot = plot_data_with_fit(data, fit_curve)
    plt.show()
