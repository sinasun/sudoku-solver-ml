import numpy as np

class Board:
    def __init__(self) -> None:
        self.array = np.zeros((9, 9))

    def get_cell(self, row: int, column: int) -> int:
        return self.array[row][column]

    def set_cell(self, row: int, column: int, value):
        self.array[row][column] = value

    def get_cell_row_possible_values(self, row: int) -> np.ndarray:
        return np.array([i for i in range(1, 10) if np.isin(self.array[row], i) is False])

    def get_cell_columns_possible_values(self, column: int) -> np.ndarray:
        return np.array([i for i in range(1, 10) if np.isin(self.array[:][column], i) is False])

    def get_cell_cube_possible_values(self, row: int, column: int) -> np.ndarray:
        cube_start_row = int(row // 3) * 3
        cube_end_row = cube_start_row + 3
        cube_start_column = int(column // 3) * 3
        cube_end_column = cube_start_column + 3
        cube_array = self.array[cube_start_row:cube_end_row][cube_start_column:cube_end_column]

        return np.array([i for i in range(1, 10) if np.isin(cube_array, i) is False])

    def get_cell_possible_values(self, row: int, column: int) -> np.ndarray:
        row_values = self.get_cell_row_possible_values(row)
        column_values = self.get_cell_columns_possible_values(column)
        cube_values = self.get_cell_cube_possible_values(row, column)
        return np.intersect1d(row_values, np.intersect1d(column_values, cube_values))

    def is_valid(self) -> bool:
        return True

    def to_string(self) -> str:
        flat_array = self.array.flatten()
        return np.array2string(flat_array)

    def append_to_file(self, filename):
        flat_array = self.array.flatten()
        np.savetxt(filename, flat_array, delimiter=',', fmt='%d')
