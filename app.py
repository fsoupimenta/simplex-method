from problems.input import create_matrix, columns_headers, rows_headers
from methods.simplex import Simplex

if __name__ == '__main__':
    matrix = create_matrix()
    simplex = Simplex(matrix=matrix, columns_headers=columns_headers, rows_headers=rows_headers)
    simplex.simplex()
