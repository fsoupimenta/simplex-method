import numpy as np

from methods.vogel import Vogel
from problems.product_distribution import create_matrix

# from problems.input import create_matrix, columns_headers, rows_headers
# from methods.simplex import Simplex

if __name__ == '__main__':
    # matrix = create_matrix()
    # simplex = Simplex(matrix=matrix, columns_headers=columns_headers, rows_headers=rows_headers)
    # simplex.simplex()
    matrix = [
        [2, 3, 11, 7, 6],
        [1, 0, 6, 1, 1],
        [5, 8, 15, 9, 10],
        [7, 5, 3, 2, 0]
    ]

    vogel = Vogel(create_matrix().astype(float))
    # vogel = Vogel(np.array(matrix).astype(float))
    vogel.vogel_method()
