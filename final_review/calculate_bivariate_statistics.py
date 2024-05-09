@@ -0,0 +1,40 @@
"""
Extract statistics from a dataset.
"""

__author__ = 'Cristian Marquez'

import numpy as np
from scipy import stats

# Generate sample data
sample_x = np.linspace(-10, 10, 22)
sample_y = sample_x ** 2

def compute_bivariate_statistics(data):
        """
        Compute statistics from provided data.
        :param data: ndarray, shape(2,M)
        :return: statistics: ndarray, shape(6,)
        """
        try:
            stats_x = stats.describe(data[0])
            stats_y = stats.describe(data[1])
            statistics = np.array([stats_y.mean, np.sqrt(stats_y.variance), stats_x.minmax[0], stats_x.minmax[1], stats_y.minmax[0], stats_y.minmax[1]])
        except IndexError as e:
            print(f'Error: {e}')
        return statistics

if __name__ == "__main__":
        # Expected values
        expected_values = [np.mean(sample_y), np.sqrt(np.var(sample_y)), np.min(sample_x), np.max(sample_x), np.min(sample_y), np.max(sample_y)]

        # Statistical names
        stat_names = ['mean of y', 'std of y', 'min of x', 'max of x', 'min of y', 'max of y']

        print('name:expected:value')
        # Display computed statistics
        for name, expected, value in zip(stat_names, expected_values, compute_bivariate_statistics([sample_x, sample_y])):
            print(f'{name}: {expected}, {value}')
        #print(compute_bivariate_statistics(sample_x, sample_y)) # Commented out redundant print statement
