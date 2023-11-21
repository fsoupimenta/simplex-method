import numpy as np

from simplex import Simplex

non_basic_variables = ['x' + str(i) for i in range(1, 31)]
basic_variables = ['f' + str(j) for j in range(1, 33)]
columns_headers = non_basic_variables + basic_variables + ['b']
rows_headers = basic_variables + ['Z']
matrix = [
    [0.7, 1.7, 0.1, 0.8, 0.9, 2.2, 3.8, 3.6, 2.2, 2.8, 0.1, 1.4, 3.4, 1.1, 3.2, 2.7, 3.9, 1.3, 1.6, 1.6, 0.5, 0.3, 1.2,
     1.1, 1.2, 3.6, 0.8, 1.1, 3.6, 2.2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 500],
    [4.5, 2.1, 3.7, 4.7, 1.4, 3.6, 2.5, 2.4, 4.9, 2.8, 3.6, 3.6, 2.1, 2.2, 1.3, 2.1, 3.1, 1.1, 3.1, 1.2, 2.3, 1.7, 3.8,
     1.3, 1.3, 4.3, 2.3, 3.6, 2.6, 3.2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 830]
]
objective = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
             -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0]
stock = [10, 18, 13, 14, 16, 18, 9, 12, 15, 11, 13, 10, 10, 8, 17, 18, 9, 13, 9, 8, 10, 10, 15, 18, 12, 9, 10, 17, 18,
         11]


def create_matrix():
    for i in range(len(non_basic_variables)):
        temp_array = np.zeros(len(columns_headers))
        temp_array[i] = 1
        temp_array[len(non_basic_variables) + i + 2] = 1
        temp_array[-1] = stock[i]
        matrix.append(temp_array)
    matrix.append(objective)

    return matrix
