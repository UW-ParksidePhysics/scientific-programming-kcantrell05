import numpy as np


diagonal_array = np.linspace(1, 5, 5)
off_diagonal_array = np.linspace(6, 9, 4)

# print(f'{diagonal_array}')
# print(f'{np.arange(1, 5+1)}')
practice_matrix = np.diag(diagonal_array) + np.diag(off_diagonal_array, k=-1)
print(f'{practice_matrix}')


print(f'max(A) = {np.amax(practice_matrix)}')

print(f'A / max(A) = {practice_matrix / np.amax(practice_matrix)}')  