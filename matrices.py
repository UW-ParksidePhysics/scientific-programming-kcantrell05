import numpy as np


matrix = np.array([[0, 1], [1, 0]])

determinant = np.linalg.det(matrix)
print(f'det(A) = {determinant}')

inverse_matrix = np.linalg.inv(matrix)
print(f'inv(A) = {inverse_matrix}')


eigenvalues, eigenvectors = np.linalg.eig(matrix)
for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors):
    print(f'lambda = {eigenvalue}')
    print(f'v = {eigenvector}')
    print()