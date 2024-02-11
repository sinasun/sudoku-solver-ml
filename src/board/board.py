import numpy as np

class Board:
    def __init__(self) -> None:
        self.array = np.zeros((9, 9))

    def is_valid(self) -> bool:
        return True

    def to_string(self) -> str:
        flat_array = self.array.flatten()
        return np.array2string(flat_array)

    def append_to_file(self, filename):
        flat_array = self.array.flatten()
        np.savetxt(filename, flat_array, delimiter=',', fmt='%d')
