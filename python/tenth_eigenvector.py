import numpy as np
import matplotlib.pyplot as plt


matrix_dimension = 10

x_values = np.linspace(0, 1, matrix_dimension)

y_function = np.sqrt(2) * np.sin(np.pi * x_values)

diagonal = 2 * np.ones(matrix_dimension)

off_diagonal = -1 * np.ones(matrix_dimension - 1)

H = np.diagflat(diagonal) + np.diagflat(off_diagonal, 1) + np.diagflat(off_diagonal, -1)

eigenvalues, eigenvectors = np.linalg.eig(H)

tenth_eigenvector = eigenvectors[:, matrix_dimension - 1]

plt.plot(x_values, tenth_eigenvector, label='Tenth Eigenvector of H')
plt.plot(x_values, y_function, label=r'$\sqrt{2}\sin(\pi x)$')
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Tenth Eigenvector of H vs. $\sqrt{2}\sin(\pi x)$')
plt.legend()
plt.grid(True)
plt.show()

