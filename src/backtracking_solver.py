import argparse
from board import Board

output_file = ""

def find_empty_location(board: Board):
    pass

def is_valid(board: Board, row, col, num):
    pass

def backtrack(board: Board):
    return False, board

def solve_sudoku(board: Board, output_file):
    solved, solution = backtrack(board)
    if solved: solution.append_to_file(output_file)

def read_boards(filename: str, output_file):
    # TODO: read from file
    boards = {}
    for board in boards:
        solve_sudoku(board, output_file)

def main():
    parser = argparse.ArgumentParser(prog="BacktrackSolver", description="Sudoku Solver using Backtracking algorithm", epilog="python3 backtracking_solver.py -i ../data/boards.csv -o ../data/solutions.csv")

    parser.add_argument('-i', '--input', default="../data/boards.csv", help="Input file of boards")
    parser.add_argument('-o', '--output', default="../data/solutions.csv", help="Output file for saving solutions")

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output

    read_boards(input_file, output_file)

if __name__ == "__main__":
    main()
