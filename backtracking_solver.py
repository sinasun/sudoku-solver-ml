def save_board_to_csv(filename, board): 
    pass

def save_solution_to_csv(filename, board):
    pass

def find_empty_location(board):
    pass

def is_valid(board, row, col, num):
    pass

def backtrack(board):
    return False, board

def solve_sudoku(board):
    is_solvabel, solution = backtrack(board)
    if is_solvabel:
        save_board_to_csv("board.csv", board)
        save_solution_to_csv("board_solution.csv", board)

def read_boards(filename):
    # TODO: read from file
    boards = {}
    for board in boards:
        solve_sudoku(board)

def main():
    read_boards("initial_boards.csv")

if __name__ == "__main__":
    main()
