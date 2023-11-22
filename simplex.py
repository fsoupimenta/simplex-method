import numpy as np

from output import export_to_sheet, export_results_to_txt


class Simplex:
    def __init__(self, matrix, columns_headers, rows_headers):
        self.matrix = np.array(matrix).astype(float)
        self.columns_headers = columns_headers
        self.rows_headers = rows_headers

    def get_pivot_column(self):
        return np.argmin(self.matrix[-1])

    def get_pivot_row(self, pivot_column: int):
        pivot_row = None
        comparator = float('inf')
        for i, row in enumerate(self.matrix[:-1]):
            if comparator > (row[-1] / row[pivot_column]) > 0:
                comparator = row[-1] / row[pivot_column]
                pivot_row = i

        return pivot_row

    def matrix_scaling(self, pivot_row: int, pivot_column: int):
        self.matrix[pivot_row] = np.divide(self.matrix[pivot_row], self.matrix[pivot_row][pivot_column])

        for i in range(self.matrix.shape[0]):
            if i != pivot_row:
                value = self.matrix[i][pivot_column]
                for j in range(self.matrix.shape[1]):
                    self.matrix[i][j] = self.matrix[i][j] - (value * self.matrix[pivot_row][j])

    def simplex(self):
        row_size = self.matrix.shape[0] + 2
        count = 1
        number_of_iterations = 0
        while min(self.matrix[-1]) < 0:
            pivot_column = self.get_pivot_column()
            pivot_row = self.get_pivot_row(pivot_column)
            export_to_sheet(columns_header=self.columns_headers, rows_header=self.rows_headers,
                            columns_to_color=pivot_column, row_to_color=pivot_row, matrix=self.matrix,
                            last_row_filled=count)
            self.matrix_scaling(pivot_row, pivot_column)
            self.rows_headers[pivot_row] = self.columns_headers[pivot_column]
            count += row_size
            number_of_iterations += 1
        export_to_sheet(columns_header=self.columns_headers, rows_header=self.rows_headers, matrix=self.matrix,
                        last_row_filled=count)
        export_results_to_txt(rows_headers=self.rows_headers, matrix=self.matrix,
                              number_of_iterations=number_of_iterations)

        print(round(self.matrix[-1][-1], 2))
