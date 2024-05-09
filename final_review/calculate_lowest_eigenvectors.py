@@ -0,0 +1,17 @@
""" This code produces the lowest eigenvalues and eigenvectors given a square matrix."""

__author__ = 'Olivia Manring'


import numpy as np

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    return eigenvalues[:number_of_eigenvectors], eigenvectors[:, :number_of_eigenvectors]

if __name__ == "__main__":
    test_matrix = [[2, -1], [-1, 2]]
    number_test_eigenvectors = 2
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(test_matrix, number_test_eigenvectors)
    print(f'eigenvalues = {eigenvalues}')
    print(f'eigenvectors = {eigenvectors}')
 25 changes: 25 additions & 0 deletions25  
final_review/calculate_quadratic_fit.py
@@ -0,0 +1,25 @@
"""
Calculate quadratic coefficients for a dataset.
"""

__author__ = 'Cristian Marquez'

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
