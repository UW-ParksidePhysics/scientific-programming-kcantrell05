import numpy as np

# Define the function f(t)
def f(t):
    return np.sin(t)

# Define the Fourier series approximation S(t; n)
def S(t, n):
    approximation = 0
    for i in range(1, n+1):
        approximation += (4 / (np.pi * (2*i - 1))) * np.sin((2*i - 1) * t)
    return approximation

# Parameters
n_values = [1, 3, 5, 10, 30, 100]
alpha_values = [0.01, 0.25, 0.49]
T = 2 * np.pi

# Generate table
print("n\tAlpha\tt\tError")
print("-" * 30)
for n in n_values:
    for alpha in alpha_values:
        for t_alpha in [alpha * T]:
            t = t_alpha
            error = f(t) - S(t, n)
            print(f"\n{n}\t{alpha}\t{t:.2f}\t{error:.6f}")
