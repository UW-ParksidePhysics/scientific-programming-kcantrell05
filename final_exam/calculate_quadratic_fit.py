# @@ -0,0 +1,25 @@
# """
# Calculate quadratic coefficients for a dataset.
# """

# __author__ = 'Cristian Marquez'

import numpy as np


def compute_quadratic_coefficients(data):
    """
    Calculate quadratic coefficients for a given dataset.
    :param data: ndarray, shape(2,M)
    :return: quadratic_coefficients: ndarray, shape(3,)
    """
    quadratic_coefficients = np.polyfit(data[0], data[1], 2)
    ordered_quadratic_coefficients = [quadratic_coefficients[-1], quadratic_coefficients[1], quadratic_coefficients[0]]

    return quadratic_coefficients

if __name__ == "__main__":
    value_names = ['quadratic coefficient', 'linear coefficient', 'constant coefficient']
    for name, value in zip(value_names, compute_quadratic_coefficients([np.linspace(-1, 1), np.linspace(-1, 1)**2])):
        print(f'{name}: {value}')
