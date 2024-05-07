import numpy as np
import matplotlib.pyplot as plt

def parse_sum_output(file_name):
    tolerances = []
    errors = []
    maximum_indices = []
    with open(file_name, 'r') as file:
        for line in file:
            if 'epsilon' in line:
                parts = line.strip().split(',')
                epsilon = float(parts[0].split(': ')[1])
                exact_error = float(parts[1].split(': ')[1])
                n = int(parts[2].split('=')[1])
                tolerances.append(epsilon)
                errors.append(exact_error)
                maximum_indices.append(n)
    return tolerances, errors, maximum_indices

def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    plt.figure(figsize=(10, 6))
    plt.semilogy(maximum_indices, errors, marker='o', linestyle='-', color='blue', label='Exact Error')
    plt.semilogy(maximum_indices, tolerances, marker='o', linestyle='-', color='red', label='Tolerance')
    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Error / Tolerance')
    plt.title('Logarithmic Sum Error vs Maximum Index')
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    tolerances, errors, maximum_indices = parse_sum_output('logarithmic_sum.out')

    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)

