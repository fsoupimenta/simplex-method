import numpy as np


class Vogel:
    def __init__(self, matrix):
        self.matrix = matrix

        self.result_matrix = np.zeros_like(self.matrix[:-1, :-1])
        self.answer = ""
        self.zmax = 0.0

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

        print("Matriz With Penalty:")
        print(self.matrix)

    def operate_demand_capacity(self, minimum_between, column_index, row_index):
        self.matrix[-2, column_index] -= minimum_between
        self.matrix[row_index, -2] -= minimum_between

    def construct_answer(self, minimum_between, column, row):
        if minimum_between != 0:
            self.answer += f"X-Row: {row} - Column: {column} = {minimum_between}\n"
        self.result_matrix[row][column] = minimum_between

    def construct_zmax(self, minimum_between, cell_value):
        if not np.isinf(cell_value):
            self.zmax += (minimum_between * cell_value)

    def dummy(self):
        sum_last_column = np.sum(self.matrix[:, -1])
        sum_last_row = np.sum(self.matrix[-1, :])

        if sum_last_column > sum_last_row:
            difference = abs(sum_last_column - sum_last_row)
            zeros_column = np.zeros(self.matrix.shape[0])
            zeros_column[-1] = difference
            self.matrix = np.insert(self.matrix, 0, zeros_column, axis=1)
        elif sum_last_row > sum_last_column:
            difference = abs(sum_last_row - sum_last_column)
            zeros_row = np.zeros(self.matrix.shape[1])
            zeros_row[-1] = difference
            self.matrix = np.insert(self.matrix, 0, zeros_row, axis=0)

    def capacity_penalty_bigger(self, max_index_last_column):
        penalty_line = self.matrix[max_index_last_column, : -2]
        minor_value_index_column = np.argmin(penalty_line)

        min_between = min(self.matrix[max_index_last_column, -2], self.matrix[-2, minor_value_index_column])

        self.operate_demand_capacity(min_between, minor_value_index_column, max_index_last_column)

        self.construct_answer(min_between, minor_value_index_column, max_index_last_column)
        self.construct_zmax(min_between, self.matrix[max_index_last_column, minor_value_index_column])

        self.matrix = self.matrix[:-1, :-1]

        if self.matrix[max_index_last_column, -1] == 0:
            self.matrix[max_index_last_column, :-1] = np.inf
        if self.matrix[-1, minor_value_index_column] == 0:
            self.matrix[:-1, minor_value_index_column] = np.inf

    def demand_penalty_bigger(self, max_index_last_row):
        penalty_column = self.matrix[:-2, max_index_last_row]
        minor_value_index_row = np.argmin(penalty_column)

        min_between = min(self.matrix[-2, max_index_last_row], self.matrix[minor_value_index_row, -2])

        self.operate_demand_capacity(min_between, max_index_last_row, minor_value_index_row)

        self.construct_answer(min_between, max_index_last_row, minor_value_index_row)
        self.construct_zmax(min_between, self.matrix[minor_value_index_row, max_index_last_row])

        self.matrix = self.matrix[:-1, :-1]

        if self.matrix[-1, max_index_last_row] == 0:
            self.matrix[:-1, max_index_last_row] = np.inf
        if self.matrix[minor_value_index_row, -1] == 0:
            self.matrix[minor_value_index_row, :-1] = np.inf

    def vogel_method(self):
        self.dummy()

        while True:
            self.calculate_penalty()
            if np.isinf(self.matrix[-1]).any():
                # indices_inf_last_row = np.where(np.isinf(self.matrix[-1]))[0]

                indices_row_with_non_inf = np.where(np.isfinite(self.matrix[:-2, : -2]).any(axis=1))[0]

                for i, demand_row_value in enumerate(self.matrix[-2, :-2]):
                    min_between = min(self.matrix[indices_row_with_non_inf, -2][0], demand_row_value)
                    self.operate_demand_capacity(min_between, i, indices_row_with_non_inf)

                    self.construct_answer(min_between, i, indices_row_with_non_inf[0])
                    self.construct_zmax(min_between, self.matrix[indices_row_with_non_inf, i][0])

                print("Final Matrix:\n", self.result_matrix)
                print("Answer:\n", self.answer)
                print("Zmax:\n", self.zmax)
                break

            if np.isinf(self.matrix[:, -1]).any():
                indices_inf_last_column = np.where(np.isinf(self.matrix[:, -1]))[0]
                indices_columns_without_inf = np.where(np.isfinite(self.matrix[:-2, :-2]).any(axis=0))[0]
                for i, capacity_column_value in enumerate(self.matrix[:-2, -2]):
                    min_between = min(self.matrix[-2, indices_columns_without_inf][0], capacity_column_value)
                    self.operate_demand_capacity(min_between, i, indices_columns_without_inf)

                    self.construct_answer(min_between, i, indices_columns_without_inf[0])
                    self.construct_zmax(min_between, self.matrix[i, indices_columns_without_inf][0])

                print("Final Matrix:\n", self.result_matrix)
                print("Answer:\n", self.answer)
                print("Zmax:\n", self.zmax)
                # That logic way needs to be verified
                break

            max_index_last_row = np.nanargmax(self.matrix[-1])
            max_index_last_column = np.nanargmax(self.matrix[:, -1])
            value_last_row = self.matrix[-1, max_index_last_row]
            value_last_column = self.matrix[max_index_last_column, -1]

            if value_last_column >= value_last_row:
                self.capacity_penalty_bigger(max_index_last_column)

            else:
                self.demand_penalty_bigger(max_index_last_row)
