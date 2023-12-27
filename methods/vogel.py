import numpy as np


class Vogel:
    def __init__(self, matrix):
        self.matrix = matrix

    def calculate_penalty(self):
        new_row = []
        for i, row in enumerate(self.matrix[:-1, :-1].T):
            row_sorted = sorted(row)[:2]
            new_row.append(row_sorted[1] - row_sorted[0])

        new_row.append(0)
        self.matrix = np.vstack((self.matrix, new_row))

        new_column = []
        for i, row in enumerate(self.matrix[:-2, :-1]):
            column_sorted = sorted(row)[:2]
            new_column.append(column_sorted[1] - column_sorted[0])

        new_column.append(0)
        new_column.append(0)
        self.matrix = np.column_stack((self.matrix, new_column))

        max_index = np.argmax(self.matrix[-1])

        print("Matriz Atualizada:")
        print(self.matrix)

    def get_difference_between_lower_costs(self):
        pass

    def get_biggest_difference(self):
        max_value = np.max(self.matrix[-1, :-1])
