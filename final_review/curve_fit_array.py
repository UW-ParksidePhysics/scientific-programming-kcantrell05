@@ -0,0 +1,33 @@
""" 
This code computes and prints out the x and y values in an array using the quadratic equation. 
"""

__author__ =  'Olivia Manring' 

import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
    """
    This returns x and y values which the y values are computed by the quadratic equation
    :param quadratic_coefficients: shape(3,)
    :param min_x: float
    :param max_x: float
    :param number_of_points: int
    :return: fit_curve: ndarray, shape(2,N)
    """
    if max_x<min_x:
        raise ArithmeticError
    try:
        x_values = np.linspace(min_x, max_x, number_of_points)
        y_values = np.polyval(quadratic_coefficients, x_values)
        return [x_values, y_values]
    except IndexError as error:
        print(f'{error}')
    except ArithmeticError as error:
        print(f'{error}')


if __name__ == "__main__":
    test_coefficients = [0,0,1]
    print(fit_curve_array(test_coefficients, -2, 2, number_of_points=7))
