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
