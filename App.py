import numpy as np


def get_pivot_column(array: np.array):
    return array[-1].index(min(array[-1]))


def get_pivot_row(array: np.array, pivot_column: int):
    pivot_row = None
    comparator = None

    for i, row in enumerate(array[:-1]):
        if comparator > row[-1] / row[pivot_column]:
            comparator = row[-1] / row[pivot_column]
            pivot_row = i

    return pivot_row


def matrix_scaling(array: np.array, pivot_row: int, pivot_column: int):
    array[pivot_row] = np.divide(array[pivot_row], array[pivot_row][pivot_column])

    for i in range(array.shape[0]):
        if i != pivot_row:
            value = array[i][pivot_column]
            for j in range(array.shape[1]):
                array[i][j] = array[i][j] - value * array[pivot_row][j]

    return array
