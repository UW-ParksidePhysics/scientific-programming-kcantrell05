# """
# Read two columns of data from a text file.
# """

# __author__ = 'Cristian Marquez'

import numpy as np


def read_data_from_file(filename):
    """
    Read two columns of data from a text file.
    :param filename: str
        Name of the file to be read.
    :return data: ndarray
        Columns of data as rows of an array.
    """
    try:
        data = np.loadtxt(filename).transpose()
    except OSError as err:
        print(f'Error: {err}')
    return data


if __name__ == "__main__":
    test_file = '../python/volumes_energies.dat'
    test_data = read_data_from_file(test_file)
    print(f'test_data = {test_data}, shape = {test_data.shape}')
